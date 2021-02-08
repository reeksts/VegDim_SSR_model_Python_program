import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import fsolve

class SSR_model:
    def __init__(self, df_layers, df_data, df_other, df_chaussee, df_site):
        self.df_layers = df_layers
        self.df_data = df_data
        self.df_other = df_other
        self.df_chaussee = df_chaussee
        self.df_site = df_site
        #self.df_cpp_result = pd.read_csv(filename_2 + filename_1 + "_cpp_model_results.csv")
        #self.df_cpp_result_day = []
        #self.df_cpp_result_z = []
        #self.df_cpp_result_h = []

        #for i in range(self.df_cpp_result["day"].size):
        #    if i%3 == 0:
        #        self.df_cpp_result_day.append(self.df_cpp_result["day"][i])
        #        self.df_cpp_result_z.append(self.df_cpp_result["z"][i])
        #        self.df_cpp_result_h.append(self.df_cpp_result["h"][i])

        # Filenames
        #self.excel_file_name = filename_3 + filename_1 + '_df' + '.xlsx'
        #self.figure_label_1 = " ".join(filename_1[3:].split("_")) + " frost depth"
        #self.figure_label_2 = " ".join(filename_1[3:].split("_")) + " frost heave"
        #self.figure_file_name_1 = filename_3 + filename_1 + '_fig_1' + '.png'
        #self.figure_file_name_2 = filename_3 + filename_1 + '_fig_2' + '.png'
        self.excel_file_name = 'test_df.xlsx'
        self.figure_label_1 = 'frost depth'
        self.figure_label_2 = 'frost heave'
        self.figure_file_name_1 = 'fig_1.png'
        self.figure_file_name_2 = 'fig_2.png'

        # Limit counts
        self.layer_count = self.df_layers['ku'].count()

        self.days = self.df_data['day'].count()
        self.total_test_time = self.days * 24

        self.layer_thickness_list = list(self.df_layers.iloc[0:self.layer_count - 1, 1])
        self.layer_thickness_list.append(10)
        self.layer_thickness_list_mod = self.layer_thickness_list.copy()
        self.interface_lim_list = list(np.cumsum(self.layer_thickness_list))

        # Input: Data lists
        self.day_list = self.df_data['day'].tolist()
        self.date_list = self.df_data['date'].tolist()
        self.temps_list = self.df_data['temps'].to_list()
        self.S_vals_list = self.df_data['S_vals'].tolist()

        # Input: layer property lists
        self.ku_list = list(self.df_layers.iloc[0:self.layer_count, 2])
        self.kf_list = list(self.df_layers.iloc[0:self.layer_count, 3])
        self.SP_list = list(self.df_layers.iloc[0:self.layer_count, 4])
        self.a_list = list(self.df_layers.iloc[0:self.layer_count, 5])
        self.Sr_list = list(self.df_layers.iloc[0:self.layer_count, 6])
        self.Ls_list = list(self.df_layers.iloc[0:self.layer_count, 7])
        self.w_list = list(self.df_layers.iloc[0:self.layer_count, 8])
        self.rhod_list = list(self.df_layers.iloc[0:self.layer_count, 9])

        # Input: Loading chaussee file
        zero_list = [0]
        self.chaussee_file_day_list = zero_list + self.df_chaussee['day'].tolist()
        self.chaussee_file_dt_list = zero_list + self.df_chaussee['dt'].tolist()
        self.chaussee_file_temps_list = zero_list + self.df_chaussee['temp'].tolist()
        self.chaussee_file_chau_z_list = zero_list + self.df_chaussee['chau_z'].tolist()
        self.chaussee_file_chau_h_list = zero_list + self.df_chaussee['chau_h'].tolist()
        self.chaussee_file_chau_h_list = [i*1000 for i in self.chaussee_file_chau_h_list]

        # Input: Loading site file
        zero_list = [0]
        self.site_file_day_list = zero_list + self.df_site['day'].tolist()
        self.site_file_dt_list = zero_list + self.df_site['dt'].tolist()
        self.site_file_temps_list = zero_list + self.df_site['temp'].tolist()
        self.site_file_site_z_list = zero_list + self.df_site['site_z'].tolist()
        self.site_file_site_h_list = zero_list + self.df_site['site_h'].tolist()
        self.site_file_site_h_list = [i * 1000 for i in self.site_file_site_h_list]

        # Input: constants
        self.ki = 2.24
        self.Tf = 0
        self.Lw = 92500
        self.rhow = 1

        # Input: other input
        self.flag = self.df_other[0][1]
        self.xps = self.df_other[1][1]
        self.Tma = self.df_other[2][1]
        self.lim = self.df_other[3][1]
        self.gradT_p = (0.43 * self.Tma + 1) / 0.82
        self.lim_upper = self.lim - self.xps
        self.lim_lower = self.lim
        self.Cq_upper = 10 ** (-4.5 * self.xps ** 0.8)
        self.Cq_lower = 1.0

        # Time step calculations: set properties
        self.ku_low = 0
        self.kf_low = 0
        self.a_low = 0
        self.SP_low = 0
        self.Sr_low = 0
        self.Ls_low = 0
        self.w_vol_low = 0
        self.rhod_low = 0

        # Time step caculations: step caclulations
        self.current_hour_count = 0
        self.hours_count = 0
        self.days_count = 0
        self.day_index = 0
        self.day = 0
        self.FI = 0

        self.dz0_sum = 0
        self.dh0 = 0
        self.dhs = 0
        self.dh = 0
        self.z = 0
        self.dz = 0
        self.dh0_sum = 0
        self.dhs_sum = 0
        self.h = 0
        self.dz0_residual = 0
        self.closest_interface = 0
        self.dz0_first = 0
        self.dz0_second = 0

        self.Rf = 0
        self.idx_low = 0
        self.Ts = 0
        self.S = 0
        self.flux = 0
        self.Cq = 0

        self.imp_vs_exp = 0

        self.pos_flux = 0
        self.neg_flux = 0
        self.freeze_water_flux = 0
        self.segregation_flux = 0

        self.root_1 = 0
        self.root_2 = 0

        # Data output containers
        self.time_output = np.array([0])
        self.dt_output = np.array([float('nan')])
        self.hours_output = np.array([0])
        self.closest_interface_output = np.array([float('nan')])
        self.FI_output = np.array([0])
        self.Ts_output = np.array([float('nan')])
        self.ku_output = np.array([float('nan')])
        self.kf_output = np.array([float('nan')])
        self.SP_output = np.array([float('nan')])
        self.a_output = np.array([float('nan')])
        self.Ls_output = np.array([float('nan')])
        self.S_output = np.array([float('nan')])
        self.Sr_output = np.array([float('nan')])
        self.Rf_output = np.array([float('nan')])
        self.dz0_imp_output = np.array([0])
        self.imp_1_vs_exp_0_output = np.array([0])
        self.dz0_sum_output = np.array([0])
        self.dh0_output = np.array([0])
        self.dh0_sum_output = np.array([0])
        self.dhs_output = np.array([0])
        self.dhs_sum_output = np.array([0])
        self.dh_output = np.array([0])
        self.h_output = np.array([0])
        self.dz_output = np.array([0])
        self.z_output = np.array([0])
        self.idx_output = np.array([float('nan')])
        self.gradT_p_output = np.array([float('nan')])
        self.flux_output = np.array([float('nan')])
        self.Cq_output = np.array([float('nan')])
        self.root_1_output = np.array([float('nan')])
        self.root_2_output = np.array([float('nan')])
        self.pos_flux_output = np.array([float('nan')])
        self.neg_flux_output = np.array([float('nan')])
        self.freeze_water_flux_output = np.array([float('nan')])
        self.segregation_flux_output = np.array([float('nan')])
        self.xps_output = np.array([float('nan')])

    def set_full_step_dt(self):
        dt = 24
        self.current_hour_count += 24
        self.day_index = math.ceil(self.current_hour_count / 24) - 1
        self.day = math.ceil(self.current_hour_count / 24)
        return dt

    def increment_current_hour_count(self, dt):
        self.current_hour_count += dt

    def decrement_current_hour_count(self, dt):
        self.current_hour_count -= dt

    def set_index(self):
        def find_nearest(array, value):
            array = np.asarray(array)
            local = (np.abs(array - value)).argmin()
            return array[local]

        nearest = find_nearest(self.interface_lim_list, self.dz0_sum)
        if self.dz0_sum < nearest:
            self.idx_low = self.interface_lim_list.index(nearest)
        else:
            self.idx_low = self.interface_lim_list.index(nearest) + 1

    def check_for_close_interface(self):
        self.closest_interface = self.interface_lim_list[self.idx_low]
        if self.closest_interface - self.dz0_sum < 0.001:
            self.dz0_sum = self.closest_interface
            return True
        else:
            return False

    def interface_check(self, dz0_imp):
        self.closest_interface = self.interface_lim_list[self.idx_low]
        return self.dz0_sum + dz0_imp > self.closest_interface

    def calculate_dz0_residual(self):
        dz0_resid = self.closest_interface - self.dz0_sum
        return dz0_resid

    def set_partial_time_step(self, partial_time_step):
        dt = 24 - partial_time_step
        self.current_hour_count += dt
        self.day_index = math.ceil(self.current_hour_count / 24) - 1
        self.day = math.ceil(self.current_hour_count / 24)
        return dt

    def increment_partial_time_step(self, partial_time_step, dt):
        partial_time_step += dt
        return partial_time_step

    def set_flux_func_based(self):
        if self.dz0_sum <= self.lim_upper:
            self.Cq = self.Cq_upper
        elif self.lim_upper < self.dz0_sum < self.lim_lower:
            self.Cq = (self.dz0_sum - self.lim_upper) / (self.lim_lower - self.lim_upper) * (
                        self.Cq_lower - self.Cq_upper) + self.Cq_upper
        else:
            self.Cq = self.Cq_lower
        self.flux = (((250 - self.day) * (9.62 + 1.44 * math.log(self.Tma))) /
                     (250 + (5.78 - 1.62 * math.log(self.Tma)) * self.day) + 1.2) * self.Cq

    def set_flux_gradT_based(self):
        self.flux = self.S * self.gradT_p * self.ku_low

    def set_temp(self):
        self.Ts = self.temps_list[self.day_index]

    def set_S(self):
        self.S = self.S_vals_list[self.day_index]

    def set_layer_props(self):
        self.ku_low = self.ku_list[self.idx_low]
        self.kf_low = self.kf_list[self.idx_low]
        self.a_low = self.a_list[self.idx_low]
        self.SP_low = self.SP_list[self.idx_low] * math.exp(-self.a_low * 0.02 * self.z)
        self.Sr_low = self.Sr_list[self.idx_low]
        self.Ls_low = self.Ls_list[self.idx_low]
        self.w_vol_low = self.w_list[self.idx_low]
        self.rhod_low = self.rhod_list[self.idx_low]

    def set_resistance(self):
        res_1 = 0
        for i in range(self.idx_low):
            res_1 += self.layer_thickness_list_mod[i] / self.kf_list[i]
        res_2 = (self.layer_thickness_list_mod[self.idx_low] - (
                    sum(self.layer_thickness_list[0:self.idx_low + 1]) - self.dz0_sum)) / self.kf_low
        res_3 = self.dhs_sum / self.ki
        self.Rf = res_1 + res_2 + res_3

    def calculate_dz0_imp(self, dt):
        if self.flag == 0:
            self.set_flux_gradT_based()
        else:
            SSR_model.set_flux_func_based(self)
        a = 0.5 * self.Ls_low
        b = 0.5 * self.flux * dt + self.Ls_low * self.kf_low * self.Rf
        c = (self.flux * dt * self.kf_low * self.Rf + self.Lw * (self.SP_low / 1000000) * (
                    self.Tf - self.Ts) * dt - self.kf_low * (self.Tf - self.Ts) * dt)
        self.root_2, self.root_1 = np.roots([a, b, c])
        if not isinstance(self.root_2, float):
            self.root_1 = SSR_model.calculate_dz0_exp(self, dt)
            self.root_2 = float('nan')
        return self.root_1

    def calculate_dz0_exp(self, dt):
        if self.flag == 0:
            SSR_model.set_flux_gradT_based(self)
        else:
            SSR_model.set_flux_func_based(self)
        if self.Rf == 0:
            dz0_exp = 0
        else:
            dz0_exp = ((self.Tf - self.Ts) * dt * (1 - self.SP_low / 1000000 * self.Lw / self.kf_low)) / \
                  (self.Ls_low * self.Rf) - self.flux * dt / self.Ls_low

        return dz0_exp

    def calculate_dt(self, dz0_resid):
        def func(dt):
            f = self.flux + self.Ls_low * dz0_resid / dt + self.Lw * (self.SP_low / 1000000) * \
                (self.Tf - self.Ts) / (self.kf_low * self.Rf + 0.5 * dz0_resid) - self.kf_low * (self.Tf - self.Ts) / \
                (self.kf_low * self.Rf + 0.5 * dz0_resid)
            return f

        dt = fsolve(func, np.array(0.1))[0]
        return dt

    def adjust_current_hour_count(self):
        if isinstance(self.current_hour_count, float):
            top_delta = math.ceil(self.current_hour_count) - self.current_hour_count
            bottom_delta = self.current_hour_count - math.floor(self.current_hour_count)
            if top_delta < bottom_delta:
                self.current_hour_count = math.ceil(self.current_hour_count)
            else:
                self.current_hour_count = math.floor(self.current_hour_count)

    def calculate_step_increments(self, dt, dz0_imp):
        if dz0_imp <= 0:
            self.dh0 = 0
            self.dhs = 0
            self.dh = self.dh0 + self.dhs
            self.h += self.dh
            self.dz = dz0_imp + self.dh
            self.z += self.dz
            self.dz0_sum += dz0_imp
            self.dh0_sum += self.dh0
            self.dhs_sum += self.dhs
            if self.dz0_sum <= 0.01:
                self.dz0_sum = 0.01
                self.z = 0
        else:
            if self.Sr_list[self.idx_low] <= 85:
                self.dh0 = 0
            else:
                self.dh0 = (dz0_imp * 0.09 * self.w_vol_low / 100 * self.rhod_low / self.rhow) * (self.Sr_low - 85) / 15
            self.layer_thickness_list_mod[self.idx_low] += self.dh0

            self.dhs = (1.09 * self.SP_low / 1000000 * (self.Tf - self.Ts) * dt) / (
                        self.kf_low * self.Rf + 0.5 * dz0_imp)
            self.dh = self.dh0 + self.dhs
            self.h += self.dh

            self.dz = dz0_imp + self.dh
            self.z += self.dz

            self.dz0_sum += dz0_imp
            self.dh0_sum += self.dh0
            self.dhs_sum += self.dhs

    def calculate_FI(self, dt):
        if self.Ts < 0:
            self.FI += dt * self.Ts * -1
        else:
            self.FI = self.FI

    def calculate_balance_flux(self, dt, dz0_imp):
        if ((self.kf_low * self.Rf + 0.5 * dz0_imp) == 0):
            self.neg_flux = 0
        else:
            self.neg_flux = self.kf_low * (self.Tf - self.Ts) / (self.kf_low * self.Rf + 0.5 * dz0_imp)
        self.pos_flux = self.flux
        self.freeze_water_flux = self.Ls_low * dz0_imp / dt
        if ((self.kf_low * self.Rf + 0.5 * dz0_imp) == 0):
            self.segregation_flux = 0
        else:
            self.segregation_flux = self.Lw * (self.SP_low / 1000000) * (self.Tf - self.Ts) / (self.kf_low * self.Rf + 0.5 * dz0_imp)

    def add_results_to_output_containers(self, dt, dz0_imp):
        self.time_output = np.append(self.time_output, self.current_hour_count / 24)
        self.dt_output = np.append(self.dt_output, dt)
        self.hours_output = np.append(self.hours_output, self.current_hour_count)
        self.closest_interface_output = np.append(self.closest_interface_output, self.closest_interface)
        self.FI_output = np.append(self.FI_output, self.FI)
        self.Ts_output = np.append(self.Ts_output, self.Ts)
        self.ku_output = np.append(self.ku_output, self.ku_low)
        self.kf_output = np.append(self.kf_output, self.kf_low)
        self.SP_output = np.append(self.SP_output, self.SP_low)
        self.a_output = np.append(self.a_output, self.a_low)
        self.Ls_output = np.append(self.Ls_output, self.Ls_low)
        self.S_output = np.append(self.S_output, self.S)
        self.Sr_output = np.append(self.Sr_output, self.Sr_low)
        self.Rf_output = np.append(self.Rf_output, self.Rf)
        self.dz0_imp_output = np.append(self.dz0_imp_output, dz0_imp)
        self.imp_1_vs_exp_0_output = np.append(self.imp_1_vs_exp_0_output, self.imp_vs_exp)
        self.dz0_sum_output = np.append(self.dz0_sum_output, self.dz0_sum)
        self.dh0_output = np.append(self.dh0_output, self.dh0)
        self.dh0_sum_output = np.append(self.dh0_sum_output, self.dh0_sum)
        self.dhs_output = np.append(self.dhs_output, self.dhs)
        self.dhs_sum_output = np.append(self.dhs_sum_output, self.dhs_sum)
        self.dh_output = np.append(self.dh_output, self.dh)
        self.h_output = np.append(self.h_output, self.h)
        self.dz_output = np.append(self.dz_output, self.dz)
        self.z_output = np.append(self.z_output, self.z)
        self.idx_output = np.append(self.idx_output, self.idx_low)
        self.gradT_p_output = np.append(self.gradT_p_output, self.gradT_p)
        self.flux_output = np.append(self.flux_output, self.flux)
        self.Cq_output = np.append(self.Cq_output, self.Cq)
        self.root_1_output = np.append(self.root_1_output, self.root_1)
        self.root_2_output = np.append(self.root_2_output, self.root_2)
        self.pos_flux_output = np.append(self.pos_flux_output, self.pos_flux)
        self.neg_flux_output = np.append(self.neg_flux_output, self.neg_flux)
        self.freeze_water_flux_output = np.append(self.freeze_water_flux_output, self.freeze_water_flux)
        self.segregation_flux_output = np.append(self.segregation_flux_output, self.segregation_flux)

    def create_final_data_set(self):
        array = np.column_stack((self.time_output,
                                 self.dt_output, self.hours_output, self.closest_interface_output,
                                 self.FI_output, self.Ts_output, self.ku_output,
                                 self.kf_output, self.SP_output, self.a_output,
                                 self.Ls_output, self.S_output, self.Sr_output,
                                 self.Rf_output, self.dz0_imp_output, self.imp_1_vs_exp_0_output,
                                 self.dz0_sum_output, self.dh0_output, self.dh0_sum_output,
                                 self.dhs_output, self.dhs_sum_output, self.dh_output,
                                 self.h_output, self.dz_output, self.z_output,
                                 self.idx_output, self.gradT_p_output, self.flux_output, self.Cq_output,
                                 self.root_1_output, self.root_2_output, self.pos_flux_output,
                                 self.neg_flux_output, self.freeze_water_flux_output, self.segregation_flux_output))

        self.array_df = pd.DataFrame(array,
                                     columns=['day', 'dt', 'hours', 'closest_int',
                                              'FI', 'Ts', 'ku',
                                              'kf', 'SP', 'a',
                                              'Ls', 'S', 'Sr',
                                              'Rf', 'dz0_imp', 'imp_1_vs_exp_0',
                                              'dz0_sum', 'dh0', 'dh0_sum',
                                              'dhs', 'dhs_sum', 'dh',
                                              'h', 'dz', 'z',
                                              'idx', 'gradT_p', 'flux', 'Cq',
                                              'root_1', 'root_2', 'pos_flux',
                                              'neg_flux', 'wat_flux', 'seg_flux'])

        #self.array_df.to_excel(self.excel_file_name, engine='xlsxwriter')

    def figure_1(self):
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

        fig = plt.figure(figsize=(14, 6), dpi=100)
        ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax1.set_title(self.figure_label_1, size=14)
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
        ax1.set_xlabel('Days', size=12)
        ax1.set_ylim([-0.10, y_lim + 0.5])
        ax1.set_ylabel('Frost depth, m', size=12)
        for axis in ['top', 'bottom', 'left', 'right']:
            ax1.spines[axis].set_linewidth(1.5)
        ax1.tick_params(axis='both', direction='in', width=1.5, right=True, top=True)
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
        ax2.tick_params(axis='both', direction='in', width=1.5, right=True, top=True)
        ax2.set_ylabel('Temperature, °C', size=12)

        if plot5 == None:
            #plots = plot1 + plot2 + plot3 + plot4
            plots = plot1 + plot2 + plot4
        else:
            #plots = plot1 + plot2 + plot3 + plot4 + plot5
            plots = plot1 + plot2 + plot4 + plot5
        labels = [l.get_label() for l in plots]
        ax1.legend(plots, labels, loc='lower left', edgecolor='black')

        fig.savefig(self.figure_file_name_1, dpi=200)
        plt.close()

    def figure_2(self):
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

        fig = plt.figure(figsize=(8, 6), dpi=100)
        ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax1.set_title(self.figure_label_2, size=14)
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

        fig.savefig(self.figure_file_name_2, dpi=200)
        plt.close()

    def SSR_calculate_single_test_case(self):
        #file_location = r"01_SAAR_original_data_set\\"
        #filename = "01_SSR_Alajarvi"

        #input_prefix = r"data_input\\"
        #output_prefix = r"data_output\\"

        #full_testsite_filename_vector = []
        #output_filename_vector = []

        #output_filename_vector.append(filename)
        #output_filename_vector.append(input_prefix + file_location)
        #output_filename_vector.append(output_prefix + file_location)

        #full_testsite_filename_vector.append(output_filename_vector)

        #for i in full_testsite_filename_vector:
        #    print("STARTING2 FOR: {}".format(i[2] + i[0]))

        print('START')
        dt = 0
        dz0 = 0
        partial_time_step = 0
        step_count = 1
        while self.current_hour_count < self.total_test_time:
            self.set_index()
            if self.check_for_close_interface():
                self.set_index()

            if partial_time_step != 0:
                dt = self.set_partial_time_step(partial_time_step)
            else:
                dt = self.set_full_step_dt()

            self.set_temp()
            self.set_S()
            self.set_layer_props()
            self.set_resistance()

            dz0_imp = self.calculate_dz0_imp(dt)

            if self.interface_check(dz0_imp):
                self.decrement_current_hour_count(dt)
                dz0_imp = self.calculate_dz0_residual()
                dt = self.calculate_dt(dz0_imp)
                self.increment_current_hour_count(dt)
                partial_time_step = self.increment_partial_time_step(partial_time_step, dt)
            else:
                partial_time_step = 0
                self.adjust_current_hour_count()
            self.calculate_FI(dt)
            self.calculate_step_increments(dt, dz0_imp)
            self.calculate_balance_flux(dt, dz0_imp)
            self.add_results_to_output_containers(dt, dz0_imp)
            step_count += 1
        self.create_final_data_set()
        #self.figure_1()
        #self.figure_2()
        print('FINISH')
        #print("FINISHING FOR: {}".format(i[2] + i[0]))

        return (self.array_df, self.interface_lim_list, self.chaussee_file_chau_z_list, self.chaussee_file_day_list,
                self.site_file_day_list, self.site_file_site_z_list, self.layer_count, self.chaussee_file_chau_h_list,
                self.site_file_site_h_list)


