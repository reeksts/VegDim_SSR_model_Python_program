import tkinter as tk
from tkinter import ttk
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from modules.climate_region_info import temp_zones
import math


class ClimateModelSpecial(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self['style'] = 'Standard.TFrame'

        # ##########  FRAME LAYOUT  ##########
        # Adding top label frame and label
        self.top_label_frame = ttk.Frame(self, style='DarkFrame.TFrame')
        self.top_label_frame.pack(side='top', fill='x')

        # Adding main top entry frame
        self.main_entry_frame_top_part = ttk.Frame(self, style='Standard.TFrame')
        self.main_entry_frame_top_part.pack(side='top', fill='x')

        # Adding main bottom entry frame
        self.main_entry_frame_bottom_part = ttk.Frame(self, style='Standard.TFrame')
        self.main_entry_frame_bottom_part.pack(side='top', fill='x')

        # Adding bottom frame for buttons
        self.bottom_button_frame = ttk.Frame(self, style='Standard.TFrame')
        self.bottom_button_frame.pack(side='top', fill='x')
        self.bottom_button_frame.columnconfigure(0, weight=1)
        self.bottom_button_frame.columnconfigure(1, weight=1)

        # ##########  CONTENT  ##########
        # Adding man title label
        self.main_title = ttk.Label(self.top_label_frame,
                                    text='Climate model (general)',
                                    style='ExtraLargeLabel.TLabel')
        self.main_title.pack(side='left', padx=(10, 0), pady=(5, 5))

        # Adding main top entry widgets
        self.mean_annual_temp_label = ttk.Label(self.main_entry_frame_top_part,
                                                text='Mean annual temperature',
                                                style='Standard.TLabel')
        self.mean_annual_temp_label.grid(row=0, column=0, sticky='w', padx=(10, 0), pady=(5, 0))

        self.var_mean_annual = tk.StringVar()
        self.mean_annual_temp_entry = ttk.Entry(self.main_entry_frame_top_part,
                                                textvariable=self.var_mean_annual,
                                                style='Standard.TEntry')
        self.mean_annual_temp_entry.grid(row=0, column=1, padx=(10, 0), pady=(5, 0))
        self.mean_annual_temp_units = ttk.Label(self.main_entry_frame_top_part,
                                                text='degC',
                                                style='Standard.TLabel')
        self.mean_annual_temp_units.grid(row=0, column=2, sticky='w', padx=(5, 0), pady=(5, 0))

        self.frost_index_label = ttk.Label(self.main_entry_frame_top_part,
                                           text='Frost index',
                                           style='Standard.TLabel')
        self.frost_index_label.grid(row=1, column=0, sticky='w', padx=(10, 0), pady=(5, 0))

        self.var_frost_index = tk.StringVar()
        self.frost_index_entry = ttk.Entry(self.main_entry_frame_top_part,
                                           textvariable=self.var_frost_index,
                                           style='Standard.TEntry')
        self.frost_index_entry.grid(row=1, column=1, padx=(10, 0), pady=(5, 0))
        self.frost_index_units = ttk.Label(self.main_entry_frame_top_part,
                                           text='degC hours',
                                           style='Standard.TLabel')
        self.frost_index_units.grid(row=1, column=2, sticky='w', padx=(5, 0), pady=(5, 0))

        # Adding main bottom entry widgets
        self.select_region_label = ttk.Label(self.main_entry_frame_bottom_part,
                                             text='Select region:',
                                             style='Standard.TLabel')
        self.select_region_label.grid(row=0, column=0, columnspan=2, sticky='w', padx=(10, 10), pady=(5, 5))
        self.see_map_button = ttk.Button(self.main_entry_frame_bottom_part,
                                         text='see map',
                                         takefocus=False,
                                         style='Standard.TButton')
        self.see_map_button.grid(row=0, column=2, columnspan=2, padx=(10, 10), pady=(5, 5))

        self.var_region = tk.StringVar()
        self.radiobutton1 = ttk.Radiobutton(self.main_entry_frame_bottom_part,
                                            variable=self.var_region,
                                            value='reg1',
                                            takefocus=False,
                                            style='Standard.TRadiobutton')
        self.radiobutton2 = ttk.Radiobutton(self.main_entry_frame_bottom_part,
                                            variable=self.var_region,
                                            value='reg2',
                                            takefocus=False,
                                            style='Standard.TRadiobutton')
        self.radiobutton3 = ttk.Radiobutton(self.main_entry_frame_bottom_part,
                                            variable=self.var_region,
                                            value='reg3',
                                            takefocus=False,
                                            style='Standard.TRadiobutton')
        self.radiobutton4 = ttk.Radiobutton(self.main_entry_frame_bottom_part,
                                            variable=self.var_region,
                                            value='reg4',
                                            takefocus=False,
                                            style='Standard.TRadiobutton')
        self.radiobutton5 = ttk.Radiobutton(self.main_entry_frame_bottom_part,
                                            variable=self.var_region,
                                            value='reg5',
                                            takefocus=False,
                                            style='Standard.TRadiobutton')
        self.radiobutton6 = ttk.Radiobutton(self.main_entry_frame_bottom_part,
                                            variable=self.var_region,
                                            value='reg6',
                                            takefocus=False,
                                            style='Standard.TRadiobutton')
        self.radiobutton7 = ttk.Radiobutton(self.main_entry_frame_bottom_part,
                                            variable=self.var_region,
                                            value='reg7',
                                            takefocus=False,
                                            style='Standard.TRadiobutton')
        self.radiobutton8 = ttk.Radiobutton(self.main_entry_frame_bottom_part,
                                            variable=self.var_region,
                                            value='reg8',
                                            takefocus=False,
                                            style='Standard.TRadiobutton')
        self.radiobutton9 = ttk.Radiobutton(self.main_entry_frame_bottom_part,
                                            variable=self.var_region,
                                            value='reg9',
                                            takefocus=False,
                                            style='Standard.TRadiobutton')
        self.radiobutton10 = ttk.Radiobutton(self.main_entry_frame_bottom_part,
                                             variable=self.var_region,
                                             value='reg10',
                                             takefocus=False,
                                             style='Standard.TRadiobutton')
        self.radiobutton11 = ttk.Radiobutton(self.main_entry_frame_bottom_part,
                                             variable=self.var_region,
                                             value='reg11',
                                             takefocus=False,
                                             style='Standard.TRadiobutton')

        self.radiobutton1.grid(row=1, column=0, padx=(10, 0), pady=(5, 0))
        self.radiobutton2.grid(row=2, column=0, padx=(10, 0), pady=(5, 0))
        self.radiobutton3.grid(row=3, column=0, padx=(10, 0), pady=(5, 0))
        self.radiobutton4.grid(row=4, column=0, padx=(10, 0), pady=(5, 0))
        self.radiobutton5.grid(row=1, column=2, padx=(10, 0), pady=(5, 0))
        self.radiobutton6.grid(row=2, column=2, padx=(10, 0), pady=(5, 0))
        self.radiobutton7.grid(row=3, column=2, padx=(10, 0), pady=(5, 0))
        self.radiobutton8.grid(row=4, column=2, padx=(10, 0), pady=(5, 0))
        self.radiobutton9.grid(row=1, column=4, padx=(10, 0), pady=(5, 0))
        self.radiobutton10.grid(row=2, column=4, padx=(10, 0), pady=(5, 0))
        self.radiobutton11.grid(row=3, column=4, padx=(10, 0), pady=(5, 0))

        self.reg1_label = ttk.Label(self.main_entry_frame_bottom_part, text='region 1', style='Standard.TLabel')
        self.reg2_label = ttk.Label(self.main_entry_frame_bottom_part, text='region 2', style='Standard.TLabel')
        self.reg3_label = ttk.Label(self.main_entry_frame_bottom_part, text='region 3', style='Standard.TLabel')
        self.reg4_label = ttk.Label(self.main_entry_frame_bottom_part, text='region 4', style='Standard.TLabel')
        self.reg5_label = ttk.Label(self.main_entry_frame_bottom_part, text='region 5', style='Standard.TLabel')
        self.reg6_label = ttk.Label(self.main_entry_frame_bottom_part, text='region 6', style='Standard.TLabel')
        self.reg7_label = ttk.Label(self.main_entry_frame_bottom_part, text='region 7', style='Standard.TLabel')
        self.reg8_label = ttk.Label(self.main_entry_frame_bottom_part, text='region 8', style='Standard.TLabel')
        self.reg9_label = ttk.Label(self.main_entry_frame_bottom_part, text='region 9', style='Standard.TLabel')
        self.reg10_label = ttk.Label(self.main_entry_frame_bottom_part, text='region 10', style='Standard.TLabel')
        self.reg11_label = ttk.Label(self.main_entry_frame_bottom_part, text='region 11', style='Standard.TLabel')

        self.reg1_label.grid(row=1, column=1, sticky='w', padx=(10, 0), pady=(5, 0))
        self.reg2_label.grid(row=2, column=1, sticky='w', padx=(10, 0), pady=(5, 0))
        self.reg3_label.grid(row=3, column=1, sticky='w', padx=(10, 0), pady=(5, 0))
        self.reg4_label.grid(row=4, column=1, sticky='w', padx=(10, 0), pady=(5, 0))
        self.reg5_label.grid(row=1, column=3, sticky='w', padx=(10, 0), pady=(5, 0))
        self.reg6_label.grid(row=2, column=3, sticky='w', padx=(10, 0), pady=(5, 0))
        self.reg7_label.grid(row=3, column=3, sticky='w', padx=(10, 0), pady=(5, 0))
        self.reg8_label.grid(row=4, column=3, sticky='w', padx=(10, 0), pady=(5, 0))
        self.reg9_label.grid(row=1, column=5, sticky='w', padx=(10, 0), pady=(5, 0))
        self.reg10_label.grid(row=2, column=5, sticky='w', padx=(10, 0), pady=(5, 0))
        self.reg11_label.grid(row=3, column=5, sticky='w', padx=(10, 0), pady=(5, 0))

        # Adding bottom line buttons
        self.see_modelled_temperature_label = ttk.Label(self.bottom_button_frame,
                                                        text='See modelled temperatures',
                                                        style='Standard.TLabel')
        self.see_modelled_temperature_label.grid(row=0, column=0, sticky='w', padx=(20, 0), pady=(5, 5))
        self.see_modelled_temperatures_button = ttk.Button(self.bottom_button_frame,
                                                           text='Open',
                                                           takefocus=False,
                                                           style='Standard.TButton',
                                                           command=self.calulate_temperature_distribution)
        self.see_modelled_temperatures_button.grid(row=1, column=0, sticky='w', padx=(20, 0), pady=(5, 5))

        self.load_temperature_label = ttk.Label(self.bottom_button_frame,
                                                text='Load temperature file',
                                                style='Standard.TLabel')
        self.load_temperature_label.grid(row=0, column=1, sticky='e', padx=(0, 20), pady=(5, 5))
        self.load_temperature_button = ttk.Button(self.bottom_button_frame,
                                                  text='Load',
                                                  takefocus=False,
                                                  style='Standard.TButton')
        self.load_temperature_button.grid(row=1, column=1, sticky='e', padx=(0, 20), pady=(5, 5))

    def calulate_temperature_distribution(self):
        mean_annual = float(self.var_mean_annual.get())
        frost_index = float(self.var_frost_index.get())
        reg_celected = self.var_region.get()
        region = temp_zones[reg_celected]
        c1 = region['c1']
        t1 = region['t1']
        c2 = region['c2']
        t2 = region['t2']

        def func(amp):
            output = 0
            for i in range(366):
                y = mean_annual + amp * (c1 * (np.cos(2 * np.pi / 365 * (t1 + i))) + c2 * (np.cos(4 * np.pi / 365 * (t2 + i))))
                if y < 0:
                    output += y * 24
            f = output + frost_index
            return f
        amp = fsolve(func, np.array(5))[0]

        def calc(i):
            y = mean_annual + amp * (c1 * (np.cos(2 * np.pi / 365 * (t1 + i))) + c2 * (np.cos(4 * np.pi / 365 * (t2 + i))))
            return y


        plt.plot(range(366), [calc(i) for i in range(366)])
        plt.show()

    def freezing_index_model_new(self, target_FI, mean_temperature):
        september = [30, 1.00]
        october = [31, 1.00]
        november = [30, 1.00]
        december = [31, 0.94]
        january_1 = [15, 0.88]
        january_2 = [16, 0.88]
        february = [28, 0.82]
        march = [31, 0.76]
        april = [30, 0.7]
        may = [31, 0.76]
        first_half = [january_1, december, november, october, september]
        second_half = [january_2, february, march, april, may]

        omega = 2*math.pi/365
        base_cos = [math.cos(x*omega) for x in range(1, 366)]
        temp_list = []

        def func(amp):
            temp_list.clear()
            output = 0
            for i in base_cos:
                y = mean_temperature + amp*i
                if y < 0:
                    output += y[0]*24
                    temp_list.append(y[0])
            f = output + target_FI
            return f
        amp = fsolve(func, np.array(5))[0]

        if len(temp_list)%2 == 0:
            half_1 = len(temp_list)/2
            half_2 = len(temp_list)/2
        else:
            half_1 = (len(temp_list)-1) / 2 + 1
            half_2 = (len(temp_list)-1) / 2

        target = half_1
        S_values = []
        while target != 0:
            holder_list = []
            days = first_half[0][0]
            S_val = first_half[0][1]
            if target > days:
                target -= days
                for i in range(days):
                    holder_list.append(S_val)
                S_values = holder_list + S_values
                holder_list.clear()
                first_half.pop(0)
            elif target <= days:
                for i in range(int(target)):
                    holder_list.append(S_val)
                S_values = holder_list + S_values
                target = 0

        target = half_2
        while target != 0:
            holder_list = []
            days = second_half[0][0]
            S_val = second_half[0][1]
            if target > days:
                target -= days
                for i in range(days):
                    holder_list.append(S_val)
                S_values += holder_list
                holder_list.clear()
                second_half.pop(0)
            elif target <= days:
                for i in range(int(target)):
                    holder_list.append(S_val)
                S_values += holder_list
                target = 0

        return temp_list, S_values


class ClimateModelGeneral(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self['style'] = 'Standard.TFrame'

        # ##########  FRAME LAYOUT  ##########
        # Adding top label frame and label
        self.top_label_frame = ttk.Frame(self, style='DarkFrame.TFrame')
        self.top_label_frame.pack(side='top', fill='x')

        # Adding main top entry frame
        self.main_entry_frame_top_part = ttk.Frame(self, style='Standard.TFrame')
        self.main_entry_frame_top_part.pack(side='top', expand='true', fill='both')

        # Adding bottom frame for buttons
        self.bottom_button_frame = ttk.Frame(self, style='Standard.TFrame')
        self.bottom_button_frame.pack(side='top', fill='x')
        self.bottom_button_frame.columnconfigure(0, weight=1)
        self.bottom_button_frame.columnconfigure(1, weight=1)

        # ##########  CONTENT  ##########
        self.main_title = ttk.Label(self.top_label_frame,
                                    text='Climate model (special)',
                                    style='ExtraLargeLabel.TLabel')
        self.main_title.pack(side='left', padx=(10, 0), pady=(5, 5))

        # Adding main top entry widgets
        self.mean_annual_temp_label = ttk.Label(self.main_entry_frame_top_part,
                                                text='Mean annual temperature',
                                                style='Standard.TLabel')
        self.mean_annual_temp_label.grid(row=0, column=0, sticky='w', padx=(10, 0), pady=(20, 0))

        self.var_mean_annual = tk.StringVar()
        self.mean_annual_temp_entry = ttk.Entry(self.main_entry_frame_top_part,
                                                textvariable=self.var_mean_annual,
                                                style='Standard.TEntry')
        self.mean_annual_temp_entry.grid(row=0, column=1, padx=(10, 0), pady=(20, 0))
        self.mean_annual_temp_units = ttk.Label(self.main_entry_frame_top_part,
                                                text='degC',
                                                style='Standard.TLabel')
        self.mean_annual_temp_units.grid(row=0, column=2, sticky='w', padx=(5, 0), pady=(20, 0))

        self.frost_index_label = ttk.Label(self.main_entry_frame_top_part,
                                           text='Frost index',
                                           style='Standard.TLabel')
        self.frost_index_label.grid(row=1, column=0, sticky='w', padx=(10, 0), pady=(20, 0))

        self.var_frost_index = tk.StringVar()
        self.frost_index_entry = ttk.Entry(self.main_entry_frame_top_part,
                                           textvariable=self.var_frost_index,
                                           style='Standard.TEntry')
        self.frost_index_entry.grid(row=1, column=1, padx=(10, 0), pady=(20, 0))
        self.frost_index_units = ttk.Label(self.main_entry_frame_top_part,
                                           text='degC hours',
                                           style='Standard.TLabel')
        self.frost_index_units.grid(row=1, column=2, sticky='w', padx=(5, 0), pady=(20, 0))

        self.select_from_map_label = ttk.Label(self.main_entry_frame_top_part,
                                               text='Select from map:',
                                               style='Standard.TLabel')
        self.select_from_map_label.grid(row=2, column=0, sticky='w', padx=(10, 0), pady=(20, 0))

        self.select_from_map_button = ttk.Button(self.main_entry_frame_top_part,
                                                 text='Open',
                                                 takefocus=False,
                                                 style='Standard.TButton',
                                                 command=self.calulate_temperature_distribution)
        self.select_from_map_button.grid(row=2, column=1, sticky='w', padx=(10, 0), pady=(20, 0))

        # Adding bottom line buttons
        self.see_modelled_temperature_label = ttk.Label(self.bottom_button_frame,
                                                        text='See modelled temperatures',
                                                        style='Standard.TLabel')
        self.see_modelled_temperature_label.grid(row=0, column=0, sticky='w', padx=(20, 0), pady=(5, 5))
        self.see_modelled_temperatures_button = ttk.Button(self.bottom_button_frame,
                                                           text='Open',
                                                           takefocus=False,
                                                           style='Standard.TButton',
                                                           command=self.calulate_temperature_distribution)
        self.see_modelled_temperatures_button.grid(row=1, column=0, sticky='w', padx=(20, 0), pady=(5, 5))

        self.load_temperature_label = ttk.Label(self.bottom_button_frame,
                                                text='Load temperature file',
                                                style='Standard.TLabel')
        self.load_temperature_label.grid(row=0, column=1, sticky='e', padx=(0, 20), pady=(5, 5))
        self.load_temperature_button = ttk.Button(self.bottom_button_frame,
                                                  text='Load',
                                                  takefocus=False,
                                                  style='Standard.TButton')
        self.load_temperature_button.grid(row=1, column=1, sticky='e', padx=(0, 20), pady=(5, 5))

    def calulate_temperature_distribution(self):
        pass

    def select_region_from_map(self):
        pass