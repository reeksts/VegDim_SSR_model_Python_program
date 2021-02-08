import tkinter as tk
from tkinter import ttk


class ModelControlWindow(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self['style'] = 'Standard.TFrame'
        self.pack(fill='x')

        # Adding top label frame and label
        self.top_label_frame = ttk.Frame(self, style='DarkFrame.TFrame')
        self.top_label_frame.pack(side='top', fill='x')

        # Adding main top entry frame
        self.main_frame = ttk.Frame(self, style='Standard.TFrame')
        self.main_frame.pack(side='top', fill='x')

        # Adding man title label
        self.main_title = ttk.Label(self.top_label_frame,
                                    text='Model control',
                                    style='ExtraLargeLabel.TLabel')
        self.main_title.pack(side='left', padx=(10, 0), pady=(5, 5))

        # Add single study frame and widgets
        self.single_study_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.single_study_frame.pack(side='top', fill='x')
        self.single_test_analysis_label = ttk.Label(self.single_study_frame,
                                                    text='Run single test analysis:',
                                                    style='Standard.TLabel')
        self.single_test_analysis_label.grid(row=0, column=0, sticky='w', padx=(10, 0), pady=(10, 0))
        self.single_test_button = ttk.Button(self.single_study_frame,
                                             text='Run',
                                             takefocus=False,
                                             style='Standard.TButton',
                                             command=self.controller.run_calculation_for_new_cases)
        self.single_test_button.grid(row=0, column=1, sticky='w', padx=(10, 0), pady=(10, 0))

        # Add other study type frame and widgets
        self.other_studies_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.other_studies_frame.pack(side='top', fill='x')
        self.property_study_label = ttk.Label(self.other_studies_frame,
                                              text='Perform parameter study on material properties:',
                                              style='Standard.TLabel')
        self.property_study_label.grid(row=0, column=0, sticky='w', padx=(10, 0), pady=(20, 0))

        self.property_study_button = ttk.Button(self.other_studies_frame,
                                                text='Open',
                                                takefocus=False,
                                                style='Standard.TButton',
                                                command=self.controller.open_parameter_study)
        self.property_study_button.grid(row=0, column=1, sticky='w', padx=(10, 0), pady=(20, 0))

        self.climate_study_label = ttk.Label(self.other_studies_frame,
                                               text='Perform parameter study on climate:',
                                               style='Standard.TLabel')
        self.climate_study_label.grid(row=1, column=0, sticky='w', padx=(10, 0), pady=(10, 0))

        self.climate_study_button = ttk.Button(self.other_studies_frame,
                                               text='Start',
                                               takefocus=False,
                                               style='Standard.TButton',
                                               command=self.controller.run_climate_study)
        self.climate_study_button.grid(row=1, column=1, sticky='w', padx=(10, 0), pady=(10, 0))