def load_all_files():
    #file_location_1 = r"01_SAAR_original_data_set\\"
    #file_location_2 = r"02_QUEB_with_default_parameters\\"
    #file_location_3 = r"03_QUEB_with_given_parameters\\"
    #file_location_4 = r"04_QUEB_with_backcalculated_values\\"
    file_location_5 = r"05_ROROS_data_set\\"

    file_location_vector = []
    #file_location_vector.append(file_location_1)
    #file_location_vector.append(file_location_2)
    #file_location_vector.append(file_location_3)
    #file_location_vector.append(file_location_4)
    file_location_vector.append(file_location_5)

    input_prefix = r"data_input\\"
    output_prefix = r"data_output\\"
    filenames_file = r"filenames.csv"

    full_testsite_filename_vector = []

    for i in file_location_vector:
        filenames = input_prefix + i + filenames_file
        import_filenames = pd.read_csv(filenames, header=None)
        for j in import_filenames[0]:
            output_filename_vector = []
            output_filename_vector.append(j)                            # file name
            output_filename_vector.append(input_prefix + i)             # input folder name
            output_filename_vector.append(output_prefix + i)            # output folder name
            full_testsite_filename_vector.append(output_filename_vector)

    return full_testsite_filename_vector

def SSR_calculate_full_data_set():
    full_testsite_filename_vector = load_all_files()
    for i in full_testsite_filename_vector:
        print("STARTING FOR: {}".format(i[2] + i[0]))
        test_site = SSR_model(i[0], i[1], i[2])
        dt = 0
        dz0 = 0
        partial_time_step = 0
        while test_site.current_hour_count < test_site.total_test_time:
            test_site.set_index()
            if test_site.check_for_close_interface():
                test_site.set_index()

            if partial_time_step != 0:
                dt = test_site.set_partial_time_step(partial_time_step)
            else:
                dt = test_site.set_full_step_dt()

            test_site.set_temp()
            test_site.set_S()
            test_site.set_layer_props()
            test_site.set_resistance()

            dz0_imp = test_site.calculate_dz0_imp(dt)

            if test_site.interface_check(dz0_imp):
                test_site.decrement_current_hour_count(dt)
                dz0_imp = test_site.calculate_dz0_residual()
                dt = test_site.calculate_dt(dz0_imp)
                test_site.increment_current_hour_count(dt)
                partial_time_step = test_site.increment_partial_time_step(partial_time_step, dt)
            else:
                partial_time_step = 0
                test_site.adjust_current_hour_count()
            test_site.calculate_FI(dt)
            test_site.calculate_step_increments(dt, dz0_imp)
            test_site.calculate_balance_flux(dt, dz0_imp)
            test_site.add_results_to_output_containers(dt, dz0_imp)
        test_site.create_final_data_set()
        test_site.figure_1()
        test_site.figure_2()
        print("FINISHING FOR: {}".format(i[2] + i[0]))

