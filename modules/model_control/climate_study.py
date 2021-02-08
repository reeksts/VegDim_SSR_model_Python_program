import tkinter as tk
from tkinter import ttk

class ClimateStudy(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.geometry("400x500")
        self.title("Climate study")
        self.resizable(False, False)
        self.controller = controller