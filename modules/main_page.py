import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import sqlite3
from PIL import ImageTk, Image
import pandas as pd
import numpy as np
from modules.thermal_conductivity_model.thermal_conductivity_model import ThermalConductivityModel
from modules.segregation_potential_model import SegregationPotentialModel
from modules.climate_model import ClimateModelGeneral, ClimateModelSpecial
from modules.model_control.model_control_window import ModelControlWindow
from modules.notes_window import NotesWindow
from modules.material_database_window import MaterialDatabaseWindow
from modules.toolbar import ToolBar
from modules.model_control.calculation import SSR_model
from modules.figures import PlotFigure1, PlotFigure2
from modules.model_control.parameter_stydy import ParameterStudy
from modules.development_window import DevelopmentWindow

import matplotlib

matplotlib.use('TkAgg')

con = sqlite3.connect("modules/material_database.db")
cur = con.cursor()

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class MainPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        self['style'] = 'Standard.TFrame'
        self.entry_container = []
        self.layers_df = pd.DataFrame
        self.data_df = pd.DataFrame
        self.other_df = pd.DataFrame
        self.chaussee_df = pd.DataFrame
        self.site_df = pd.DataFrame
        self.figure1_object = None
        self.figure2_object = None

        # Adding toolbar frame
        self.toolbar_frame = ttk.Frame(self)
        self.toolbar_frame.pack(side='top', fill='x')
        self.toolbar = ToolBar(self.toolbar_frame, self)

        # Adding main frame
        self.main_frame = ttk.Frame(self, padding=10, style='Standard.TFrame')
        self.main_frame.pack(side='top', fill='both', expand=True)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        # Adding main left and right frames
        self.main_frame_left_side = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.main_frame_left_side.grid(row=0, column=0, sticky='nsew')
        self.main_frame_right_side = ttk.Frame(self.main_frame, style='Standard.TFrame')
        #self.main_frame_right_side.grid(row=0, column=1, sticky='nsew', padx=(10, 0))
        self.empty_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.empty_frame.grid(row=0, column=1)

        # Adding frames in the left side top part (material selection and properties)
        self.mat_properties_frame = ttk.Frame(self.main_frame_left_side, style='Standard.TFrame')
        self.mat_properties_frame.pack(side='top', fill='x')
        self.mat_properties_title_frame = ttk.Frame(self.mat_properties_frame, style='Standard.TFrame')
        self.mat_properties_title_frame.pack(side='top', fill='x')
        self.mat_properties_main_frame = ttk.Frame(self.mat_properties_frame, padding=10, style='Standard.TFrame')
        self.mat_properties_main_frame.pack(side='top', fill='x')

        # Adding figure frames
        self.figure_1_frame = ttk.Frame(self.main_frame_right_side, style='Standard.TFrame')
        self.figure_1_frame.pack(side='top', fill='both', expand=True, pady=(0, 5))
        self.figure_2_frame = ttk.Frame(self.main_frame_right_side, style='Standard.TFrame')
        self.figure_2_frame.pack(side='top', fill='both', expand=True, pady=(5, 0))

        # Adding frame for climate and note options
        self.climate_control_notes_frame = ttk.Frame(self.main_frame_left_side, style='Standard.TFrame')
        self.climate_control_notes_frame.pack(side='top', fill='x', pady=(20, 0))

        # Adding climate, notes and model control frames
        self.climate_frame = ttk.Frame(self.climate_control_notes_frame, style='Standard.TFrame')
        self.climate_frame.pack(side='left', fill='both')

        self.climate_pages = dict()
        for climate_class in [ClimateModelGeneral, ClimateModelSpecial]:
            model_page = climate_class(self.climate_frame, self)
            self.climate_pages[climate_class] = model_page
            model_page.grid(row=0, column=0, sticky='nsew')

        self.switch_climate_model(1)

        self.notes_control_frame = ttk.Frame(self.climate_control_notes_frame, style='Standard.TFrame')
        self.notes_control_frame.pack(side='left', fill='both', expand=True, padx=(10, 0))
        self.model_control_window = ModelControlWindow(self.notes_control_frame, self)
        self.notes_window = NotesWindow(self.notes_control_frame, self)
        self.development_window = DevelopmentWindow(self.notes_control_frame, self)


        # Add title frame and label material layer selection
        self.top_label_frame = ttk.Frame(self.mat_properties_title_frame, style='DarkFrame.TFrame')
        self.top_label_frame.pack(side='top', fill='x')

        self.main_title = ttk.Label(
            self.top_label_frame,
            text='Material layer selection',
            style='ExtraLargeLabel.TLabel')
        self.main_title.pack(side='left', padx=(10, 0), pady=(5, 5))

        # Initial entry lines
        for i in range(1, 5, 1):
            entry_line = EntryLine(self.mat_properties_main_frame, i, self)
            entry_line.pack_objects()
            self.entry_container.append(entry_line)

        # Adding material database button
        self.material_db_button = ttk.Button(
            self.mat_properties_main_frame,
            text='Open material database',
            width=35,
            style='Standard.TButton',
            takefocus=False,
            command=self.open_material_database)
        self.material_db_button.grid(row=5, column=0, columnspan=5, pady=(10, 0))

        # Adding labels to top row (material selection and properties)
        self.top_label1 = ttk.Label(self.mat_properties_main_frame, text='Material', style='Standard.TLabel')
        self.top_label2 = ttk.Label(self.mat_properties_main_frame, text='H, m', style='Standard.TLabel')

        self.label_rhod = ttk.Label(self.mat_properties_main_frame, text='rhod', style='Standard.TLabel')
        self.label_rhos = ttk.Label(self.mat_properties_main_frame, text='rhos', style='Standard.TLabel')
        self.label_n = ttk.Label(self.mat_properties_main_frame, text='n', style='Standard.TLabel')
        self.label_w_grav = ttk.Label(self.mat_properties_main_frame, text='w%', style='Standard.TLabel')
        self.label_sp_val = ttk.Label(self.mat_properties_main_frame, text='SP', style='Standard.TLabel')
        self.label_a_val = ttk.Label(self.mat_properties_main_frame, text='a', style='Standard.TLabel')
        self.label_ku = ttk.Label(self.mat_properties_main_frame, text='ku', style='Standard.TLabel')
        self.label_kf = ttk.Label(self.mat_properties_main_frame, text='kf', style='Standard.TLabel')
        self.label_sr = ttk.Label(self.mat_properties_main_frame, text='Sr', style='Standard.TLabel')
        self.label_lf = ttk.Label(self.mat_properties_main_frame, text='Lf', style='Standard.TLabel')

        # Packing top row labels (material selection and properties)
        self.top_label1.grid(row=0, column=3, padx=(5, 0), pady=(3, 0))
        self.top_label2.grid(row=0, column=4, padx=(5, 0), pady=(3, 0))

        self.label_rhod.grid(row=0, column=5, padx=(30, 0), pady=(3, 0))
        self.label_rhos.grid(row=0, column=6, padx=(7, 0), pady=(3, 0))
        self.label_n.grid(row=0, column=7, padx=(7, 0), pady=(3, 0))
        self.label_w_grav.grid(row=0, column=8, padx=(7, 0), pady=(3, 0))
        self.label_sp_val.grid(row=0, column=9, padx=(7, 0), pady=(3, 0))
        self.label_a_val.grid(row=0, column=11, padx=(7, 0), pady=(3, 0))
        self.label_ku.grid(row=0, column=12, padx=(7, 0), pady=(3, 0))
        self.label_kf.grid(row=0, column=13, padx=(7, 0), pady=(3, 0))
        self.label_sr.grid(row=0, column=15, padx=(7, 0), pady=(3, 0))
        self.label_lf.grid(row=0, column=16, padx=(7, 0), pady=(3, 0))

    def load_full_file(self):
        file_name = filedialog.askopenfilename(
            initialdir=r'C:\Users\karlisr\OneDrive - NTNU\2_PostDoc_NTNU\01_SSR_project_Model_development\08_SSR_model_python_app_ACTIVE\data',
            title='Select a file',
            filetypes=(('Excel files', '.xlsx'), ('All files', '*.*')))

        # Layers sheet
        self.layers_df = pd.read_excel(file_name, sheet_name='layers')
        material_count = len(self.layers_df['ku'])
        current_entry_lines = len(self.entry_container)

        while material_count != current_entry_lines:
            if material_count > current_entry_lines:
                self.add_new_line(current_entry_lines-1)
                current_entry_lines = len(self.entry_container)
            elif material_count < current_entry_lines:
                self.remove_line(current_entry_lines-1)
                current_entry_lines = len(self.entry_container)

        counter = 0
        for entry_line in self.entry_container:
            entry_line.entry1.set(str(counter+1))
            entry_line.entry2.set(self.layers_df.iloc[counter]['height'])
            entry_line.var_rhod.set(self.layers_df.iloc[counter]['rhod'])
            entry_line.var_rhos.set(1)
            entry_line.var_n.set(1)
            entry_line.var_w_grav.set(self.layers_df.iloc[counter]['w_vol'])
            entry_line.var_sp_val.set(self.layers_df.iloc[counter]['SP'])
            entry_line.var_a_val.set(self.layers_df.iloc[counter]['a'])
            entry_line.var_ku.set(self.layers_df.iloc[counter]['ku'])
            entry_line.var_kf.set(self.layers_df.iloc[counter]['kf'])
            entry_line.var_sr.set(self.layers_df.iloc[counter]['Sr'])
            entry_line.var_lf.set(self.layers_df.iloc[counter]['Ls'])
            counter += 1

        # Data sheet
        self.data_df = pd.read_excel(file_name, sheet_name='data')

        # Other sheet
        self.other_df = pd.read_excel(file_name, sheet_name='other').to_numpy()

        # Chaussee sheet
        self.chaussee_df = pd.read_excel(file_name, sheet_name='chaussee')

        # Site sheet
        self.site_df = pd.read_excel(file_name, sheet_name='site')

    def status(self):
        print("\n")
        for i in self.entry_container:
            print(i.row)

    def repack_db_button(self):
        self.material_db_button.grid_forget()
        row = len(self.entry_container) + 1
        self.material_db_button.grid(row=row, column=0, columnspan=5, pady=(10, 0))

    def add_new_line(self, row):
        new_line = EntryLine(self.mat_properties_main_frame, row, self)
        new_line.pack_objects()
        self.entry_container.insert(row-1, new_line)

        for i in self.entry_container[row:]:
            i.row += 1
            i.forget_objects()
            i.pack_objects()

        if len(self.entry_container) > 1:
            for i in self.entry_container:
                i.minus_button["state"] = "normal"
        if len(self.entry_container) > 9:
            for i in self.entry_container:
                i.plus_button["state"] = "disabled"
        self.repack_db_button()

    def remove_line(self, row):
        if row == len(self.entry_container):
            self.entry_container[row-1].delete_object()
            del self.entry_container[row-1]
            for entry_line in self.entry_container:
                entry_line.forget_objects()
                entry_line.pack_objects()
        else:
            self.entry_container[row-1].delete_object()
            del self.entry_container[row-1]

            for entry_line in self.entry_container[row-1:]:
                entry_line.row -= 1

            for entry_line in self.entry_container:
                entry_line.forget_objects()
                entry_line.pack_objects()
                entry_line.row_line_number["text"] = str(entry_line.row) + "."

        if len(self.entry_container) == 1:
            self.entry_container[0].minus_button["state"] = "disabled"
        if len(self.entry_container) < 10:
            for i in self.entry_container:
                i.plus_button["state"] = "normal"
        self.repack_db_button()

    def disable_entry_line(self, row):
        """The function disables or enables editing of content in specific row after the user has clicked on the
        checkbutton"""
        if self.entry_container[row-1].checked.get() == 0:
            self.entry_container[row - 1].entry_rhod["state"] = "disabled"
            self.entry_container[row - 1].entry_rhos["state"] = "disabled"
            self.entry_container[row - 1].entry_n["state"] = "disabled"
            self.entry_container[row - 1].entry_w_grav["state"] = "disabled"
            self.entry_container[row - 1].entry_sp_val["state"] = "disabled"
            self.entry_container[row - 1].entry_sp_opt_button["state"] = "disabled"
            self.entry_container[row - 1].entry_a_val["state"] = "disabled"
            self.entry_container[row - 1].entry_ku["state"] = "disabled"
            self.entry_container[row - 1].entry_kf["state"] = "disabled"
            self.entry_container[row - 1].entry_th_opt_button["state"] = "disabled"
            #self.entry_container[row - 1].entry_sr["state"] = "disabled"
            #self.entry_container[row - 1].entry_lf["state"] = "disabled"
            #self.entry_container[row - 1].entry_lf_opt_button["state"] = "disabled"

        elif self.entry_container[row-1].checked.get() == 1:
            self.entry_container[row - 1].entry_rhod["state"] = "normal"
            self.entry_container[row - 1].entry_rhos["state"] = "normal"
            self.entry_container[row - 1].entry_n["state"] = "normal"
            self.entry_container[row - 1].entry_w_grav["state"] = "normal"
            self.entry_container[row - 1].entry_sp_val["state"] = "normal"
            self.entry_container[row - 1].entry_sp_opt_button["state"] = "normal"
            self.entry_container[row - 1].entry_a_val["state"] = "normal"
            self.entry_container[row - 1].entry_ku["state"] = "normal"
            self.entry_container[row - 1].entry_kf["state"] = "normal"
            self.entry_container[row - 1].entry_th_opt_button["state"] = "normal"
            #self.entry_container[row - 1].entry_sr["state"] = "normal"
            #self.entry_container[row - 1].entry_lf["state"] = "normal"
            #self.entry_container[row - 1].entry_lf_opt_button["state"] = "normal"

    def combobox_selection(self, event, row):
        materials = cur.execute("SELECT * FROM materials").fetchall()
        material_names = []
        for i in materials:
            material_names.append(i[1])
        selected_material = self.entry_container[row-1].var_mat_selection.get()
        mat_index = material_names.index(selected_material)

        self.entry_container[row-1].var_rhod.set(materials[mat_index][2])
        self.entry_container[row-1].var_w_grav.set(materials[mat_index][3])
        self.entry_container[row-1].var_sp_val.set(materials[mat_index][4])
        self.entry_container[row-1].var_a_val.set(materials[mat_index][5])
        self.entry_container[row-1].var_ku.set(materials[mat_index][6])
        self.entry_container[row-1].var_kf.set(materials[mat_index][7])
        self.entry_container[row-1].var_sr.set(materials[mat_index][8])
        self.entry_container[row-1].var_lf.set(materials[mat_index][9])

    def kf_thermal_conductivty_model(self, row):
        th_model = ThermalConductivityModel(row, self)

    def segregation_potential_model(self, row):
        sp_model = SegregationPotentialModel(row)

    def open_material_database(self):
        material_database = MaterialDatabaseWindow()

    # Toolbar options
    def toolbar_button_new(self):
        pass

    def toolbar_button_open(self):
        pass

    def toolbar_button_save(self):
        pass

    def toolbar_button_info(self):
        pass

    def calculate_entry_changes(self, event, entry, row):
        """This function dynamically updates entry fields for rhod, sr an lf. All fields must be real numbers for
        function to take action. Changed -> Updated executed as follow:
        rhod -> n, sr, lf
        rhos -> n, sr, lf
        n -> rhod, sr, lf
        w_grav -> sr, lf

        Future implementations: if user overrides sr or lf values this should be implemented as follows:
        sr -> w_grav, lf
        lf -> w_grav, lf"""
        entry_line = self.entry_container[row - 1]
        if entry == 'rhod':
            try:
                # calculate porosity
                porosity = 1-float(entry_line.var_rhod.get()) / float(entry_line.var_rhos.get())
                entry_line.var_n.set(f'{porosity:.2f}')

                # calculate saturation
                saturation = float(entry_line.var_w_grav.get())*(float(entry_line.var_rhod.get()) /
                                                                 float(entry_line.var_n.get()))
                entry_line.var_sr.set(f'{saturation:.0f}')
                if float(entry_line.var_sr.get()) > 100:
                    entry_line.entry_sr.configure(style='RedWarning.TEntry')
                else:
                    entry_line.entry_sr.configure(style='Standard.TEntry')

                # calculate latent heat
                latent_heat = (float(entry_line.var_w_grav.get())/100) * (float(entry_line.var_rhod.get())/1) * 92500
                entry_line.var_lf.set(f'{latent_heat:.0f}')
            except:
                pass
        elif entry == 'rhos':
            try:
                # calculate porosity
                porosity = 1 - float(entry_line.var_rhod.get()) / float(entry_line.var_rhos.get())
                entry_line.var_n.set(f'{porosity:.2f}')

                # calculate saturation
                saturation = float(entry_line.var_w_grav.get()) * (float(entry_line.var_rhod.get()) /
                                                                   float(entry_line.var_n.get()))
                entry_line.var_sr.set(f'{saturation:.0f}')
                if float(entry_line.var_sr.get()) > 100:
                    entry_line.entry_sr.configure(style='RedWarning.TEntry')
                else:
                    entry_line.entry_sr.configure(style='Standard.TEntry')
            except:
                pass
        elif entry == 'n':
            try:
                # calculate rhod
                rhod = float(entry_line.var_rhos.get()) * (1 - float(entry_line.var_n.get()))
                entry_line.var_rhod.set(f'{rhod:.2f}')

                # calculate saturation
                saturation = float(entry_line.var_w_grav.get()) * (float(entry_line.var_rhod.get()) /
                                                                   float(entry_line.var_n.get()))
                entry_line.var_sr.set(f'{saturation:.0f}')
                if float(entry_line.var_sr.get()) > 100:
                    entry_line.entry_sr.configure(style='RedWarning.TEntry')
                else:
                    entry_line.entry_sr.configure(style='Standard.TEntry')

                # calculate latent heat
                latent_heat = (float(entry_line.var_w_grav.get())/100) * (float(entry_line.var_rhod.get())/1) * 92500
                entry_line.var_lf.set(f'{latent_heat:.0f}')
            except:
                pass
        elif entry == 'w_grav':
            try:
                # calculate saturation
                saturation = float(entry_line.var_w_grav.get()) * (float(entry_line.var_rhod.get()) /
                                                                   float(entry_line.var_n.get()))
                entry_line.var_sr.set(f'{saturation:.0f}')
                if float(entry_line.var_sr.get()) > 100:
                    entry_line.entry_sr.configure(style='RedWarning.TEntry')
                else:
                    entry_line.entry_sr.configure(style='Standard.TEntry')

                # calculate latent heat
                latent_heat = (float(entry_line.var_w_grav.get())/100) * (float(entry_line.var_rhod.get())/1) * 92500
                entry_line.var_lf.set(f'{latent_heat:.0f}')
            except:
                pass
        elif entry == 'sr':
            try:
                saturation = float(entry_line.var_sr.get())
                entry_line.var_sr.set(f'{saturation:.0f}')
            except:
                pass

    # Menu options
    def toolbar_on_off(self, status):
        """"The function removes or adds back teh status bar. Because of teh packing also teh main frame has
        to be repacked. (Note: This makes me think that maybe using teh grid geometry manager would actually
        allow to add or remove widgets from certain location without having to repack other widgets)"""
        if not status:
            self.toolbar_frame.pack_forget()
        elif status:
            self.main_frame.pack_forget()
            self.toolbar_frame.pack(side='top', fill='x')
            self.main_frame.pack(side='top', fill='x')

    def switch_climate_model(self, selection):
        if selection == 1:
            climate_page = self.climate_pages[ClimateModelGeneral]
            climate_page.tkraise()
        elif selection == 2:
            climate_page = self.climate_pages[ClimateModelSpecial]
            climate_page.tkraise()

    def switch_flux_model(self, selection):
        print(selection)

    def show_hide_figures(self, status):
        if status == True:
            self.empty_frame.grid_forget()
            self.main_frame_right_side.grid(row=0, column=1, sticky='nsew', padx=(10, 0))
        elif status == False:
            self.empty_frame.grid(row=0, column=1)
            self.main_frame_right_side.grid_forget()

    # Button functionality
    def run_calculation_for_single_case(self):
        """The button is located in the model control window.
        This function runs the calculation with a loaded file"""
        model_object = SSR_model(self.layers_df, self.data_df, self.other_df, self.chaussee_df, self.site_df)
        array_df, interface_lim_list, chaussee_file_chau_z_list, chaussee_file_day_list, site_file_day_list,\
        site_file_site_z_list, layer_count, chaussee_file_chau_h_list, site_file_site_h_list = model_object.SSR_calculate_single_test_case()
        self.figure1_object = PlotFigure1(self.figure_1_frame, array_df, interface_lim_list, chaussee_file_chau_z_list,
                    chaussee_file_day_list, site_file_day_list, site_file_site_z_list, layer_count,
                    chaussee_file_chau_h_list, site_file_site_h_list)
        self.figure2_object = PlotFigure2(self.figure_2_frame, array_df, interface_lim_list, chaussee_file_chau_z_list,
                                     chaussee_file_day_list, site_file_day_list, site_file_site_z_list, layer_count,
                                     chaussee_file_chau_h_list, site_file_site_h_list)
        self.figure1_object.plot_figure1()
        self.figure2_object.plot_figure2()
        self.main_frame_right_side.grid(row=0, column=1, sticky='nsew', padx=(10, 0))
        self.empty_frame.grid_forget()

    def run_calculation_for_new_cases(self):
        pass
        # Step 1. Collect all the input parameters into a proper df
        columns = ['name', 'height', 'ku', 'kf', 'SP', 'a', 'Sr', 'Ls', 'w_vol', 'rhod']
        np_array = np.array([])
        column = []
        index = []
        for material in self.entry_container:
            index.append(material.entry1.get())
            column.append(float(material.entry2.get()))
            column.append(float(material.var_ku.get()))
            column.append(float(material.var_kf.get()))
            column.append(float(material.var_sp_val.get()))
            column.append(float(material.var_a_val.get()))
            column.append(float(material.var_sr.get()))
            column.append(float(material.var_lf.get()))
            column.append(float(material.var_w_grav.get()))
            column.append(float(material.var_rhod.get()))
            print(np.array(column))
            column.clear()

        # Step 2. Collect all the temperature into a proper df

    def open_parameter_study(self):
        material_names = []
        for entry in self.entry_container:
            material_names.append(entry.var_mat_selection.get())
        ParameterStudy(self, material_names)

    def run_parameter_study(self, layer_selected, property_selected, values):
        """ This button is located in the parameter study window.
        The function executes multiple calculations with the parameters given by the user"""
        print(layer_selected)
        print(property_selected)
        print(values)

    def run_climate_study(self):
        pass


