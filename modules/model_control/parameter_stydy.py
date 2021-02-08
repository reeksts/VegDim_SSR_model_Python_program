import tkinter as tk
from tkinter import ttk

class ParameterStudy(tk.Toplevel):
    def __init__(self, controller, layer_names):
        super().__init__()
        self.geometry("400x500")
        self.title("Parameter study")
        self.resizable(False, False)
        self.controller = controller
        self.layer_names = layer_names

        # Adding main frame
        self.main_frame = ttk.Frame(self, padding=10, style='Standard.TFrame')
        self.main_frame.pack(side='top', fill='both', expand=True)

        # Adding top label frame and label
        self.top_label_frame = ttk.Frame(self.main_frame, style='DarkFrame.TFrame')
        self.top_label_frame.pack(side='top', fill='x')

        self.main_title = ttk.Label(self.top_label_frame,
                                    text='Parameter study',
                                    style='ExtraLargeLabel.TLabel')
        self.main_title.pack(side='left', padx=(10, 0), pady=(5, 5))

        # Adding layer selection title
        self.layer_selection_title_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.layer_selection_title_frame.pack(side='top', fill='x')
        self.layer_selection_label = ttk.Label(self.layer_selection_title_frame,
                                               text='Select layer to study:',
                                               style='Standard.TLabel')
        self.layer_selection_label.pack(side='left', pady=(10, 5))

        # Adding layer name selection
        self.layer_selection_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.layer_selection_frame.pack(side='top', fill='x')

        row_number = 0
        selection = 0
        self.layer_selection = tk.IntVar()
        print(self.layer_selection.get())
        for material in self.layer_names:
            radiobutton = ttk.Radiobutton(self.layer_selection_frame,
                                          variable=self.layer_selection,
                                          value=selection,
                                          takefocus=False,
                                          style='Standard.TRadiobutton')
            radiobutton.grid(row=row_number, column=0, padx=(10, 0))

            label = ttk.Label(self.layer_selection_frame,
                              text=material,
                              style='Standard.TLabel')
            label.grid(row=row_number, column=1, sticky='w', padx=(10, 0))

            selection += 1
            row_number += 1

        # Adding layer selection title
        self.layer_selection_title_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.layer_selection_title_frame.pack(side='top', fill='x')
        self.layer_selection_label = ttk.Label(self.layer_selection_title_frame,
                                                text='Select property to study:',
                                                style='Standard.TLabel')
        self.layer_selection_label.pack(side='left', pady=(10, 5))

        # Adding property to study selection
        self.property_selection_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.property_selection_frame.pack(side='top', fill='x')

        row_number = 0
        selection = 1
        self.property_selection = tk.StringVar()
        for property in ['w%', 'SP', 'ku', 'kf']:
            radiobutton = ttk.Radiobutton(self.property_selection_frame,
                                            variable=self.property_selection,
                                            value=property,
                                            takefocus=False,
                                            style='Standard.TRadiobutton')
            radiobutton.grid(row=row_number, column=0, sticky='w', padx=(10, 0))

            label = ttk.Label(self.property_selection_frame,
                                text=property,
                                style='Standard.TLabel')
            label.grid(row=row_number, column=1, padx=(10, 0))

            selection += 1
            row_number += 1

        # Adding layer selection title
        self.property_entry_title_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.property_entry_title_frame.pack(side='top', fill='x')
        self.property_entry_title = ttk.Label(self.property_entry_title_frame,
                                        text='Enter values:',
                                        style='Standard.TLabel')
        self.property_entry_title.pack(side='left', pady=(10, 0))

        self.property_entry_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.property_entry_frame.pack(side='top', fill='x')
        self.entry_value_list = tk.StringVar()
        self.property_entry = ttk.Entry(self.property_entry_frame,
                                        width=25,
                                        textvariable=self.entry_value_list,
                                        style='Standard.TEntry')
        self.property_entry.pack(side='left', pady=(10, 5))

        # Adding run button
        self.run_button_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.run_button_frame.pack(side='top', fill='x')
        self.run_button = ttk.Button(self.run_button_frame,
                                     text='Run',
                                     style='Standard.TButton',
                                     takefocus=False,
                                     command=self.run_parameter_study)
        self.run_button.pack(side='left', pady=(10, 5))

    def run_parameter_study(self):
        layer_selected = self.layer_selection.get()
        property_selected = self.property_selection.get()
        values = []
        for i in self.entry_value_list.get().split(', '):
            values.append(float(i))
        self.controller.run_parameter_study(layer_selected, property_selected, values)
        self.destroy()


