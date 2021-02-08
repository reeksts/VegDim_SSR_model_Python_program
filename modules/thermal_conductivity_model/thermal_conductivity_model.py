import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from modules.thermal_conductivity_model.particle_thermal_conductivity_selection import ParticleThermalConductivitySelection
from modules.thermal_conductivity_model.rock_thermal_conductivity_selection import RockThermalConductivitySelection


class ThermalConductivityModel(tk.Toplevel):
    def __init__(self, row, controller):
        super().__init__()
        self.title("Thermal conductivity model")
        self.row = row
        self.controller = controller
        #self.resizable(False, False)

        # Adding outer container frames
        self.background_frame = ttk.Frame(self, style='Standard.TFrame')
        self.background_frame.pack(side='top', fill='both', expand=True)

        self.main_frame = ttk.Frame(self.background_frame, style='Standard.TFrame')
        self.main_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)

        # Adding main title frame
        self.main_title_frame = ttk.Frame(self.main_frame, style='DarkFrame.TFrame')
        self.main_title_frame.pack(side='top', fill='x')

        # Adding inner container frames
        self.top_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.top_frame.pack(side='top', fill='x')

        self.center_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.center_frame.pack(side='top', fill='x')

        self.bottom_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.bottom_frame.pack(side='top', fill='x')

        # Adding top part container frames
        self.top_frame_inner_left = ttk.Frame(self.top_frame, style='Standard.TFrame')
        self.top_frame_inner_left.pack(side='left', fill='both', expand=True)

        self.top_frame_inner_right = ttk.Frame(self.top_frame, style='Standard.TFrame')
        self.top_frame_inner_right.pack(side='left', fill='both', expand=True)

        # Adding bottom part container frames
        self.bottom_frame_inner_left = ttk.Frame(self.bottom_frame, style='Standard.TFrame')
        self.bottom_frame_inner_left.pack(side='left', fill='both', expand=True)

        self.bottom_frame_inner_center = ttk.Frame(self.bottom_frame, style='Standard.TFrame')
        self.bottom_frame_inner_center.pack(side='left', fill='both', expand=True)

        self.bottom_frame_inner_right = ttk.Frame(self.bottom_frame, style='Standard.TFrame')
        self.bottom_frame_inner_right.pack(side='left', fill='both', expand=True)

        # Adding buttons in the button part
        self.ok_button = ttk.Button(self.bottom_frame_inner_left,
                                    text='Ok',
                                    width=15,
                                    takefocus=False,
                                    style='Standard.TButton',
                                    command=self.ok_button_func)
        self.ok_button.pack(side='left', padx=(10, 0), pady=(10, 10))

        self.see_calc_button = ttk.Button(self.bottom_frame_inner_center,
                                          text='See calculation',
                                          width=15,
                                          takefocus=False,
                                          style='Standard.TButton',
                                          command=self.see_calc_button_func)
        self.see_calc_button.pack(side='top', padx=(0, 10), pady=(10, 10))

        self.cancel_button = ttk.Button(self.bottom_frame_inner_right,
                                          text='Cancel',
                                          width=15,
                                          takefocus=False,
                                          style='Standard.TButton',
                                          command=self.cancel_button)
        self.cancel_button.pack(side='right', padx=(0, 10), pady=(10, 10))

        # Adding main title
        self.main_title = ttk.Label(self.main_title_frame,
                                   text='Thermal conductivity model',
                                   style='ExtraLargeLabel.TLabel')
        self.main_title.pack(side='left', padx=(10, 10), pady=(10, 10))

        # ku or kf selection frame widgets
        self.calculate_label = ttk.Label(self.top_frame_inner_left, text='Calculate:', style='LargeLabel.TLabel')
        self.calculate_label.grid(row=0, column=0, columnspan=2, sticky='w', padx=(10, 0), pady=(0, 0))

        self.ku_checkbutton = ttk.Checkbutton(self.top_frame_inner_left,
                                              style='Standard.TCheckbutton')
        self.ku_checkbutton.grid(row=1, column=0, sticky='w', padx=(10, 0), pady=(5, 0))
        self.ku_checkbutton_label = ttk.Label(self.top_frame_inner_left,
                                              text='Calculate unfrozen thermal conductivity',
                                              style='Standard.TLabel')
        self.ku_checkbutton_label.grid(row=1, column=1, sticky='w', padx=(3, 0), pady=(5, 0))

        self.kf_checkbutton = ttk.Checkbutton(self.top_frame_inner_left,
                                              style='Standard.TCheckbutton')
        self.kf_checkbutton.grid(row=2, column=0, sticky='w', padx=(10, 0), pady=(5, 0))
        self.kf_checkbutton_label = ttk.Label(self.top_frame_inner_left,
                                              text='Calculate frozen thermal conductivity',
                                              style='Standard.TLabel')
        self.kf_checkbutton_label.grid(row=2, column=1, sticky='w', padx=(3, 0), pady=(5, 0))

        # Adding override options widgets
        self.override_label = ttk.Label(self.top_frame_inner_left, text='Override on output:', style='LargeLabel.TLabel')
        self.override_label.grid(row=3, column=0, columnspan=2, sticky='w', padx=(10, 0), pady=(20, 0))

        self.sr_override_checkbutton = ttk.Checkbutton(self.top_frame_inner_left,
                                                       style='Standard.TCheckbutton')
        self.sr_override_checkbutton.grid(row=4, column=0, sticky='w', padx=(10, 0), pady=(5, 0))
        self.sr_override_label = ttk.Label(self.top_frame_inner_left,
                                           text='Sr value',
                                           style='Standard.TLabel')
        self.sr_override_label.grid(row=4, column=1, sticky='w', padx=(3, 0), pady=(5, 0))

        # select material type frame widgets
        self.select_type_label = ttk.Label(self.top_frame_inner_right,
                                           text='Select material type',
                                           style='LargeLabel.TLabel')
        self.select_type_label.grid(row=0, column=0, columnspan=4, sticky='w', padx=(10, 0), pady=(0, 0))

        self.k_label = ttk.Label(self.top_frame_inner_right, text='k', style='Standard.TLabel')
        self.k_label.grid(row=1, column=2, columnspan=2, padx=(0, 0), pady=(3, 0))

        self.unfrozen_label = ttk.Label(self.top_frame_inner_right, text='unfrozen', style='Standard.TLabel')
        self.unfrozen_label.grid(row=2, column=2, padx=(5, 0), pady=(3, 0))
        self.frozen_label = ttk.Label(self.top_frame_inner_right, text='frozen', style='Standard.TLabel')
        self.frozen_label.grid(row=2, column=3, padx=(5, 0), pady=(3, 0))

        self.type_selection = tk.StringVar()
        self.radiobutton_1 = ttk.Radiobutton(self.top_frame_inner_right,
                                             value='type1',
                                             variable=self.type_selection,
                                             takefocus=False,
                                             style='Standard.TRadiobutton')
        self.radiobutton_1.grid(row=3, column=0, sticky='w', padx=(10, 0), pady=(3, 0))
        self.radiobutton_2 = ttk.Radiobutton(self.top_frame_inner_right,
                                             value='type2',
                                             variable=self.type_selection,
                                             takefocus=False,
                                             style='Standard.TRadiobutton')
        self.radiobutton_2.grid(row=4, column=0, sticky='w', padx=(10, 0), pady=(3, 0))
        self.radiobutton_3 = ttk.Radiobutton(self.top_frame_inner_right,
                                             value='type3',
                                             variable=self.type_selection,
                                             takefocus=False,
                                             style='Standard.TRadiobutton')
        self.radiobutton_3.grid(row=5, column=0, sticky='w', padx=(10, 0), pady=(3, 0))
        self.radiobutton_4 = ttk.Radiobutton(self.top_frame_inner_right,
                                             value='type4',
                                             variable=self.type_selection,
                                             takefocus=False,
                                             style='Standard.TRadiobutton')
        self.radiobutton_4.grid(row=6, column=0, sticky='w', padx=(10, 0), pady=(3, 0))

        self.type_label_1 = ttk.Label(self.top_frame_inner_right,
                                      text='gravel and coarse sands:',
                                      style='Standard.TLabel')
        self.type_label_1.grid(row=3, column=1, sticky='w', padx=(5, 0), pady=(3, 0))
        self.type_label_2 = ttk.Label(self.top_frame_inner_right,
                                      text='medium and fine sands:',
                                      style='Standard.TLabel')
        self.type_label_2.grid(row=4, column=1, sticky='w', padx=(5, 0), pady=(3, 0))
        self.type_label_3 = ttk.Label(self.top_frame_inner_right,
                                      text='silty and clayey soils:',
                                      style='Standard.TLabel')
        self.type_label_3.grid(row=5, column=1, sticky='w', padx=(5, 0), pady=(3, 0))
        self.type_label_4 = ttk.Label(self.top_frame_inner_right,
                                      text='organic fibrous soils (peat):',
                                      style='Standard.TLabel')
        self.type_label_4.grid(row=6, column=1, sticky='w', padx=(5, 0), pady=(3, 0))

        self.var_unfrozen_1 = tk.StringVar(value='4.60')
        self.var_unfrozen_2 = tk.StringVar(value='3.55')
        self.var_unfrozen_3 = tk.StringVar(value='1.90')
        self.var_unfrozen_4 = tk.StringVar(value='0.60')
        self.unfrozen_val_1 = ttk.Label(self.top_frame_inner_right,
                                        textvariable=self.var_unfrozen_1,
                                        style='Standard.TLabel')
        self.unfrozen_val_1.grid(row=3, column=2, padx=(0, 0), pady=(3, 0))
        self.unfrozen_val_2 = ttk.Label(self.top_frame_inner_right,
                                        textvariable=self.var_unfrozen_2,
                                        style='Standard.TLabel')
        self.unfrozen_val_2.grid(row=4, column=2, padx=(0, 0), pady=(3, 0))
        self.unfrozen_val_3 = ttk.Label(self.top_frame_inner_right,
                                        textvariable=self.var_unfrozen_3,
                                        style='Standard.TLabel')
        self.unfrozen_val_3.grid(row=5, column=2, padx=(0, 0), pady=(3, 0))
        self.unfrozen_val_4 = ttk.Label(self.top_frame_inner_right,
                                        textvariable=self.var_unfrozen_4,
                                        style='Standard.TLabel')
        self.unfrozen_val_4.grid(row=6, column=2, padx=(0, 0), pady=(3, 0))

        self.var_frozen_1 = tk.StringVar(value='1.70')
        self.var_frozen_2 = tk.StringVar(value='0.95')
        self.var_frozen_3 = tk.StringVar(value='0.85')
        self.var_frozen_4 = tk.StringVar(value='0.25')
        self.frozen_val_1 = ttk.Label(self.top_frame_inner_right,
                                      textvariable=self.var_frozen_1,
                                      style='Standard.TLabel')
        self.frozen_val_1.grid(row=3, column=3, padx=(0, 0), pady=(3, 0))
        self.frozen_val_2 = ttk.Label(self.top_frame_inner_right,
                                      textvariable=self.var_frozen_2,
                                      style='Standard.TLabel')
        self.frozen_val_2.grid(row=4, column=3, padx=(0, 0),pady=(3, 0))
        self.frozen_val_3 = ttk.Label(self.top_frame_inner_right,
                                      textvariable=self.var_frozen_3,
                                      style='Standard.TLabel')
        self.frozen_val_3.grid(row=5, column=3, padx=(0, 0), pady=(3, 0))
        self.frozen_val_4 = ttk.Label(self.top_frame_inner_right,
                                      textvariable=self.var_frozen_4,
                                      style='Standard.TLabel')
        self.frozen_val_4.grid(row=6, column=3, padx=(0, 0), pady=(3, 0))

        # Adding center frame widgets for mineral or rock selection calculation
        self.center_frame_top_selection_frame = ttk.Frame(self.center_frame, style='Standard.TFrame')
        self.center_frame_top_selection_frame.pack(side='top', fill='x')

        self.particle_th_con_label = ttk.Label(self.center_frame_top_selection_frame,
                                              text='Particle thermal conductivity',
                                              style='LargeLabel.TLabel')
        self.particle_th_con_label.grid(row=0, column=0, columnspan=4, sticky='w', padx=(10, 0), pady=(15, 0))

        self.calculation_selection = tk.StringVar()
        self.rock_selection_radiobutton = ttk.Radiobutton(self.center_frame_top_selection_frame,
                                                          value='rock',
                                                          variable=self.calculation_selection,
                                                          style='Standard.TRadiobutton',
                                                          takefocus=False,
                                                          command=self.switch_frames)
        self.rock_selection_radiobutton.grid(row=1, column=0, padx=(10, 0), pady=(5, 5))
        self.rock_selection_label = ttk.Label(self.center_frame_top_selection_frame,
                                              text='by rock type',
                                              style='Standard.TLabel')
        self.rock_selection_label.grid(row=1, column=1, padx=(3, 0), pady=(5, 5))

        self.mineral_selection_radiobutton = ttk.Radiobutton(self.center_frame_top_selection_frame,
                                                             value='mineral',
                                                             variable=self.calculation_selection,
                                                             style='Standard.TRadiobutton',
                                                             takefocus=False,
                                                             command=self.switch_frames)
        self.mineral_selection_radiobutton.grid(row=1, column=2, padx=(10, 0), pady=(5, 5))
        self.mineral_selection_label = ttk.Label(self.center_frame_top_selection_frame,
                                                 text='by mineral',
                                                 style='Standard.TLabel')
        self.mineral_selection_label.grid(row=1, column=3, padx=(3, 0), pady=(5, 5))

        self.switch_frame_container = ttk.Frame(self.center_frame, style='Standard.TFrame')
        self.switch_frame_container.pack(side='bottom', fill='both', expand=True)
        self.switch_frame_container.columnconfigure(0, weight=1)
        self.switch_frame_container.rowconfigure(0, weight=1)

        # Frame switching
        self.frame_pages = dict()

        for frame_class in [SelectByRock, SelectByMineral]:
            selection_frame = frame_class(self.switch_frame_container)
            self.frame_pages[frame_class] = selection_frame
            selection_frame.grid(row=0, column=0, sticky='nsew')

        self.empty_start_frame = ttk.Frame(self.switch_frame_container, style='Standard.TFrame')
        self.empty_start_frame.grid(row=0, column=0, sticky='nsew')

    def ok_button_func(self):
        self.calculate_th()

    def see_calc_button_func(self):
        pass

    def cancel_button(self):
        self.destroy()

    def switch_frames(self):
        if self.calculation_selection.get() == 'rock':
            frame = self.frame_pages[SelectByRock]
            frame.tkraise()
        if self.calculation_selection.get() == 'mineral':
            frame = self.frame_pages[SelectByMineral]
            frame.tkraise()

    def calculate_geometric_mean_th_con(self):
        """The function calculate thermal conductivity for solid particles as the geometric mean of selected
        minerals and their percentages. This function is used when option of 'by mineral' is used"""
        thermal_conductivities = []
        percentages = []
        for mineral in self.frame_pages[SelectByMineral].entry_line_container:
            thermal_conductivities.append(float(mineral.var_th.get()))
            percentages.append(float(mineral.var_percentage.get()))

        ks = 1
        for th, perc in zip(thermal_conductivities, percentages):
            ks *= th**perc

        return ks

    def calculate_mean_density(self):
        desnsities = []
        percentages = []
        for mineral in self.frame_pages[SelectByMineral].entry_line_container:
            desnsities.append(float(mineral.var_rho.get()))
            percentages.append(float(mineral.var_percentage.get()))

        rhos = 1
        for rho, perc in zip(desnsities, percentages):
            rhos *= rho*perc

        return rhos

    def calculate_th(self):
        # Get selected calculation - both or only ku or only kf
            # Probably set flags for each those options?
            # And then if both are false raise a message that none was seleceted
        ks, rhos, kappa_unfrozen, kappa_frozen = (None, None, None, None)
        kair = 0.024
        kwater = 0.60
        kice = 2.24

        # STEP 21 - set ks values
        if self.calculation_selection.get() == 'rock':
            ks = 2.69
            #ks = float(self.frame_pages[SelectByMineral].var_th.get())

        elif self.calculation_selection.get() == 'mineral':
            ks = 2.69
            #ks = self.calculate_geometric_mean_th_con()

        # STEP 2 - set rhos values
        if self.calculation_selection.get() == 'rock':
            rhos = 2.69
            #rhos = float(self.frame_pages[SelectByMineral].var_rho.get())

        elif self.calculation_selection.get() == 'mineral':
            rhos = 2.69
            #rhos = self.calculate_mean_density()

        # STEP 3 - set kappa values
        if self.type_selection.get() == 'type1':
            kappa_unfrozen = float(self.var_unfrozen_1.get())
            kappa_frozen = float(self.var_frozen_1.get())
        elif self.type_selection.get() == 'type1':
            kappa_unfrozen = float(self.var_unfrozen_2.get())
            kappa_frozen = float(self.var_frozen_2.get())
        elif self.type_selection.get() == 'type1':
            kappa_unfrozen = float(self.var_unfrozen_3.get())
            kappa_frozen = float(self.var_frozen_3.get())
        elif self.type_selection.get() == 'type1':
            kappa_unfrozen = float(self.var_unfrozen_4.get())
            kappa_frozen = float(self.var_frozen_4.get())
        print(f'kappa_unfrozen is {kappa_unfrozen}')
        print(f'kappa_frozen is {kappa_frozen}')

        # STEP 4 - Get other parameters that were entered by the user
        entry_line = self.controller.entry_container[self.row - 1]
        rhod_entered = float(entry_line.var_rho.get())
        sr_entered = float(entry_line.var_sr.get())
        print(f'rhod_entered is {rhod_entered}')
        print(f'sr_entered is {sr_entered}')


        # STEP 5 - Calculate porosity
        porosity = 0.29
        #porosity = 1 - rhod_entered/rhos
        print(f'porosity is {porosity}')

        # STEP 6 - Calculate kdry value
        kdry = 0.51

        #kdry = ks**((1 - porosity)**0.59) * kair**(porosity**0.73)
        print(f'kdry is {kdry}')

        # STEP 7 - calculate ksat values
        ksat_u = ks**(1 - porosity)*kwater**porosity
        ksat_f = ks**(1 - porosity)*kice**porosity
        print(f'ksat_u is {ksat_u}')
        print(f'ksat_f is {ksat_f}')

        # STEP8 - calculate kr
        kr_u = (kappa_unfrozen * sr_entered) / (1 + (kappa_unfrozen - 1) * sr_entered)
        kr_f = (kappa_frozen * sr_entered) / (1 + (kappa_frozen - 1) * sr_entered)
        print(f'kr_u is {kr_u}')
        print(f'kr_f is {kr_f}')

        # STEP 9 - calculate ku and kf
        ku = (ksat_u - kdry) * kr_u + kdry
        kf = (ksat_f - kdry) * kr_f + kdry
        print(f'ku is {ku}')
        print(f'kf is {kf}')


        # overwrite changes - both or only one depending on what the user has entered


