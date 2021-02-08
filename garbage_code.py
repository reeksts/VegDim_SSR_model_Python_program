class AddNewMineral(tk.Tk):
    def __init__(self):
        super().__init__()
        #self.geometry("300x150")
        self.title("Add new mineral")
        self.resizable(False, False)

        # Adding container frames:
        self.background_frame = tk.Frame(self, bg='#b6cb94')
        self.background_frame.pack(side='top', fill='both', expand=True)

        self.main_frame = tk.Frame(self.background_frame, bg='#a7bf37')
        self.main_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)

        # Adding labels and entries:
        self.top_label = tk.Label(self.main_frame, text='Add new mineral', anchor='w', justify='left')
        self.mineral_name_label = tk.Label(self.main_frame, text="Name", anchor='w', justify='left', width=20)
        self.mineral_th_label = tk.Label(self.main_frame, text='Thermal conductivity', anchor='w', justify='left')
        self.mineral_rho_label = tk.Label(self.main_frame, text='Density', anchor='w', justify='left')

        self.mineral_name_entry = tk.Entry(self.main_frame, width=20)
        self.mineral_th_entry = tk.Entry(self.main_frame, width=20)
        self.mineral_rho_entry = tk.Entry(self.main_frame, width=20)

        self.mineral_th_unit_label = tk.Label(self.main_frame, text='[W/mK]', anchor='w', justify='left')
        self.mineral_rho_unit_label = tk.Label(self.main_frame, text='[g/cm3]', anchor='w', justify='left')

        # Packing labels and entries
        self.top_label.grid(row=0, column=0, columnspan=3, sticky="ew")
        self.mineral_name_label.grid(row=1, column=0, sticky='ew', pady=(5, 0))
        self.mineral_th_label.grid(row=2, column=0, sticky='ew', pady=(5, 0))
        self.mineral_rho_label.grid(row=3, column=0, sticky='ew', pady=(5, 0))

        self.mineral_name_entry.grid(row=1, column=1, padx=(5, 0), pady=(5, 0))
        self.mineral_th_entry.grid(row=2, column=1, padx=(5, 0), pady=(5, 0))
        self.mineral_rho_entry.grid(row=3, column=1, padx=(5, 0), pady=(5, 0))

        self.mineral_th_unit_label.grid(row=2, column=2, sticky='ew', padx=(1, 5), pady=(5, 0))
        self.mineral_rho_unit_label.grid(row=3, column=2, sticky='ew', padx=(1, 5), pady=(5, 0))

        # Adding control buttons
        self.cancel_button = tk.Button(self.main_frame,
                                       text='Cancel',
                                       width=16,
                                       command=self.cancel_button)
        self.cancel_button.grid(row=4, column=1, columnspan=2, pady=(5, 5))

    def cancel_button(self):
        self.destroy()

class AddNewRock(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("200x200")
        self.title("Add new mineral")
        self.resizable(False, False)

        # Adding container frames:
        self.background_frame = tk.Frame(self, bg='#b6cb94')
        self.background_frame.pack(side='top', fill='both', expand=True)

        self.main_frame = tk.Frame(self.background_frame, bg='#a7bf37')
        self.main_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)

        # Adding labels and entries:
        self.top_label = tk.Label(self.main_frame, text='Add new mineral:')
        self.mineral_name_label = tk.Label(self.main_frame, text="Name:")
        self.mineral_th_label = tk.Label(self.main_frame, text='Thermal conductivity')
        self.mineral_rho_label = tk.Label(self.main_frame, text='Density')

        self.mineral_name_entry = tk.Entry(self.main_frame, width=20)
        self.mineral_th_entry = tk.Entry(self.main_frame, width=20)
        self.mineral_rho_entry = tk.Entry(self.main_frame, width=20)

        # Packing labels and entries
        self.top_label.grid(row=0, column=0, columnspan=2)
        self.mineral_name_label.grid(row=1, column=0)
        self.mineral_th_label.grid(row=2, column=0)
        self.mineral_rho_label.grid(row=3, column=0)

        self.mineral_name_entry.grid(row=1, column=1)
        self.mineral_th_entry.grid(row=2, column=1)
        self.mineral_rho_entry.grid(row=3, column=1)


