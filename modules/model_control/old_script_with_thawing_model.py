import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import fsolve
import os
import glob


class FL_calc:
    def __init__(self, filename):
        self.filename = filename
        self.df_layer_props = pd.read_excel(self.filename, sheet_name='layers')
        self.df_data = pd.read_excel(self.filename, sheet_name='data')
        self.df_other = pd.read_excel(self.filename, sheet_name='other').to_numpy()

    def set_filenames(self):
        self.excel_file_name = self.filename[:-5] + '_df' + '.xlsx'
        self.figure_label_1 = self.filename[3:-5]
        self.figure_label_2 = self.filename[3:-5]
        self.figure_file_name_1 = self.filename[:-5] + '_fig_1' + '.png'
        self.figure_file_name_2 = self.filename[:-5] + '_fig_2' + '.png'

    def set_limit_counts(self):
        self.layer_count = self.df_layer_props['ku'].count()

        self.days = self.df_data['day'].count()
        self.time = self.days * 24

        self.layer_height_list = list(self.df_layer_props.iloc[0:self.layer_count - 1, 1])
        self.layer_height_list.append(10)
        self.layer_height_list_mod = self.layer_height_list.copy()
        self.lim_list = list(np.cumsum(self.layer_height_list))

    def set_parameter_lists(self):
        self.day_list = self.df_data['day'].tolist()
        self.temps_list = self.df_data['temps'].to_list()
        self.chau_z_list = self.df_data['chau_z'].tolist()
        self.chau_h_list = self.df_data['chau_h'].tolist()
        self.site_z_list = self.df_data['site_z'].tolist()
        self.S_vals_list = self.df_data['S_vals'].tolist()

        self.ku_list = list(self.df_layer_props.iloc[0:self.layer_count, 2])
        self.kf_list = list(self.df_layer_props.iloc[0:self.layer_count, 3])
        self.SP_list = list(self.df_layer_props.iloc[0:self.layer_count, 4])
        self.a_list = list(self.df_layer_props.iloc[0:self.layer_count, 5])
        self.Sr_list = list(self.df_layer_props.iloc[0:self.layer_count, 6])
        self.Ls_list = list(self.df_layer_props.iloc[0:self.layer_count, 7])
        self.w_list = list(self.df_layer_props.iloc[0:self.layer_count, 8])
        self.rhod_list = list(self.df_layer_props.iloc[0:self.layer_count, 9])

    def set_other_inputs(self):
        self.flag = self.df_other[0][1]
        self.xps = self.df_other[1][1]
        self.Tma = self.df_other[2][1]
        self.lim = self.df_other[3][1]

    def set_arrays(self):
        self.time_arr = np.array([])
        self.hours_arr = np.array([])
        self.FI_arr = np.array([])
        self.Ts_arr = np.array([])
        self.ku_arr = np.array([])
        self.kf_arr = np.array([])
        self.SP_arr = np.array([])
        self.a_arr = np.array([])
        self.Ls_arr = np.array([])
        self.S_arr = np.array([])
        self.Sr_arr = np.array([])
        self.Rf_arr = np.array([])
        self.dz0_arr = np.array([])
        self.dz0_exp_arr = np.array([])
        self.dz0_sum_arr = np.array([])
        self.dh0_arr = np.array([])
        self.dh0_sum_arr = np.array([])
        self.dhs_arr = np.array([])
        self.dhs_sum_arr = np.array([])
        self.dh_arr = np.array([])
        self.h_arr = np.array([])
        self.dz_arr = np.array([])
        self.z_arr = np.array([])
        self.idx_arr = np.array([])
        self.flux_arr = np.array([])

        self.dz0_upper_arr = np.array([])
        self.dz0_upper_sum_arr = np.array([])

    def add_to_arrays(self):
        self.time_arr = np.array([])
        self.hours_arr = np.array([])
        self.FI_arr = np.array([])
        self.Ts_arr = np.array([])
        self.ku_arr = np.array([])
        self.kf_arr = np.array([])
        self.SP_arr = np.array([])
        self.a_arr = np.array([])
        self.Ls_arr = np.array([])
        self.S_arr = np.array([])
        self.Sr_arr = np.array([])
        self.Rf_arr = np.array([])
        self.dz0_arr = np.array([])
        self.dz0_exp_arr = np.array([])
        self.dz0_sum_arr = np.array([])
        self.dh0_arr = np.array([])
        self.dh0_sum_arr = np.array([])
        self.dhs_arr = np.array([])
        self.dhs_sum_arr = np.array([])
        self.dh_arr = np.array([])
        self.h_arr = np.array([])
        self.dz_arr = np.array([])
        self.z_arr = np.array([])
        self.idx_arr = np.array([])
        self.flux_arr = np.array([])

        self.dz0_upper_arr = np.array([])
        self.dz0_upper_sum_arr = np.array([])

    def calculation(self):
        """ the function calculates total frost penetration for a given time parameter """

        ki = 2.18
        Tf = 0
        Lw = 92500
        rhow = 1
        gradT_p = 2

        z = 0
        dz0_sum = 0.01
        dh0_sum = 0
        dhs_sum = 0
        h = 0
        minutes_count = 0
        hours_count = 0
        FI = 0

        dz0_upper = 0
        dz0_upper_sum = 0

        while hours_count < self.time:

            if dz0_sum < 0.05:
                ddt = 1
            elif minutes_count % 60 != 0:
                ddt = 1
            else:
                ddt = 60

            dt = ddt/60
            minutes_count += ddt
            hours_count = minutes_count / 60
            days_count = hours_count/24
            day_index = math.ceil(days_count)-1
            day = math.ceil(days_count)

            Ts = self.temps_list[day_index]
            S = self.S_vals_list[day_index]

            if Ts <=0:

                if dz0_sum < self.lim:
                    Cq = 10**(-4.5*self.xps**0.8)
                else:
                    Cq = 1.0
                flux = (((250-day)*(9.62+1.44*math.log(self.Tma)) / ((250 + (5.78-1.62*math.log(self.Tma)))*day))+1.2)*Cq

                def find_nearest(array, value):
                    array = np.asarray(array)
                    idx = (np.abs(array - value)).argmin()
                    return array[idx]

                nearest = find_nearest(self.lim_list, dz0_sum)
                if dz0_sum <= nearest:
                    idx = self.lim_list.index(nearest)
                else:
                    idx = self.lim_list.index(nearest) + 1

                ku = self.ku_list[idx]
                kf = self.kf_list[idx]
                a = self.a_list[idx]
                SP = self.SP_list[idx] * math.exp(-a * 0.02 * z)
                Sr = self.Sr_list[idx]
                Ls = self.Ls_list[idx]
                w_vol = self.w_list[idx]
                rhod = self.rhod_list[idx]


                res_1 = 0
                for i in range(idx):
                    res_1 += self.layer_height_list_mod[i]/self.kf_list[i]
                res_2 = (self.layer_height_list_mod[idx] - (sum(self.layer_height_list[0:idx+1]) - dz0_sum)) / kf
                res_3 = dhs_sum/ki
                Rf = res_1 + res_2 + res_3

                dz0 = ((Tf - Ts) * dt * (1 - SP/1000000 * Lw / kf)) / (Ls * Rf) - S*gradT_p*ku* dt / Ls

                #########################################################################################################
                ########################################### ALTERNATIVE  dz0  ###########################################
                #########################################################################################################

                def func(dz0_exp):
                    f = ku*gradT_p*S+Ls*dz0_exp/dt+Lw*SP/1000000*Ts/(Rf+0.5*dz0_exp/kf)-(Tf-Ts)/(Rf+0.5*dz0_exp/kf)
                    return f
                # dz0_exp = fsolve(func, np.array(0.1))[0]
                dz0_exp = 1

                #########################################################################################################
                #########################################################################################################
                #########################################################################################################

                if dz0 <= 0:
                    dh0 = 0
                    dhs = 0
                    dh = dh0 + dhs
                    h += dh
                    dz = dz0 + dh
                    z += dz
                    dz0_sum += dz0
                    dh0_sum += dh0
                    dhs_sum += dhs
                    if dz0_sum < 0.01:
                        dz0_sum = 0.01
                        z = 0
                else:
                    if self.Sr_list[idx] <= 85:
                        dh0 = 0
                    else:
                        dh0 = (dz0 * 0.09 * w_vol/100*rhod/rhow) * (Sr-85)/15
                    self.layer_height_list_mod[idx] += dh0

                    dhs = (1.09 * SP/1000000 * (Tf - Ts) * dt) / (kf * Rf)
                    dh = dh0 + dhs
                    h += dh

                    dz = dz0 + dh
                    z += dz

                    dz0_sum += dz0
                    dh0_sum += dh0
                    dhs_sum += dhs

                flag = days_count.is_integer()
                if flag == True:
                    FL_frost_list.append(z)
                    FL_heave_list.append(h)
                    index = int(days_count - 1)
                    value_site_z = self.df_data.iloc[index, 5]
                    if not math.isnan(value_site_z):
                        CHAU_frost_list.append(self.df_data.iloc[index, 3])
                        SITE_frost_list.append(value_site_z)
                    value_site_h = self.df_data.iloc[index, 6]
                    if not math.isnan(value_site_h):
                        CHAU_frost_list.append(self.df_data.iloc[index, 4])
                        SITE_frost_list.append(value_site_h)

                if Ts < 0:
                    FI += dt * Ts * -1
                else:
                    FI = FI

                self.time_arr = np.append(self.time_arr, hours_count / 24)
                self.hours_arr = np.append(self.hours_arr, hours_count)
                self.FI_arr = np.append(self.FI_arr, FI)
                self.Ts_arr = np.append(self.Ts_arr, Ts)
                self.ku_arr = np.append(self.ku_arr, ku)
                self.kf_arr = np.append(self.kf_arr, kf)
                self.SP_arr = np.append(self.SP_arr, SP)
                self.a_arr = np.append(self.a_arr, a)
                self.Ls_arr = np.append(self.Ls_arr, Ls)
                self.S_arr = np.append(self.S_arr, S)
                self.Sr_arr = np.append(self.Sr_arr, Sr)
                self.Rf_arr = np.append(self.Rf_arr, Rf)
                self.dz0_arr = np.append(self.dz0_arr, dz0)
                self.dz0_exp_arr = np.append(self.dz0_exp_arr, dz0_exp)
                self.dz0_sum_arr = np.append(self.dz0_sum_arr, dz0_sum)
                self.dh0_arr = np.append(self.dh0_arr, dh0)
                self.dh0_sum_arr = np.append(self.dh0_sum_arr, dh0_sum)
                self.dhs_arr = np.append(self.dhs_arr, dhs)
                self.dhs_sum_arr = np.append(self.dhs_sum_arr, dhs_sum)
                self.dh_arr = np.append(self.dh_arr, dh)
                self.h_arr = np.append(self.h_arr, h)
                self.dz_arr = np.append(self.dz_arr, dz)
                self.z_arr = np.append(self.z_arr, z)
                self.idx_arr = np.append(self.idx_arr, idx)
                self.flux_arr = np.append(self.flux_arr, flux)

                dz0_upper = 0
                self.dz0_upper_arr = np.append(self.dz0_upper_arr, dz0_upper)
                self.dz0_upper_sum_arr = np.append(self.dz0_upper_sum_arr, float('NaN'))

            elif Ts > 0 and dz0_upper_sum <= dz0_sum:
                ##### Definign upper position ##########################################################################
                def find_nearest(array, value):
                    array = np.asarray(array)
                    idx = (np.abs(array - value)).argmin()
                    return array[idx]

                nearest = find_nearest(self.lim_list, dz0_upper)
                if dz0_sum <= nearest:
                    idx_upper = self.lim_list.index(nearest)
                else:
                    idx_upper = self.lim_list.index(nearest) + 1

                ##### Defining lower position ##########################################################################
                def find_nearest(array, value):
                    array = np.asarray(array)
                    idx = (np.abs(array - value)).argmin()
                    return array[idx]

                nearest = find_nearest(self.lim_list, dz0_sum)
                if dz0_sum <= nearest:
                    idx_lower = self.lim_list.index(nearest)
                else:
                    idx_lower = self.lim_list.index(nearest) + 1

                ##### Getting upper parameters #########################################################################
                ku_upp = self.ku_list[idx_upper]
                Ls_upp = self.Ls_list[idx_upper]

                ##### Getting lower parameters #########################################################################
                ku_low = self.ku_list[idx_lower]
                kf_low = self.kf_list[idx_lower]
                a_low = self.a_list[idx_lower]
                SP_low = self.SP_list[idx_lower] * math.exp(-a_low * 0.02 * z)
                Sr_low = self.Sr_list[idx_lower]
                Ls_low = self.Ls_list[idx_lower]
                w_vol_low = self.w_list[idx_lower]
                rhod_low = self.rhod_list[idx_lower]


                ##### Defing upper resistance ##########################################################################
                res_1_upp = 0
                for i in range(idx_upper):
                    res_1_upp += self.layer_height_list_mod[i] / self.ku_list[i]
                res_2_upp = (self.layer_height_list[idx_upper] - (sum(self.layer_height_list[0:idx_upper + 1]) - dz0_upper_sum)) / ku_upp
                Rf_upp = res_1_upp + res_2_upp

                ##### Defing lower resistance ##########################################################################
                Rf_low = 0


                ##### Calculating upper dz0 ############################################################################
                def upper_front(dz0_upper):
                    f = (Tf - Ts) / (Rf_upp + 0.5 * dz0_upper / ku_upp) - Ls_upp * 0.5 * dz0_upper / dt
                    return f
                dz0_upper = fsolve(upper_front, np.array(0.1))[0]*-1

                ##### Calculating lower dz0 ############################################################################
                dz0 = ku_low*gradT_p*S*dt/Ls_low *-1


                ##### Post calculation #################################################################################

                if Ts < 0:
                    FI += dt * Ts * -1
                else:
                    FI = FI

                dh0 = 0
                dhs = 0
                dh = dh0 + dhs
                h += dh

                dz = dz0 + dh
                z += dz

                dz0_sum += dz0
                dh0_sum += dh0
                dhs_sum += dhs

                dz0_upper_sum += dz0_upper

                dz0_exp = 1
                flux = 1

                self.time_arr = np.append(self.time_arr, hours_count / 24)
                self.hours_arr = np.append(self.hours_arr, hours_count)
                self.FI_arr = np.append(self.FI_arr, FI)
                self.Ts_arr = np.append(self.Ts_arr, Ts)
                self.ku_arr = np.append(self.ku_arr, ku_low)
                self.kf_arr = np.append(self.kf_arr, kf_low)
                self.SP_arr = np.append(self.SP_arr, SP_low)
                self.a_arr = np.append(self.a_arr, a_low)
                self.Ls_arr = np.append(self.Ls_arr, Ls_low)
                self.S_arr = np.append(self.S_arr, S)
                self.Sr_arr = np.append(self.Sr_arr, Sr_low)
                self.Rf_arr = np.append(self.Rf_arr, Rf_low)
                self.dz0_arr = np.append(self.dz0_arr, dz0)
                self.dz0_exp_arr = np.append(self.dz0_exp_arr, dz0_exp)
                self.dz0_sum_arr = np.append(self.dz0_sum_arr, dz0_sum)
                self.dh0_arr = np.append(self.dh0_arr, dh0)
                self.dh0_sum_arr = np.append(self.dh0_sum_arr, dh0_sum)
                self.dhs_arr = np.append(self.dhs_arr, dhs)
                self.dhs_sum_arr = np.append(self.dhs_sum_arr, dhs_sum)
                self.dh_arr = np.append(self.dh_arr, dh)
                self.h_arr = np.append(self.h_arr, h)
                self.dz_arr = np.append(self.dz_arr, dz)
                self.z_arr = np.append(self.z_arr, z)
                self.idx_arr = np.append(self.idx_arr, idx_lower)
                self.flux_arr = np.append(self.flux_arr, flux)


                self.dz0_upper_arr = np.append(self.dz0_upper_arr, dz0_upper)
                self.dz0_upper_sum_arr = np.append(self.dz0_upper_sum_arr, dz0_upper_sum)

            else:
                self.time_arr = np.append(self.time_arr, hours_count / 24)
                self.hours_arr = np.append(self.hours_arr, hours_count)
                self.FI_arr = np.append(self.FI_arr, 0)
                self.Ts_arr = np.append(self.Ts_arr, Ts)
                self.ku_arr = np.append(self.ku_arr, 0)
                self.kf_arr = np.append(self.kf_arr, 0)
                self.SP_arr = np.append(self.SP_arr, 0)
                self.a_arr = np.append(self.a_arr, 0)
                self.Ls_arr = np.append(self.Ls_arr, 0)
                self.S_arr = np.append(self.S_arr, 0)
                self.Sr_arr = np.append(self.Sr_arr, 0)
                self.Rf_arr = np.append(self.Rf_arr, 0)
                self.dz0_arr = np.append(self.dz0_arr, 0)
                self.dz0_exp_arr = np.append(self.dz0_exp_arr, 0)
                self.dz0_sum_arr = np.append(self.dz0_sum_arr, 0)
                self.dh0_arr = np.append(self.dh0_arr, 0)
                self.dh0_sum_arr = np.append(self.dh0_sum_arr, 0)
                self.dhs_arr = np.append(self.dhs_arr, 0)
                self.dhs_sum_arr = np.append(self.dhs_sum_arr, 0)
                self.dh_arr = np.append(self.dh_arr, 0)
                self.h_arr = np.append(self.h_arr, 0)
                self.dz_arr = np.append(self.dz_arr, 0)
                self.z_arr = np.append(self.z_arr, float('NaN'))
                self.idx_arr = np.append(self.idx_arr, 0)
                self.flux_arr = np.append(self.flux_arr, 0)

                self.dz0_upper_arr = np.append(self.dz0_upper_arr, 0)
                self.dz0_upper_sum_arr = np.append(self.dz0_upper_sum_arr, float('NaN'))






        array = np.column_stack((self.time_arr, self.hours_arr, self.FI_arr, self.Ts_arr, self.ku_arr, self.kf_arr,
                                 self.SP_arr, self.a_arr, self.Ls_arr, self.S_arr, self.Sr_arr, self.Rf_arr,
                                 self.dz0_arr, self.dz0_exp_arr, self.dz0_sum_arr, self.dh0_arr, self.dh0_sum_arr,
                                 self.dhs_arr, self.dhs_sum_arr, self.dh_arr, self.h_arr, self.dz_arr, self.z_arr,
                                 self.idx_arr, self.flux_arr, self.dz0_upper_arr, self.dz0_upper_sum_arr))

        self.array_df = pd.DataFrame(array[:, 1:], index=array[:, 0],
                                     columns=['hours', 'FI', 'Ts', 'ku', 'kf', 'SP', 'a', 'Ls', 'S', 'Sr', 'Rf', 'dz0',
                                              'dz0_exp', 'dz0_sum', 'dh0', 'dh0_sum', 'dhs', 'dhs_sum', 'dh', 'h', 'dz',
                                              'z', 'idx', 'flux', 'dz0_upper', 'dz0_upper_sum'])

        self.array_df.to_excel(self.excel_file_name, engine='xlsxwriter')

        return self.array_df

    def figure_1(self):
        fig = plt.figure(figsize=(8,6), dpi=100)
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        axes.set_title(self.figure_label_1, size=14)
        axes.plot(self.array_df.index.values, self.array_df['z'], label='frost penetration', color='#948B3d', lw=2)
        axes.plot(self.array_df.index.values, self.array_df['dz0_upper_sum'], label='frost penetration', color='red', lw=2)
        axes.plot(self.df_data['day'], self.df_data['chau_z'])
        axes.plot(self.df_data['day'], self.df_data['site_z'], marker='+', ms=6, mew=1.5,)
        axes.legend(loc="upper right")

        for i in range(self.layer_count-1):
            axes.plot([0, self.days], [self.lim_list[i], self.lim_list[i]], lw=0.5, ls='--', color='black')
        axes.set_xlim([-5, self.days+5])
        axes.set_ylim([-0.05, self.lim_list[-2]+2])
        axes.set_xticks([0, 20, 40, 60, 80, 100, 120, 140, 160, 180])
        axes.set_xlabel('Days', size=12)
        axes.set_ylabel('Frost front, m', size=12)
        axes.invert_yaxis()
        for axis in ['top', 'bottom', 'left', 'right']:
            axes.spines[axis].set_linewidth(1.5)
        axes.tick_params(axis='both', direction='in', width=1.5, right=True, top=True)
        fig.savefig(self.figure_file_name_1, dpi=200)
        plt.show()

    def figure_2(self):
        fig = plt.figure(figsize=(8,6), dpi=100)
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        axes.set_title(self.figure_label_2, size=14)
        axes.plot(self.array_df.index.values, self.array_df['h']*np.array(1000), label='frost heave',
                  lw=2, color='#948B3d')
        axes.plot(self.df_data['day'], self.df_data['chau_h'], lw=2)
        axes.legend(loc="upper right")
        axes.set_xlim([-5, self.days+5])
        axes.set_ylim([-20, 220])
        axes.set_xticks([0, 20, 40, 60, 80, 100, 120, 140, 160, 180])
        axes.set_yticks([0, 25, 50, 75, 100, 125, 150, 175, 200])
        axes.set_xlabel('Days', size=12)
        axes.set_ylabel('Frost heave, mm', size=12)
        for axis in ['top', 'bottom', 'left', 'right']:
            axes.spines[axis].set_linewidth(1.5)
        axes.tick_params(axis='both', direction='in', width=1.5, right=True, top=True)
        fig.savefig(self.figure_file_name_2, dpi=200)
        plt.show()

    def figure_3(self):
        fig = plt.figure(figsize=(8, 6), dpi=100)
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        axes.set_title('Temperature', size=14)
        axes.plot(self.array_df.index.values, self.array_df['Ts'], label='Temperature',
                  lw=2, color='#948B3d')
        axes.plot([0, 180], [0, 0])
        axes.legend(loc="upper right")
        axes.set_xlim([-5, self.days + 5])
        #axes.set_ylim([-20, 220])
        axes.set_xticks([0, 20, 40, 60, 80, 100, 120, 140, 160, 180])
        #axes.set_yticks([0, 25, 50, 75, 100, 125, 150, 175, 200])
        axes.set_xlabel('Days', size=12)
        axes.set_ylabel('Temperature, degC', size=12)
        for axis in ['top', 'bottom', 'left', 'right']:
            axes.spines[axis].set_linewidth(1.5)
        axes.tick_params(axis='both', direction='in', width=1.5, right=True, top=True)
        #fig.savefig(self.figure_file_name_2, dpi=200)
        plt.show()