class SelectByRock(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['style'] = 'Standard.TFrame'
        self.parent = parent

        # Adding and packing top row labels
        self.name_label = ttk.Label(self, text='Mineral', style='Standard.TLabel')
        self.name_label.grid(row=0, column=0, padx=(10, 0), pady=(5, 0))
        self.rho_label = ttk.Label(self, text='rho', style='Standard.TLabel')
        self.rho_label.grid(row=0, column=1, padx=(0, 0), pady=(5, 0))
        self.th_label = ttk.Label(self, text='th', style='Standard.TLabel')
        self.th_label.grid(row=0, column=2, padx=(0, 0), pady=(5, 0))

        self.var_name = tk.StringVar(value='Custom')
        self.var_rho = tk.StringVar()
        self.var_th = tk.StringVar()
        self.name_label_entry = ttk.Label(self, textvariable=self.var_name, style='Standard.TLabel')
        self.name_label_entry.grid(row=1, column=0, padx=(10, 0), pady=(5, 0))
        self.rho_label_entry = ttk.Entry(self, textvariable=self.var_rho, style='Standard.TEntry')
        self.rho_label_entry.grid(row=1, column=1, padx=(10, 0), pady=(5, 0))
        self.th_label_entry = ttk.Entry(self, textvariable=self.var_th, style='Standard.TEntry')
        self.th_label_entry.grid(row=1, column=2, padx=(10, 0), pady=(5, 0))

        self.select_from_list = ttk.Button(self,
                                           text='Select from list',
                                           width=15,
                                           takefocus=False,
                                           style='Standard.TButton',
                                           command=self.select_rock)
        self.select_from_list.grid(row=2,
                                   column=0,
                                   columnspan=2,
                                   sticky='w',
                                   padx=(10, 0),
                                   pady=(10, 10))

    def select_rock(self):
        select_rock = RockThermalConductivitySelection(self)

    def refresh_with_selected_entry(self, selected_entry):
        """The function updates the rock entry by the one that was selected by the user. It updates name and adds
        corresponding rho and th values to entry fields"""
        self.var_name.set(selected_entry[0])
        self.var_rho.set(selected_entry[1])
        self.var_th.set(selected_entry[2])


class SelectByMineral(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['style'] = 'Standard.TFrame'
        self.entry_line_container = []

        # Adding and packing top row labels
        self.name_label = ttk.Label(self, text='Mineral', style='Standard.TLabel')
        self.name_label.grid(row=0, column=3, padx=(10, 0), pady=(5, 0))
        self.rho_label = ttk.Label(self, text='rho', style='Standard.TLabel')
        self.rho_label.grid(row=0, column=4, padx=(0, 0), pady=(5, 0))
        self.th_label = ttk.Label(self, text='th', style='Standard.TLabel')
        self.th_label.grid(row=0, column=5, padx=(0, 0), pady=(5, 0))
        self.th_label = ttk.Label(self, text='%', style='Standard.TLabel')
        self.th_label.grid(row=0, column=6, padx=(0, 0), pady=(5, 0))

        # Add initial entry lines
        for i in range(1, 5):
            new_line = SelectByMineralEntryLine(self, i, name='Custom')
            new_line.pack_objects()
            self.entry_line_container.append(new_line)

        # Adding select minerals button
        self.var_row_number = tk.IntVar(value=len(self.entry_line_container)+1)
        self.select_from_list = ttk.Button(self,
                                           text='Select from list',
                                           width=15,
                                           takefocus=False,
                                           style='Standard.TButton',
                                           command=self.select_minerals)
        self.select_from_list.grid(row=self.var_row_number.get(),
                                   column=0,
                                   columnspan=5,
                                   sticky='w',
                                   padx=(10, 0),
                                   pady=(10, 10))

        # Adding sum percentage label
        self.var_sum_percentage = tk.StringVar(value='sum: 0.0')
        self.sum_percentage_label = ttk.Label(self, textvariable=self.var_sum_percentage, style='Standard.TLabel')
        self.sum_percentage_label.grid(row=self.var_row_number.get(), column=6, padx=(0, 0), pady=(10, 10))


    def repack_button_and_label(self):
        """Repacks button and label at the button of the entry lines. This function is used when lines are
        added or removed."""
        self.var_row_number.set(len(self.entry_line_container) + 1)
        self.select_from_list.grid_forget()
        self.select_from_list.grid(row=self.var_row_number.get(),
                                   column=0,
                                   columnspan=5,
                                   sticky='w',
                                   padx=(10, 0),
                                   pady=(10, 10))
        self.sum_percentage_label.grid_forget()
        self.sum_percentage_label.grid(row=self.var_row_number.get(), column=6, padx=(0, 0), pady=(10, 10))

    def enable_disable_plus_minus_buttons(self):
        pass

    def add_new_line(self, row):
        new_line = SelectByMineralEntryLine(self, row, name='Custom')
        new_line.pack_objects()
        self.entry_line_container.insert(row - 1, new_line)

        for i in self.entry_line_container[row:]:
            i.row += 1
            i.forget_objects()
            i.pack_objects()

        if len(self.entry_line_container) > 1:
            for i in self.entry_line_container:
                i.minus_button["state"] = "normal"
        if len(self.entry_line_container) > 9:
            for i in self.entry_line_container:
                i.plus_button["state"] = "disabled"
        self.repack_button_and_label()

    def remove_line(self, row):
        if row == len(self.entry_line_container):
            self.entry_line_container[row-1].destroy_objects()
            del self.entry_line_container[row-1]
            for entry_line in self.entry_line_container:
                entry_line.forget_objects()
                entry_line.pack_objects()
        else:
            self.entry_line_container[row-1].destroy_objects()
            del self.entry_line_container[row-1]

            for entry_line in self.entry_line_container[row-1:]:
                entry_line.row -= 1

            for entry_line in self.entry_line_container:
                entry_line.forget_objects()
                entry_line.pack_objects()
                entry_line.row_line_number["text"] = str(entry_line.row) + "."

        if len(self.entry_line_container) == 1:
            self.entry_line_container[0].minus_button["state"] = "disabled"
        if len(self.entry_line_container) < 10:
            for i in self.entry_line_container:
                i.plus_button["state"] = "normal"
        self.repack_button_and_label()

    def select_minerals(self):
        """Opens a new window of selectable mineral materials. The user can select minerals form the given list.
        These minerals are than added to the mineral material selection list"""
        ParticleThermalConductivitySelection(self)

    def refresh_with_selected_entries(self, selected_entries):
        """The function deletes all the mineral entry lines and replaces them by the selected minerals from the
        mineral library. If no mineral was selected, no action takes place"""
        for line in self.entry_line_container:
            line.destroy_objects()
        self.entry_line_container.clear()
        row = 1
        for new_entry in selected_entries:
            new_line = SelectByMineralEntryLine(self, row, name=new_entry[0], rho=new_entry[1], th=new_entry[2])
            new_line.pack_objects()
            self.entry_line_container.append(new_line)
            row += 1
        self.repack_button_and_label()


class SelectByMineralEntryLine:
    """
    This class allows to add new mineral entry line.
    These lines can be packed, destroyed and forgot - all this functionality allows to dynamically
    update the 'by mineral' window when user adds or removes lines, or selects minerals from the
    mineral list
    """
    def __init__(self, parent, row, name=None, rho=None, th=None):
        """ Initializer simply creates all the widgets. Packing of these widgets is done separately with
        the pack_objects method. This is done so for reusability purposes"""
        self.parent = parent
        self.row = row
        self.name = name
        self.rho = rho
        self.th = th

        self.plus_sign_image = tk.PhotoImage(file='modules/icons/sq_plus_icon&16_inverted.png')
        self.minus_sign_image = tk.PhotoImage(file='modules/icons/sq_minus_icon&16_inverted.png')

        # Adding entry line widgets
        self.row_line_number = ttk.Label(self.parent, width=2, text=str(self.row) + ".", style='Standard.TLabel')
        self.plus_button = ttk.Button(self.parent,
                                      image=self.plus_sign_image,
                                      style='ImageButton.TButton',
                                      takefocus=False,
                                      command=lambda: self.parent.add_new_line(self.row))
        self.minus_button = ttk.Button(self.parent,
                                       image=self.minus_sign_image,
                                       style='ImageButton.TButton',
                                       takefocus=False,
                                       command=lambda: self.parent.remove_line(self.row))
        self.var_name = tk.StringVar(value=self.name)
        self.name_label = ttk.Label(self.parent, textvariable=self.var_name, style='Standard.TLabel')

        self.var_rho = tk.StringVar(value=self.rho)
        self.rho_entry = ttk.Entry(self.parent, textvariable=self.var_rho, style='Standard.TEntry')

        self.var_th = tk.StringVar(value=self.th)
        self.th_entry = ttk.Entry(self.parent, textvariable=self.var_th, style='Standard.TEntry')

        self.var_percentage = tk.StringVar()
        self.percentage_entry = ttk.Entry(self.parent, textvariable=self.var_percentage, style='Standard.TEntry')

    def pack_objects(self):
        """ This function simply packs all the widgets defined in this class"""
        self.row_line_number.grid(row=self.row, column=0, padx=(10, 0), pady=(5, 0))
        self.plus_button.grid(row=self.row, column=1, padx=(10, 0), pady=(5, 0))
        self.minus_button.grid(row=self.row, column=2, padx=(5, 0), pady=(5, 0))
        self.name_label.grid(row=self.row, column=3, padx=(10, 0), pady=(5, 0))
        self.rho_entry.grid(row=self.row, column=4,padx=(10, 0), pady=(5, 0))
        self.th_entry.grid(row=self.row, column=5,padx=(10, 0), pady=(5, 0))
        self.percentage_entry.grid(row=self.row, column=6,padx=(10, 10), pady=(5, 0))

    def forget_objects(self):
        """ The function allows to forget all the widgets defined in this class, so they could be packed
        again in new places"""
        self.row_line_number.grid_forget()
        self.plus_button.grid_forget()
        self.minus_button.grid_forget()
        self.name_label.grid_forget()
        self.rho_entry.grid_forget()
        self.th_entry.grid_forget()
        self.percentage_entry.grid_forget()

    def destroy_objects(self):
        """ This function destroys all the widgets defined in this class. Thi sis done when user clicks on the
        delete line button. I think that explicitly destroying these widgets is better approach than simply forgetting
        them. Otherwise the memory would be crammed with unnecessary widgets that are not used any more."""
        self.row_line_number.destroy()
        self.plus_button.destroy()
        self.minus_button.destroy()
        self.name_label.destroy()
        self.rho_entry.destroy()
        self.th_entry.destroy()
        self.percentage_entry.destroy()


class ThermalConductivityCalculation():
    def __init__(self, w_grav, porosity):
        self.rhos_and_ks_vals = {"anorthoside": [2.73, 1.8],
                                 "basalt": [2.90, 1.7],
                                 "diabase": [2.98, 2.3],
                                 "dolostone": [2.90, 3.8],
                                 "gabbro" : [3.03, 2.2],        #2.92
                                 "gneiss": [2.75, 2.6],
                                 "granite": [2.75, 2.5],
                                 "limestone": [2.70, 2.5],
                                 "marble": [2.80, 3.2],
                                 "quartzite": [2.631, 5.5],       #2.6, 5.0
                                 "sandstone": [2.80, 3.0],
                                 "schist": [2.65, 1.5],
                                 "shale": [2.65, 2.0],
                                 "syenite": [2.80, 2.0],
                                 "trap_rock": [2.90, 2.0],
                                 "coal": [1.35, 0.26],
                                 "peat": [1.50, 0.25],
                                 "silt_and_clay": [2.75, 2.90]}
        self.w_grav = w_grav
        self.porosity = porosity

        self.k_water = 0.6
        self.k_ice = 2.24
        self.k_air = 0.024
        self.rhow = 1

        self.rock_type = ""
        self.k_rock = 0
        self.rhos_rock = 0
        self.rhod = 0
        self.Sr = 0
        self.k_dry = 0
        self.k_sat_u = 0
        self.k_sat_f = 0
        self.kr_u = 0
        self.kr_f = 0
        self.k_unfrozen = 0
        self.k_frozen = 0

    def choose_stone_type(self):
        self.rock_type = input("Choose rock type from the list: gabbro, quartzite: ")
        self.k_rock = self.rhos_and_ks_vals[self.rock_type][1]
        self.rhos_rock = self.rhos_and_ks_vals[self.rock_type][0]

    def calc_rhod(self):
        self.rhod = self.rhos_rock * (1-self.porosity)

    def calc_Sr(self):
        self.Sr = (self.w_grav*self.rhod)/(100*self.porosity*self.rhow)

    def calc_k_dry(self):
        self.k_dry = self.k_rock**((1-self.porosity)**0.59)*self.k_air**(self.porosity**0.73)

    def calc_k_sat(self):
        self.k_sat_u = self.k_rock**(1-self.porosity)*self.k_water**self.porosity
        self.k_sat_f = self.k_rock**(1-self.porosity)*self.k_ice**self.porosity

    def calc_kr(self):
        self.kr_u = (4.7*self.Sr)/(1+3.7*self.Sr)
        self.kr_f = (1.8*self.Sr)/(1+0.8*self.Sr)

    def calculate_thermal_conductivity(self):
        self.k_unfrozen = (self.k_sat_u - self.k_dry)*self.kr_u + self.k_dry
        self.k_frozen = (self.k_sat_f - self.k_dry) * self.kr_f + self.k_dry
