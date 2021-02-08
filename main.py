import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from modules.menu_bar import MenuBar
from modules.start_page import StartPage
from modules.main_page import MainPage
from modules.style_configuration import StyleConfiguration
#import numpy as np
#import pandas as pd
#import matplotlib
#matplotlib.use('TkAgg')
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
#from matplotlib.figure import  Figure
#from matplotlib import style
#import sqlite3
#import _2_th_cond
#from tkinter import messagebox

#style.use('ggplot')

#con = sqlite3.connect('library.db')
#cur = con.cursor()


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Frost Lite')
        self.geometry('+300+300')
        self.resizable(True, True)
        self.config(menu=MenuBar(self))

        # Create container frame
        self.container_frame = tk.Frame(self, bg='#cdccd5')
        self.container_frame.pack(side='top', fill='both', expand=True)
        self.container_frame.rowconfigure(0, weight=1)
        self.container_frame.columnconfigure(0, weight=1)

        self.frame_pages = dict()

        for page_class in [StartPage, MainPage]:
            page = page_class(self.container_frame, self)
            self.frame_pages[page_class] = page
            page.grid(row=0, column=0, sticky='nsew')

        self.switch_page(MainPage)

    def switch_page(self, page_class):
        page = self.frame_pages[page_class]
        page.tkraise()

    # Menu options
    def toolbar_on_off(self, status):
        self.frame_pages[MainPage].toolbar_on_off(status)

    def switch_climate_model(self, selection):
        self.frame_pages[MainPage].switch_climate_model(selection)

    def switch_flux_model(self, selection):
        self.frame_pages[MainPage].switch_flux_model(selection)

    def show_hide_figures(self, status):
        self.frame_pages[MainPage].show_hide_figures(status)

    def resizable_window(self, status):
        if status == False:
            self.resizable(False, False)
        elif status == True:
            self.resizable(True, True)


def main():
    root = MainApp()
    style = ttk.Style()
    StyleConfiguration(style)
    root.mainloop()


if __name__ == '__main__':
    main()
