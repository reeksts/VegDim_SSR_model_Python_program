import tkinter as tk
from tkinter import ttk
from modules.thermal_conductivity_model.rock_thermal_conductivity_library import rock_class_list


class RockThermalConductivitySelection(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        #self.geometry("500x1000+300+400")
        self.title("Select rock type")
        self.resizable(False, False)
        self.controller = controller

        self.rock_class_container = []
        self.radiobutton_variable = tk.StringVar()
        self.name_retrieved = None
        self.rho_retrieved = None
        self.th_retrieved = None

        self.background_frame = ttk.Frame(self, style='Standard.TFrame')
        self.background_frame.pack(side='top', fill='both', expand=True)

        self.main_frame = ttk.Frame(self.background_frame, style='Standard.TFrame')
        self.main_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)

        # Adding top frame for column labels
        self.top_label_frame = ttk.Frame(self.main_frame, style='DarkFrame.TFrame')
        self.top_label_frame.pack(side='top', fill='x')

        # Adding center frame entry content
        self.center_frame = tk.Frame(self.main_frame)
        self.center_frame.pack(side='top', fill='both', expand=True)
        self.center_frame.columnconfigure(0, weight=1)
        self.center_frame.rowconfigure(0, weight=1)                # is this necessary??

        # Adding bottom frame with button
        self.button_label_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.button_label_frame.pack(side='top', fill='x')

        self.select_button = ttk.Button(self.button_label_frame,
                                        text='press',
                                        takefocus=False,
                                        style='Standard.TButton',
                                        command=self.select_material)
        self.select_button.pack(side='left', pady=(10, 0))

        # Top row label containers
        self.empty_container = ttk.Frame(self.top_label_frame, width=25, height=40, style='DarkFrame.TFrame')
        self.rock_name_container = ttk.Frame(self.top_label_frame, width=200, height=40, style='DarkFrame.TFrame')
        self.rock_rho_container = ttk.Frame(self.top_label_frame, width=100, height=40, style='DarkFrame.TFrame')
        self.rock_th_container = ttk.Frame(self.top_label_frame, width=100, height=40, style='DarkFrame.TFrame')

        # Packing top row label containers
        self.empty_container.pack(side='left', padx=(5, 0))
        self.rock_name_container.pack(side='left', padx=(5, 0))
        self.rock_rho_container.pack(side='left', padx=(5, 0))
        self.rock_th_container.pack(side='left', padx=(5, 0))

        self.rock_name_container.pack_propagate(0)
        self.rock_rho_container.pack_propagate(0)
        self.rock_th_container.pack_propagate(0)

        # Adding top row labels
        self.rock_name = ttk.Label(self.rock_name_container, text='Mineral', style='DarkLargeLabel.TLabel')
        self.rock_rho = ttk.Label(self.rock_rho_container, text='Rho', style='DarkLargeLabel.TLabel')
        self.rock_th = ttk.Label(self.rock_th_container, text='Th', style='DarkLargeLabel.TLabel')

        #Packing top row labels
        self.rock_name.pack(expand=True, fill='x')
        self.rock_rho.pack(expand=True, fill='x')
        self.rock_th.pack(expand=True, fill='x')

        self.display_all_materials()


    def display_all_materials(self):
        for class_name, class_content in rock_class_list:
            new_rock_class = NewRockClass(self.center_frame, class_name, class_content, self.radiobutton_variable, self)
            self.rock_class_container.append(new_rock_class)

    def retrieve_selected_rock(self, name, rho, th):
        self.name_retrieved = name.get().strip()
        self.rho_retrieved = rho.get()
        self.th_retrieved = th.get()

    def select_material(self):
        selected_entry = (self.name_retrieved, self.rho_retrieved, self.th_retrieved)
        self.controller.refresh_with_selected_entry(selected_entry)
        self.destroy()


class NewRockClass(ttk.Frame):
    def __init__(self, parent, class_name, class_content, variable, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller

        self.pack(fill='x')
        self['style'] = 'Standard.TFrame'
        self.class_entry_line_container = []
        self.columnconfigure(0, weight=1)

        # Adding class name label
        self.class_name_entry_line = ttk.Frame(self, style='Standard.TFrame')
        self.class_name_entry_line.grid(row=0, column=0, sticky='ew')
        self.class_name_entry_line.grid_propagate(0)

        self.empty_container = ttk.Frame(self.class_name_entry_line, width=25, height=40, style='Standard.TFrame')
        self.empty_container.pack(side='left', padx=(5, 0))

        self.class_name_label_container = ttk.Frame(self.class_name_entry_line, height=40, style='Standard.TFrame')
        self.class_name_label_container.pack(side='left', padx=(5, 0))

        self.class_name_label = ttk.Label(self.class_name_label_container,
                                          text=class_name,
                                          style='LeftAlignedLargeBold.TLabel')
        self.class_name_label.pack(expand=True)

        row_number = 1
        for rock in class_content:
            new_entry_line = NewRockClassEntryLine(self,
                                                   row_number,
                                                   rock[0],
                                                   rock[1],
                                                   rock[2],
                                                   variable)
            self.class_entry_line_container.append(new_entry_line)
            row_number += 1

    def testing(self):
        print('yoooooo')


class NewRockClassEntryLine(ttk.Frame):
    def __init__(self, parent, row, text1, text2, text3, variable):
        super().__init__(parent)
        self.parent = parent
        self.row = row
        self['style'] = 'Standard.TFrame'
        self.grid(row=self.row, column=0, sticky='ew')
        self.grid_propagate(0)

        # Adding containers
        self.radiobutton_container = ttk.Frame(self, width=25, height=30, style='Standard.TFrame')
        self.name_label_container = ttk.Frame(self, width=200, height=30, style='Standard.TFrame')
        self.rho_label_container = ttk.Frame(self, width=100, height=30, style='Standard.TFrame')
        self.th_label_container = ttk.Frame(self, width=100, height=30, style='Standard.TFrame')
        self.radiobutton_container.pack(side='left', padx=(5, 0))
        self.name_label_container.pack(side='left', padx=(5, 0))
        self.rho_label_container.pack(side='left', padx=(5, 0))
        self.th_label_container.pack(side='left', padx=(5, 0))
        self.radiobutton_container.pack_propagate(0)
        self.name_label_container.pack_propagate(0)
        self.rho_label_container.pack_propagate(0)
        self.th_label_container.pack_propagate(0)

        # Adding checkbox and labels
        self.var_name = tk.StringVar(value='     ' + text1)
        self.var_rho = tk.StringVar(value=text2)
        self.var_th = tk.StringVar(value=text3)

        self.radiobutton = ttk.Radiobutton(
            self.radiobutton_container,
            value=text1,
            variable=variable,
            takefocus=False,
            style='Standard.TRadiobutton',
            command=lambda: self.parent.controller.retrieve_selected_rock(self.var_name,
                                                                          self.var_rho,
                                                                          self.var_th))
        self.rho_label = ttk.Label(self.rho_label_container, textvariable=self.var_rho, style='Standard.TLabel')
        self.th_label = ttk.Label(self.th_label_container, textvariable=self.var_th, style='Standard.TLabel')

        self.radiobutton.pack(expand=True)
        self.rho_label.pack(expand=True, fill='x')
        self.th_label.pack(expand=True, fill='x')

        self.name_label = ttk.Label(self.name_label_container,
                                    textvariable=self.var_name,
                                    style='LeftAligned.TLabel')
        self.name_label.pack(expand=True, fill='x')