class EntryLine:
    def __init__(self, parent, row, controller):
        self.parent = parent
        self.row = row
        self.controller = controller

        self.plus_sign_image = tk.PhotoImage(file="modules/icons/sq_plus_icon&16_inverted.png")
        self.minus_sign_image = tk.PhotoImage(file="modules/icons/sq_minus_icon&16_inverted.png")
        self.opt_img = Image.open("modules/icons/2x2_grid_icon&16_inverted.png")
        self.opt_img_resized = ImageTk.PhotoImage(self.opt_img.resize((8, 8), Image.ANTIALIAS))

        self.var_mat_selection = tk.StringVar()
        materials = cur.execute("SELECT * FROM materials").fetchall()
        material_list = []
        for i in materials:
            material_list.append(i[1])

        # Adding material selection widgets
        self.var_line_number = tk.StringVar(value=self.row)
        self.row_line_number = ttk.Label(
            self.parent,
            width=2,
            textvariable=self.var_line_number,
            style='Standard.TLabel',
        )
        self.plus_button = ttk.Button(
            self.parent,
            image=self.plus_sign_image,
            takefocus=False,
            style='ImageButton.TButton',
            command=lambda: self.controller.add_new_line(self.row),
        )
        self.minus_button = ttk.Button(
            self.parent,
            image=self.minus_sign_image,
            takefocus=False,
            style='ImageButton.TButton',
            command=lambda: self.controller.remove_line(self.row),
        )
        self.entry1 = ttk.Combobox(
            self.parent,
            textvariable=self.var_mat_selection,
            values=material_list,
            state='readonly',
            style='Standard.TCombobox',
        )
        self.entry1.bind('<<ComboboxSelected>>',
                         lambda event, x=self.row: self.controller.combobox_selection(event, self.row))
        self.entry2 = ttk.Spinbox(
            self.parent,
            from_=0.01,
            to=10,
            format="%.2f",
            increment=0.01,
            width=4,
            style='Standard.TSpinbox',
        )

        # Variables for material entries
        self.var_rhod = tk.StringVar()
        self.var_rhos = tk.StringVar()
        self.var_n = tk.StringVar()
        self.var_w_grav = tk.StringVar()
        self.var_sp_val = tk.StringVar()
        self.var_a_val = tk.StringVar()
        self.var_ku = tk.StringVar()
        self.var_kf = tk.StringVar()
        self.var_sr = tk.StringVar()
        self.var_lf = tk.StringVar()

        # Checkbox variable
        self.checked = tk.IntVar()
        self.checked.set(0)

        # Entry fields for material properties
        self.entry_rhod = ttk.Entry(
            self.parent,
            width=6,
            textvariable=self.var_rhod,
            state='disabled',
            style='Standard.TEntry',
        )
        self.entry_rhos = ttk.Entry(
            self.parent,
            width=6,
            textvariable=self.var_rhos,
            state='disabled',
            style='Standard.TEntry',
        )
        self.entry_n = ttk.Entry(
            self.parent,
            width=6,
            textvariable=self.var_n,
            state='disabled',
            style='Standard.TEntry',
        )
        self.entry_w_grav = ttk.Entry(
            self.parent,
            width=6,
            textvariable=self.var_w_grav,
            state='disabled',
            style='Standard.TEntry',
        )
        self.entry_sp_val = ttk.Entry(
            self.parent,
            width=6,
            textvariable=self.var_sp_val,
            state='disabled',
            style='Standard.TEntry',
        )
        self.entry_sp_opt_label = ttk.Frame(self.parent, style='Standard.TFrame')
        self.entry_sp_opt_button = ttk.Button(
            self.entry_sp_opt_label,
            image=self.opt_img_resized,
            state='disabled',
            takefocus=False,
            style='ImageButton.TButton',
            command=lambda: self.controller.segregation_potential_model(self.row),
        )
        self.entry_a_val = ttk.Entry(
            self.parent,
            width=6,
            textvariable=self.var_a_val,
            state='disabled',
            style='Standard.TEntry',
        )
        self.entry_ku = ttk.Entry(
            self.parent,
            width=6,
            textvariable=self.var_ku,
            state='disabled',
            style='Standard.TEntry',
        )
        self.entry_kf = ttk.Entry(
            self.parent,
            width=6,
            textvariable=self.var_kf,
            state='disabled',
            style='Standard.TEntry',
        )
        self.entry_th_opt_label = ttk.Frame(self.parent, style='Standard.TFrame')
        self.entry_th_opt_button = ttk.Button(
            self.entry_th_opt_label,
            image=self.opt_img_resized,
            state='disabled',
            takefocus=False,
            style='ImageButton.TButton',
            command=lambda: self.controller.kf_thermal_conductivty_model(self.row),
        )
        self.entry_sr = ttk.Entry(
            self.parent,
            width=6,
            textvariable=self.var_sr,
            state='disabled',
            style='DisabledEntry.TEntry',
        )
        self.entry_lf = ttk.Entry(
            self.parent,
            width=6,
            textvariable=self.var_lf,
            state='disabled',
            style='DisabledEntry.TEntry',
        )
        self.checkbox = ttk.Checkbutton(
            self.parent,
            variable=self.checked,
            style='Standard.TCheckbutton',
            command=lambda: self.controller.disable_entry_line(self.row))

        # Entry bindings
        self.entry_rhod.bind(
            '<KeyRelease>',
            lambda event, entry='rhod', row=self.row: self.controller.calculate_entry_changes(event, entry, self.row)
        )
        self.entry_rhos.bind(
            '<KeyRelease>',
            lambda event, entry='rhos', row=self.row: self.controller.calculate_entry_changes(event, entry, self.row)
        )
        self.entry_n.bind(
            '<KeyRelease>',
            lambda event, entry='n', row=self.row: self.controller.calculate_entry_changes(event, entry, self.row)
        )
        self.entry_w_grav.bind(
            '<KeyRelease>',
            lambda event, entry='w_grav', row=self.row: self.controller.calculate_entry_changes(event, entry, self.row)
        )
        self.entry_sr.bind(
            '<KeyRelease>',
            lambda event, entry='sr', row=self.row: self.controller.calculate_entry_changes(event, entry, self.row)
        )

    def pack_objects(self):
        """Packs all widgets for a given line"""
        # Packing material selection entries
        self.row_line_number.grid(row=self.row, column=0, padx=(5, 0), pady=(5, 0))
        self.plus_button.grid(row=self.row, column=1, padx=(10, 0), pady=(5, 0))
        self.minus_button.grid(row=self.row, column=2, padx=(5, 0), pady=(5, 0))
        self.entry1.grid(row=self.row, column=3, padx=(10, 0), pady=(5, 0))
        self.entry2.grid(row=self.row, column=4, padx=(10, 0), pady=(5, 0))

        # Packing material property entries
        self.entry_rhod.grid(row=self.row, column=5, padx=(30, 0), pady=(5, 0))
        self.entry_rhos.grid(row=self.row, column=6, padx=(7, 0), pady=(5, 0))
        self.entry_n.grid(row=self.row, column=7, padx=(7, 0), pady=(5, 0))
        self.entry_w_grav.grid(row=self.row, column=8, padx=(7, 0), pady=(5, 0))
        self.entry_sp_val.grid(row=self.row, column=9, padx=(7, 0), pady=(5, 0))
        self.entry_sp_opt_label.grid(row=self.row, column=10, sticky='nsew', pady=(5, 0))
        self.entry_sp_opt_button.pack(padx=(1, 2))
        self.entry_a_val.grid(row=self.row, column=11, padx=(7, 0), pady=(5, 0))
        self.entry_ku.grid(row=self.row, column=12, padx=(7, 0), pady=(5, 0))
        self.entry_kf.grid(row=self.row, column=13, padx=(7, 0), pady=(5, 0))
        self.entry_th_opt_label.grid(row=self.row, column=14, sticky='nsew', pady=(5, 0))
        self.entry_th_opt_button.pack(padx=(1, 2))
        self.entry_sr.grid(row=self.row, column=15, padx=(7, 0), pady=(5, 0))
        self.entry_lf.grid(row=self.row, column=16, padx=(7, 0), pady=(5, 0))

        self.checkbox.grid(row=self.row, column=17, padx=(7, 0), pady=(3, 0))

    def delete_object(self):
        """Deletes all objects in the selected line"""
        self.row_line_number.destroy()
        self.plus_button.destroy()
        self.minus_button.destroy()
        self.entry1.destroy()
        self.entry2.destroy()

        self.entry_rhod.destroy()
        self.entry_rhos.destroy()
        self.entry_n.destroy()
        self.entry_w_grav.destroy()
        self.entry_sp_val.destroy()
        self.entry_sp_opt_label.destroy()
        self.entry_sp_opt_button.destroy()
        self.entry_a_val.destroy()
        self.entry_ku.destroy()
        self.entry_kf.destroy()
        self.entry_th_opt_label.destroy()
        self.entry_th_opt_button.destroy()
        self.entry_sr.destroy()
        self.entry_lf.destroy()

        self.checkbox.destroy()

    def forget_objects(self):
        """Forgets all objects in the given line. This is used as a function before packing again"""
        self.row_line_number.grid_forget()
        self.plus_button.grid_forget()
        self.minus_button.grid_forget()
        self.entry1.grid_forget()
        self.entry2.grid_forget()

        self.entry_rhod.grid_forget()
        self.entry_rhos.grid_forget()
        self.entry_n.grid_forget()
        self.entry_w_grav.grid_forget()
        self.entry_sp_val.grid_forget()
        self.entry_sp_opt_label.grid_forget()
        self.entry_sp_opt_button.place_forget()
        self.entry_a_val.grid_forget()
        self.entry_ku.grid_forget()
        self.entry_kf.grid_forget()
        self.entry_th_opt_label.grid_forget()
        self.entry_th_opt_button.place_forget()
        self.entry_sr.grid_forget()
        self.entry_lf.grid_forget()

        self.checkbox.grid_forget()

        self.var_line_number.set(self.row)

