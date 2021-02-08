import tkinter as tk
from tkinter import ttk


class DevelopmentWindow(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self['style'] = 'Standard.TFrame'
        self.pack(fill='x')

        # Adding top label frame and label
        self.top_label_frame = ttk.Frame(self, style='DarkFrame.TFrame')
        self.top_label_frame.pack(side='top', fill='x')

        self.main_title = ttk.Label(self.top_label_frame,
                                    text='Development window',
                                    style='ExtraLargeLabel.TLabel')
        self.main_title.pack(side='left', padx=(10, 0), pady=(5, 5))

        self.main_frame = ttk.Frame(self, style='Standard.TFrame')
        self.main_frame.pack(side='top', fill='x')

        # Adding load file label and button
        self.load_file_label = ttk.Label(self.main_frame,
                                         text='Load external file',
                                         style='Standard.TLabel')
        self.load_file_label.grid(row=0, column=0, sticky='w', pady=(15, 15))
        self.load_file_button = ttk.Button(self.main_frame,
                                           text='Load',
                                           takefocus=False,
                                           style='Standard.TButton',
                                           command=self.controller.load_full_file)
        self.load_file_button.grid(row=0, column=1, sticky='w', padx=(10, 0))

        # Adding run calculation label and button
        self.run_file_label = ttk.Label(self.main_frame,
                                         text='Run calculation',
                                         style='Standard.TLabel')
        self.run_file_label.grid(row=1, column=0, sticky='w', pady=(15, 15))
        self.run_file_button = ttk.Button(self.main_frame,
                                          text='Run',
                                          takefocus=False,
                                          style='Standard.TButton',
                                          command=self.controller.run_calculation_for_single_case)
        self.run_file_button.grid(row=1, column=1, sticky='w', padx=(10, 0))