'''
class MainLeftTopFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(self, parent)
        self.place(x=0, y=0)
        self.config(width=600, height=400, bg='yellow')
        #label = Label(self, text='Left Frame', font='Verdana 12 bold')
        #label.pack(pady=10, padx=10)


class MainLeftBottomFrame(tk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.place(x=0, y=400)
        self.config(width=600, height=400, bg='green')

        label_frame = LabelFrame(self, width=580, height=380, text='Layer properties', font='Arial 10')
        label_frame.place(x=10, y=10)


        self.labels = []
        numb = 1
        for i in range(8):
            self.labels.append(Label(label_frame, text='Layer ' + str(numb), font='Arial 10'))
            numb += 1
        number1 = 0
        for i in range(8):
            self.labels[number1].place(x=20, y=40+i*25, anchor=W)
            number1 += 1

        self.entries = []
        for i in range(48):
            self.entries.append(Entry(label_frame, width=8))
        number = 0
        for i in range(7):
            for j in range(6):
                self.entries[number].insert(0, variable_list[number])
                self.entries[number].place(x=80+j*70, y=40+i*25, anchor=W)
                number += 1

        button1 = Button(label_frame, width=6, text='Enter', command=self.get_values)
        button1.place(x=430, y=250, anchor=W)

        button2 = Button(label_frame, width=6, text='Plot', command=self.plot)
        button2.place(x=430, y=290, anchor=W)

        button3 = Button(label_frame, text='Open', command=self.new_window)
        button3.place(x=520, y=320)

    def new_window(self):
        new_window = _2_th_cond.NewWindow()

    def plot(self):
        plot = MainRightBottomFrame(self.controller)


class MainRightTopFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.place(x=600, y=0)
        self.config(width=600, height=400, bg='green')

        x = [1,2,3,4,5,6,7,8]
        y = [5,2,6,8,4,8,3,5]

        figure = Figure(figsize=(6,4), dpi=100)
        subplot = figure.add_subplot(111)
        subplot.plot(x, y)

        canvas = FigureCanvasTkAgg(figure, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

class MainRightBottomFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.place(x=600, y=400)
        self.config(width=600, height=400, bg='yellow')

        plot = Fig1(self)


class Fig1:
    def __init__(self, parent):

        new_instance = FrostCalc()
        df = new_instance.Calculation(1803)

        fig = Figure(figsize=(6,4))
        fig.patch.set_facecolor('xkcd:mint green')

        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        axes.plot(df.index.values, df['z_tot']*-1, label='SSR with SP', linewidth=2)
        axes.plot(df.index.values, df['z_tot_0_SP']*-1, label='SSR no SP', linewidth=2)
        # axes.plot(times, temp_2degC, label='Comsol_2degC', linewidth=2)
        # axes.plot(times, temp_4degC, label='Comsol_4degC', linewidth=2)
        axes.legend(loc="upper right")
        axes.patch.set_facecolor('xkcd:mint green')
        axes.plot([0, 4000], [-h1, -h1], color="black", linestyle='--', linewidth=1)       #Top of 2nd layer line
        axes.plot([0, 4000], [-(h1+h2), -(h1+h2)], color="black", linestyle='--', linewidth=1)       #Top of 3nd layer line
        axes.plot([0, 4000], [-(h1+h2+h3), -(h1+h2+h3)], color="black", linestyle='--', linewidth=1)       #Top of 4th layer line
        for axis in ['top','bottom','left','right']:
            axes.spines[axis].set_linewidth(1.5)
        axes.set_title("Frost front penetration")
        axes.set_xlabel('Time, hours', size=12)
        axes.set_ylabel('Frost front, m', size=12)
        axes.set_xlim([0, 4000])
        axes.set_ylim([-2.5, 0])
        axes.set_xticks([0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000])
        axes.set_yticks([0, -0.5, -1.0, -1.5, -2.0, -2.5])
        axes.annotate("Top of 2nd layer", xy=(1400, -h1), xytext=(1400,-(h1-0.15)),
                      arrowprops=dict(arrowstyle="-|>,head_width=0.4,head_length=0.8",
                                      shrinkA=0,shrinkB=0, connectionstyle="arc3,rad=0.5"))
        axes.annotate("Top of 3nd layer", xy=(1400, -(h1+h2)), xytext=(1400,-(h1+h2-0.15)),
                      arrowprops=dict(arrowstyle="-|>,head_width=0.4,head_length=0.8",
                                      shrinkA=0,shrinkB=0, connectionstyle="arc3,rad=0.5"))
        axes.annotate("Top of 4th layer", xy=(600, -(h1+h2+h3)), xytext=(600,-(h1+h2+h3-0.15)),
                      arrowprops=dict(arrowstyle="-|>,head_width=0.4,head_length=0.8",
                                      shrinkA=0,shrinkB=0, connectionstyle="arc3,rad=0.5"))
        axes.tick_params(axis='both', direction='in', width=1.5, right=True, top=True)

        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        print([h1, h2, h3, h4])
'''