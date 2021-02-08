import tkinter as tk
from tkinter import ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
matplotlib.use('TkAgg')
import math
import numpy as np


class PlotFigure1(ttk.Frame):
    def __init__(self, fig1_frame, array_df, interface_lim_list, chaussee_file_chau_z_list,
                 chaussee_file_day_list, site_file_day_list, site_file_site_z_list, layer_count,
                 chaussee_file_chau_h_list, site_file_site_h_list):
        super().__init__(fig1_frame)
        self.pack(side='top', fill='both', expand=True)
        self.fig1_frame = fig1_frame
        self.array_df = array_df
        self.interface_lim_list = interface_lim_list
        self.chaussee_file_chau_z_list = chaussee_file_chau_z_list
        self.chaussee_file_day_list = chaussee_file_day_list
        self.site_file_day_list = site_file_day_list
        self.site_file_site_z_list = site_file_site_z_list
        self.layer_count = layer_count
        self.chaussee_file_chau_h_list = chaussee_file_chau_h_list
        self.site_file_site_h_list = site_file_site_h_list

    def plot_figure1(self):
        def find_x_lim(x):
            x_lim = int(math.ceil(x / 10.0)) * 10
            return x_lim

        def find_y_lim_frost(y):
            y_lim = int(math.ceil(y / 0.5)) * 0.5
            return y_lim

        def find_y_min_temperature(y):
            y_lim = int(math.floor(y / 5)) * 5
            return y_lim

        def find_y_max_temperature(y):
            y_lim = int(math.ceil(y / 5)) * 5
            return y_lim

        x_lim = find_x_lim(self.array_df['day'].max())
        y_lim = find_y_lim_frost(self.interface_lim_list[-2])
        y_min_temperature = find_y_min_temperature(self.array_df['Ts'].min())
        y_max_temperature = find_y_max_temperature(self.array_df['Ts'].max())

        fig = Figure(figsize=(14, 6), dpi=100)
        fig.patch.set_facecolor('#262626')
        ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax1.set_facecolor('#262626')
        ax1.set_title('TITLE 1', size=14, color='white')
        plot1 = ax1.plot(self.array_df['day'],
                         self.array_df['z'],
                         label='Frost penetration (Python)',
                         lw=2, color='olivedrab')
        if np.nansum(np.array(self.chaussee_file_chau_z_list)) != 0:
            plot5 = ax1.plot(self.chaussee_file_day_list,
                             self.chaussee_file_chau_z_list,
                             label='Chaussee results',
                             linestyle='None',
                             marker='x',
                             ms=3,
                             mew=1,
                             color='royalblue')
        else:
            plot5 = None
        plot2 = ax1.plot(self.site_file_day_list,
                         self.site_file_site_z_list,
                         label='Site measurement',
                         linestyle='None',
                         marker='+',
                         ms=5,
                         mew=1,
                         color='darkorange')
        #plot3 = ax1.plot(self.df_cpp_result_day,
        #                 self.df_cpp_result_z,
        #                 label="Frost penetration (C++)",
        #                 linestyle='None',
        #                 marker='o',
        #                 ms=3,
        #                 mew=1,
        #                 color='firebrick')

        for i in range(self.layer_count - 1):
            ax1.plot([-5, x_lim+5], [self.interface_lim_list[i], self.interface_lim_list[i]], lw=1.5, ls='dashdot',
                      color='black')
        ax1.set_xlim([-5, x_lim + 5])
        ax1.set_xticks(range(0, x_lim + 10, 10))
        ax1.set_xlabel('Days', size=12, color='white')
        ax1.set_ylim([-0.10, y_lim + 0.5])
        ax1.set_ylabel('Frost depth, m', size=12, color='white')
        for axis in ['top', 'bottom', 'left', 'right']:
            ax1.spines[axis].set_linewidth(1.5)
            ax1.spines[axis].set_color('white')
        ax1.tick_params(axis='both', direction='in', width=1.5, right=True, top=True, colors='white')
        ax1.invert_yaxis()

        ax2 = ax1.twinx()
        plot4 = ax2.plot(self.array_df['day'], self.array_df['Ts'], label='Temperature', ls=':', lw=1, color='darkgrey')
        ax2.plot([-5, x_lim + 5], [0, 0], ls='--', lw=1, color='darkgrey')
        boolean_list = []
        for i in self.array_df['Ts']:
            if i <= 0:
                boolean_list.append(True)
            else:
                boolean_list.append(False)
        ax2.fill_between(self.array_df['day'], self.array_df['Ts'], where=boolean_list,
                                 color='black', interpolate=True, alpha=0.08)
        ax2.set_ylim([y_min_temperature, y_max_temperature])
        ax2.tick_params(axis='both', direction='in', width=1.5, right=True, top=True, colors='white')
        ax2.set_ylabel('Temperature, °C', size=12)

        if plot5 == None:
            #plots = plot1 + plot2 + plot3 + plot4
            plots = plot1 + plot2 + plot4
        else:
            #plots = plot1 + plot2 + plot3 + plot4 + plot5
            plots = plot1 + plot2 + plot4 + plot5
        labels = [l.get_label() for l in plots]
        ax1.legend(plots, labels, loc='lower left', edgecolor='black')

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

