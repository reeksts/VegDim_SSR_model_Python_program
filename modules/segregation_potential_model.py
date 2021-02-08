import tkinter as tk
from tkinter import ttk

class SegregationPotentialModel(tk.Toplevel):
    def __init__(self, row):
        super().__init__()
        self.geometry("400x400")
        self.title("Segregation potential model")
        self.resizable(False, False)

        # Variable definition
        self.Ss = 0
        self.M_MB = 0
        self.M_mol_MB = 319.87
        self.A_v = 6.02*10**23
        self.A_MB = 0

        # Adding main frame
        self.main_frame = ttk.Frame(self, padding=10, style='Standard.TFrame')
        self.main_frame.pack(side='top', fill='both', expand=True)

        # Adding top label frame and label
        self.top_label_frame = ttk.Frame(self.main_frame, style='DarkFrame.TFrame')
        self.top_label_frame.pack(side='top', fill='x')

        self.main_title = ttk.Label(self.top_label_frame,
                                    text='Segregation potential (SP)',
                                    style='ExtraLargeLabel.TLabel')
        self.main_title.pack(side='left', padx=(10, 0), pady=(5, 5))

    def calculation_of_Ss(self):
        pass

    def calculation_of_SP(self):
        pass