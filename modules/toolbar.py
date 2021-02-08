import tkinter as tk
from tkinter import ttk

class ToolBar(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        self.pack(side='top', fill='both', expand=True)
        self['style'] = 'ToolBar.TFrame'

        # Loading image files
        self.image_new = tk.PhotoImage(file='modules/icons/doc_empty_icon&16_inverted.png')
        self.image_open = tk.PhotoImage(file='modules/icons/folder_open_icon&16_inverted.png')
        self.image_save = tk.PhotoImage(file='modules/icons/save_icon&16_inverted.png')
        self.image_info = tk.PhotoImage(file='modules/icons/lightbulb_icon&16_inverted.png')

        # Creating buttons
        self.button_new = ttk.Button(self,
                                     image=self.image_new,
                                     style='ToolBar.TButton',
                                     takefocus=False,
                                     command=self.controller.toolbar_button_new)
        self.button_open = ttk.Button(self,
                                      image=self.image_open,
                                      style='ToolBar.TButton',
                                      takefocus=False,
                                      command=self.controller.toolbar_button_open)
        self.button_save = ttk.Button(self,
                                      image=self.image_save,
                                      style='ToolBar.TButton',
                                      takefocus=False,
                                      command=self.controller.toolbar_button_save)
        self.button_info = ttk.Button(self,
                                      image=self.image_info,
                                      style='ToolBar.TButton',
                                      takefocus=False,
                                      command=self.controller.toolbar_button_info)

        # Packing buttons
        self.button_new.grid(row=0, column=0, padx=(5, 0), pady=(2, 2))
        self.button_open.grid(row=0, column=1, padx=(7, 0), pady=(2, 2))
        self.button_save.grid(row=0, column=2, padx=(7, 0), pady=(2, 2))
        self.button_info.grid(row=0, column=3, padx=(7, 0), pady=(2, 2))
        #padx = (5, 10), pady = (5, 5)