class Comparison:
    def __init__(self):
        fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(16, 8))

        axes[0, 0].plot(CHAU_frost_list, SITE_frost_list, marker='o', ms=2, mfc='darkblue')
        axes[0, 0].plot([0, 0], [3, 3], ls='-', lw=2, color='black')
        axes[0, 0].plot([0, 0.15], [2.85, 3], ls='dotted', lw=1, color='black')
        axes[0, 0].plot([0, 0.15], [2.85, 3], ls='dotted', lw=1, color='black')
        for axis in ['top', 'bottom', 'left', 'right']:
            axes[0, 0].spines[axis].set_linewidth(1.5)
        axes[0, 0].set_title("Frost depth \n(Chaussee vs. measurements")
        axes[0, 0].set_xlabel('Predicted (Chaussee) frost depth, m', size=12)
        axes[0, 0].set_ylabel('Measured frost depth, m', size=12)
        axes[0, 0].set_xlim([0, 3])
        axes[0, 0].set_ylim([0, 3])
        axes[0, 0].set_xticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
        axes[0, 0].set_yticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
        axes[0, 0].tick_params(axis='both', direction='in', width=1.5, right=True, top=True)

        axes[0, 1].plot(FL_frost_list, SITE_frost_list, marker='o', ms=2, mfc='darkblue')
        axes[0, 1].plot([0, 0], [3, 3], ls='-', lw=2, color='black')
        axes[0, 1].plot([0, 0.15], [2.85, 3], ls='dotted', lw=1, color='black')
        axes[0, 1].plot([0, 0.15], [2.85, 3], ls='dotted', lw=1, color='black')
        for axis in ['top', 'bottom', 'left', 'right']:
            axes[0, 1].spines[axis].set_linewidth(1.5)
        axes[0, 1].set_title("Frost depth \n(Frost Lite vs. measurements")
        axes[0, 1].set_xlabel('Predicted (Frost Lite) frost depth, m', size=12)
        axes[0, 1].set_ylabel('Measured frost depth, m', size=12)
        axes[0, 1].set_xlim([0, 3])
        axes[0, 1].set_ylim([1, 3])
        axes[0, 1].set_xticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
        axes[0, 1].set_yticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
        axes[0, 1].tick_params(axis='both', direction='in', width=1.5, right=True, top=True)

        axes[0, 2].plot(FL_frost_list, CHAU_frost_list, marker='o', ms=2, mfc='darkblue')
        axes[0, 2].plot([0, 0], [3, 3], ls='-', lw=2, color='black')
        axes[0, 2].plot([0, 0.15], [2.85, 3], ls='dotted', lw=1, color='black')
        axes[0, 2].plot([0, 0.15], [2.85, 3], ls='dotted', lw=1, color='black')
        for axis in ['top', 'bottom', 'left', 'right']:
            axes[0, 2].spines[axis].set_linewidth(1.5)
        axes[0, 2].set_title("Frost depth \n(Frost Lite vs. Chaussee")
        axes[0, 2].set_xlabel('Predicted (Frost Lite) frost depth, m', size=12)
        axes[0, 2].set_ylabel('Predicted (Chaussee) frost depth, m', size=12)
        axes[0, 2].set_xlim([0, 3])
        axes[0, 2].set_ylim([1, 3])
        axes[0, 2].set_xticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
        axes[0, 2].set_yticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
        axes[0, 2].tick_params(axis='both', direction='in', width=1.5, right=True, top=True)

        axes[1, 0].plot(CHAU_heave_list, SITE_heave_list, marker='o', ms=2, mfc='darkblue')
        axes[1, 0].plot([0, 0], [150, 150], ls='-', lw=2, color='black')
        axes[1, 0].plot([0, 20], [130, 150], ls='dotted', lw=1, color='black')
        axes[1, 0].plot([20, 0], [150, 130], ls='dotted', lw=1, color='black')
        for axis in ['top', 'bottom', 'left', 'right']:
            axes[1, 0].spines[axis].set_linewidth(1.5)
        axes[1, 0].set_title("Frost heave \n(Chaussee vs. measurements")
        axes[1, 0].set_xlabel('Predicted (Chaussee) frost heave, mm', size=12)
        axes[1, 0].set_ylabel('Measured frost heave, mm', size=12)
        axes[1, 0].set_xlim([0, 150])
        axes[1, 0].set_ylim([0, 150])
        axes[1, 0].set_xticks([0, 30, 60, 90, 120, 150])
        axes[1, 0].set_yticks([0, 30, 60, 90, 120, 150])
        axes[1, 0].tick_params(axis='both', direction='in', width=1.5, right=True, top=True)

        axes[1, 1].plot(FL_heave_list, SITE_heave_list, marker='o', ms=2, mfc='darkblue')
        axes[1, 1].plot([0, 0], [150, 150], ls='-', lw=2, color='black')
        axes[1, 1].plot([0, 20], [130, 150], ls='dotted', lw=1, color='black')
        axes[1, 1].plot([20, 0], [150, 130], ls='dotted', lw=1, color='black')
        for axis in ['top', 'bottom', 'left', 'right']:
            axes[1, 1].spines[axis].set_linewidth(1.5)
        axes[1, 1].set_title("Frost heave \n(Frost Lite vs. measurements")
        axes[1, 1].set_xlabel('Predicted (Frost Lite) frost heave, mm', size=12)
        axes[1, 1].set_ylabel('Measured frost heave, mm', size=12)
        axes[1, 1].set_xlim([0, 4000])
        axes[1, 1].set_ylim([0, 0.5])
        axes[1, 1].set_xticks([0, 30, 60, 90, 120, 150])
        axes[1, 1].set_yticks([0, 30, 60, 90, 120, 150])
        axes[1, 1].tick_params(axis='both', direction='in', width=1.5, right=True, top=True)

        axes[1, 2].plot(FL_frost_list, CHAU_frost_list, marker='o', ms=2, mfc='darkblue')
        axes[1, 2].plot([0, 0], [150, 150], ls='-', lw=2, color='black')
        axes[1, 2].plot([0, 20], [130, 150], ls='dotted', lw=1, color='black')
        axes[1, 2].plot([20, 0], [150, 130], ls='dotted', lw=1, color='black')
        for axis in ['top', 'bottom', 'left', 'right']:
            axes[1, 2].spines[axis].set_linewidth(1.5)
        axes[1, 2].set_title("Frost heave \n(Frost Lite vs. Chaussee")
        axes[1, 2].set_xlabel('Predicted (Frost Lite) frost heave, mm', size=12)
        axes[1, 2].set_ylabel('Predicted (Chaussee) frost heave, mm', size=12)
        axes[1, 2].set_xlim([0, 150])
        axes[1, 2].set_ylim([0, 150])
        axes[1, 2].set_xticks([0, 30, 60, 90, 120, 150])
        axes[1, 2].set_yticks([0, 30, 60, 90, 120, 150])
        axes[1, 2].tick_params(axis='both', direction='in', width=1.5, right=True, top=True)

FL_frost_list = []
CHAU_frost_list = []
SITE_frost_list = []

FL_heave_list = []
CHAU_heave_list = []
SITE_heave_list = []


file_name = 'generic_test_data.xlsx'
calc_site = FL_calc(file_name)

calc_site.set_filenames()
calc_site.set_limit_counts()
calc_site.set_parameter_lists()
calc_site.set_other_inputs()
calc_site.set_arrays()
calc_site.calculation()
calc_site.figure_1()
calc_site.figure_2()
calc_site.figure_3()


#os.chdir(r'C:\Users\karlisr\OneDrive - NTNU\2_PostDoc_NTNU\1_SSR_Model_development\5_SSR_model_calculation_Chaussee_input_based_ACTIVE\1_SSR_Chaussee_input_Python_project\excel_files')
#file_list = glob.glob('*.xlsx')


#for i in file_list:
#    frost_calc = FL_calc(i)
#    df = frost_calc.calc()
#    frost_calc.figure_1()
#    frost_calc.figure_2()