import tkinter as tk
from tkinter import ttk


class NotesWindow(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self['style'] = 'Standard.TFrame'
        self.pack(side='top', fill='x', pady=(20, 0))

        # Adding top label frame and label
        self.top_label_frame = ttk.Frame(self, style='DarkFrame.TFrame')
        self.top_label_frame.pack(side='top', fill='x')
        self.main_title = ttk.Label(self.top_label_frame,
                                    text='Notes',
                                    style='ExtraLargeLabel.TLabel')
        self.main_title.pack(side='left', padx=(10, 0), pady=(5, 5))

        # Adding main top entry frame
        self.main_frame = ttk.Frame(self, style='Standard.TFrame', height=100)
        self.main_frame.pack(side='top', fill='x')

        # Adding text editor window
        #self.text_editor = tk.Text(self.main_frame)
        #self.text_editor.pack(padx=30, pady=30)