class PlotFigure2(ttk.Frame):
    def __init__(self, fig2_frame, array_df, interface_lim_list, chaussee_file_chau_z_list,
                 chaussee_file_day_list, site_file_day_list, site_file_site_z_list, layer_count,
                 chaussee_file_chau_h_list, site_file_site_h_list):
        super().__init__(fig2_frame)
        self.pack(side='top', fill='both', expand=True)
        self.fig2_frame = fig2_frame
        self.array_df = array_df
        self.interface_lim_list = interface_lim_list
        self.chaussee_file_chau_z_list = chaussee_file_chau_z_list
        self.chaussee_file_day_list = chaussee_file_day_list
        self.site_file_day_list = site_file_day_list
        self.site_file_site_z_list = site_file_site_z_list
        self.layer_count = layer_count
        self.chaussee_file_chau_h_list = chaussee_file_chau_h_list
        self.site_file_site_h_list = site_file_site_h_list

    def plot_figure2(self):
        def find_x_lim(x):
            x_lim = int(math.ceil(x / 10.0)) * 10
            return x_lim

        def find_y_lim_frost(y):
            y_lim = int(math.ceil(y / 0.02)) * 0.02
            return y_lim

        x_lim = find_x_lim(self.array_df['day'].max())
        y_lim = find_y_lim_frost(self.array_df['h'].max())*1000
        if y_lim < 10:
            y_lim = 10

        fig = Figure(figsize=(8, 6), dpi=100)
        ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax1.set_title('TITLE 2', size=14)
        ax1.plot(self.array_df['day'], self.array_df['h'] * np.array(1000), label='Frost heave (Python)', lw=2, color='olivedrab')
        if np.nansum(np.array(self.chaussee_file_chau_h_list)) != 0:
            ax1.plot(self.chaussee_file_day_list, self.chaussee_file_chau_h_list, label='Chaussee results',
                     linestyle='None', marker='x', ms=3, mew=1, color='royalblue')
        ax1.plot(self.site_file_day_list, self.site_file_site_h_list, label='Site measurement',
                 linestyle='None', marker='+', ms=4, mew=1, color='darkorange')
        #ax1.plot(self.df_cpp_result_day, np.array(self.df_cpp_result_h)*1000, label="Frost heave (C++)",
        #         linestyle='None', marker='o', ms=3, mew=1, color='firebrick')
        ax1.legend(loc="upper left")
        ax1.set_xlim([-5, x_lim + 5])
        ax1.set_xticks(range(0, x_lim + 10, 10))
        ax1.set_ylim([-5, y_lim+5])
        ax1.set_xlabel('Days', size=12)
        ax1.set_ylabel('Frost heave, mm', size=12)
        for axis in ['top', 'bottom', 'left', 'right']:
            ax1.spines[axis].set_linewidth(1.5)
        ax1.tick_params(axis='both', direction='in', width=1.5, right=True, top=True)

        ax2 = ax1.twinx()
        ax2.set_ylim([-5, y_lim + 5])
        ax2.tick_params(axis='both', direction='in', width=1.5, right=True, top=True)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side='top', fill='both', expand=True)


