import tkinter as tk
from tkinter import ttk
from modules.main_page import MainPage

class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=10)
        self.parent = parent
        self.controller = controller

        self.button = tk.Button(self, text='To Main Page', command=lambda: self.controller.switch_page(MainPage))
        self.button.grid()