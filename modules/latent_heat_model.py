import tkinter as tk

class LatentHeatModel(tk.Toplevel):
    def __init__(self, row):
        super().__init__()
        self.geometry("400x400")
        self.title("Latent heat model")
        self.resizable(False, False)

        self.row = row
        print(self.row)