def SSR_calculate_single_test_case():
    file_location = r"01_SAAR_original_data_set\\"
    filename = "01_SSR_Alajarvi"

    input_prefix = r"data_input\\"
    output_prefix = r"data_output\\"

    full_testsite_filename_vector = []
    output_filename_vector = []

    output_filename_vector.append(filename)
    output_filename_vector.append(input_prefix + file_location)
    output_filename_vector.append(output_prefix + file_location)

    full_testsite_filename_vector.append(output_filename_vector)

    for i in full_testsite_filename_vector:
        print("STARTING FOR: {}".format(i[2] + i[0]))
        test_site = SSR_model(i[0], i[1], i[2])
        dt = 0
        dz0 = 0
        partial_time_step = 0
        step_count = 1
        while test_site.current_hour_count < test_site.total_test_time:
            test_site.set_index()
            if test_site.check_for_close_interface():
                test_site.set_index()

            if partial_time_step != 0:
                dt = test_site.set_partial_time_step(partial_time_step)
            else:
                dt = test_site.set_full_step_dt()

            test_site.set_temp()
            test_site.set_S()
            test_site.set_layer_props()
            test_site.set_resistance()

            dz0_imp = test_site.calculate_dz0_imp(dt)

            if test_site.interface_check(dz0_imp):
                test_site.decrement_current_hour_count(dt)
                dz0_imp = test_site.calculate_dz0_residual()
                dt = test_site.calculate_dt(dz0_imp)
                test_site.increment_current_hour_count(dt)
                partial_time_step = test_site.increment_partial_time_step(partial_time_step, dt)
            else:
                partial_time_step = 0
                test_site.adjust_current_hour_count()
            test_site.calculate_FI(dt)
            test_site.calculate_step_increments(dt, dz0_imp)
            test_site.calculate_balance_flux(dt, dz0_imp)
            test_site.add_results_to_output_containers(dt, dz0_imp)
            step_count += 1
        test_site.create_final_data_set()
        test_site.figure_1()
        test_site.figure_2()
        print("FINISHING FOR: {}".format(i[2] + i[0]))

#SSR_calculate_full_data_set()
#SSR_calculate_single_test_case()