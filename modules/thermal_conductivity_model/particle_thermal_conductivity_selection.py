import tkinter as tk
from tkinter import ttk
from modules.thermal_conductivity_model.particle_thermal_conductivity_library import mineral_class_list


class ParticleThermalConductivitySelection(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.geometry("500x1000+300+400")
        self.title("Select minerals")
        self.resizable(False, False)
        self.controller = controller

        self.mineral_class_container = []

        self.background_frame = ttk.Frame(self, style='Standard.TFrame')
        self.background_frame.pack(side='top', fill='both', expand=True)

        self.main_frame = ttk.Frame(self.background_frame, style='Standard.TFrame')
        self.main_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)

        # Adding top frame for column labels
        self.top_label_frame = ttk.Frame(self.main_frame, style='DarkFrame.TFrame')
        self.top_label_frame.pack(side='top', fill='x')

        # Adding center frame for canvas and scrollbar
        self.center_frame = tk.Frame(self.main_frame)
        self.center_frame.pack(side='top', fill='both', expand=True)
        self.center_frame.columnconfigure(0, weight=1)
        self.center_frame.rowconfigure(0, weight=1)                # is this necessary??

        # Adding bottom frame with button
        self.button_label_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.button_label_frame.pack(side='top', fill='x')

        self.select_button = ttk.Button(self.button_label_frame,
                                        text='press',
                                        takefocus=False,
                                        style='Standard.TButton',
                                        command=self.select_materials)
        self.select_button.pack(side='left', pady=(10, 0))

        # Adding canvas
        self.canvas = tk.Canvas(self.center_frame, highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky='nsew')

        self.canvas_frame = ttk.Frame(self.canvas, style='Standard.TFrame')
        self.scrollable_window = self.canvas.create_window((0, 0), window=self.canvas_frame, anchor='nw')

        # Adding bindings
        self.canvas_frame.bind("<Configure>", self.configure_scroll_region)
        self.canvas.bind("<Configure>", self.configure_window_size)
        #self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        # Adding scrollbar
        self.scrollbar = ttk.Scrollbar(self.center_frame, orient='vertical', command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas_frame.bind('<Enter>', self._bound_to_mousewheel)
        self.canvas_frame.bind('<Leave>', self._unbound_to_mousewheel)

        # Top row label containers
        self.empty_container = ttk.Frame(self.top_label_frame, width=25, height=40, style='DarkFrame.TFrame')
        self.mineral_name_container = ttk.Frame(self.top_label_frame, width=200, height=40, style='DarkFrame.TFrame')
        self.mineral_rho_container = ttk.Frame(self.top_label_frame, width=100, height=40, style='DarkFrame.TFrame')
        self.mineral_th_container = ttk.Frame(self.top_label_frame, width=100, height=40, style='DarkFrame.TFrame')

        # Packing top row label containers
        self.empty_container.pack(side='left', padx=(5, 0))
        self.mineral_name_container.pack(side='left', padx=(5, 0))
        self.mineral_rho_container.pack(side='left', padx=(5, 0))
        self.mineral_th_container.pack(side='left', padx=(5, 0))

        self.mineral_name_container.pack_propagate(0)
        self.mineral_rho_container.pack_propagate(0)
        self.mineral_th_container.pack_propagate(0)

        # Adding top row labels
        self.mineral_name = ttk.Label(self.mineral_name_container, text='Mineral', style='DarkLargeLabel.TLabel')
        self.mineral_rho = ttk.Label(self.mineral_rho_container, text='Rho', style='DarkLargeLabel.TLabel')
        self.mineral_th = ttk.Label(self.mineral_th_container, text='Th', style='DarkLargeLabel.TLabel')

        #Packing top row labels
        self.mineral_name.pack(expand=True, fill='x')
        self.mineral_rho.pack(expand=True, fill='x')
        self.mineral_th.pack(expand=True, fill='x')

        self.display_all_materials()

    def configure_scroll_region(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def configure_window_size(self, event):
        self.canvas.itemconfig(self.scrollable_window, width=self.canvas.winfo_width())

    def _bound_to_mousewheel(self, event):
        self.canvas.bind_all('<MouseWheel>', self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        self.canvas.unbind_all('<MouseWheel>')

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-int(event.delta / 120), "units")

    def display_all_materials(self):
        for class_name, class_name_postfix, class_content in mineral_class_list:
            new_mineral_class = NewMineralClass(self.canvas_frame, class_name, class_name_postfix, class_content)
            self.mineral_class_container.append(new_mineral_class)

    def select_materials(self):
        selected_entries = []
        for mineral_class in self.mineral_class_container:
            for entry_line in mineral_class.class_entry_line_container:
                if entry_line.checked.get() == 1:
                    selected_mineral = (entry_line.var_name.get().strip(),
                                        entry_line.var_rho.get(),
                                        entry_line.var_th.get())
                    selected_entries.append(selected_mineral)
        self.controller.refresh_with_selected_entries(selected_entries)
        self.destroy()


class NewMineralClass(ttk.Frame):
    def __init__(self, parent, class_name, class_name_postfix, class_content):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill='x')
        self['style'] = 'Standard.TFrame'
        self.class_entry_line_container = []
        self.columnconfigure(0, weight=1)

        # Adding class name label
        self.class_name_entry_line = ttk.Frame(self, style='Standard.TFrame')
        self.class_name_entry_line.grid(row=0, column=0, sticky='ew')
        self.class_name_entry_line.grid_propagate(0)

        self.empty_container = ttk.Frame(self.class_name_entry_line, width=25, height=40, style='Standard.TFrame')
        self.empty_container.pack(side='left', padx=(5, 0))

        self.class_name_label_container = ttk.Frame(self.class_name_entry_line, height=40, style='Standard.TFrame')
        self.class_name_label_container.pack(side='left', padx=(5, 0))

        self.class_name_label = ttk.Label(self.class_name_label_container,
                                          text=class_name,
                                          style='LeftAlignedLargeBold.TLabel')
        self.class_name_label.pack(expand=True)

        self.class_name_postfix_label_container = ttk.Frame(self.class_name_entry_line,
                                                            height=40,
                                                            style='Standard.TFrame')
        self.class_name_postfix_label_container.pack(side='left')

        self.class_name_postfix_label = ttk.Label(self.class_name_postfix_label_container,
                                                  text=class_name_postfix,
                                                  style='LeftAlignedSmall.TLabel')
        self.class_name_postfix_label.pack(expand=True)

        row_number = 1
        for sub_class in class_content:
            if len(sub_class) == 3:
                flag = True
                new_entry_line = NewMineralClassEntryLine(self,
                                                          row_number,
                                                          flag,
                                                          sub_class[0],
                                                          sub_class[1],
                                                          sub_class[2])
                self.class_entry_line_container.append(new_entry_line)
                row_number += 1
            else:
                flag = False
                new_entry_line = NewMineralClassEntryLine(self,
                                                          row_number,
                                                          flag,
                                                          sub_class[0],
                                                          sub_class[1],
                                                          sub_class[2])
                row_number += 1
                for mineral in sub_class[3:]:
                    flag = True
                    new_entry_line = NewMineralClassEntryLine(self,
                                                              row_number,
                                                              flag,
                                                              '     ' + mineral[0],
                                                              mineral[1],
                                                              mineral[2])
                    self.class_entry_line_container.append(new_entry_line)
                    row_number += 1


class NewMineralClassEntryLine(ttk.Frame):
    def __init__(self, parent, row, flag, text1, text2, text3):
        super().__init__(parent)
        self.parent = parent
        self.row = row
        self['style'] = 'Standard.TFrame'
        self.grid(row=self.row, column=0, sticky='ew')
        self.grid_propagate(0)
        self.flag = flag

        # Adding containers
        self.checkbox_container = ttk.Frame(self, width=25, height=30, style='Standard.TFrame')
        self.name_label_container = ttk.Frame(self, width=200, height=30, style='Standard.TFrame')
        self.rho_label_container = ttk.Frame(self, width=100, height=30, style='Standard.TFrame')
        self.th_label_container = ttk.Frame(self, width=100, height=30, style='Standard.TFrame')
        self.checkbox_container.pack(side='left', padx=(5, 0))
        self.name_label_container.pack(side='left', padx=(5, 0))
        self.rho_label_container.pack(side='left', padx=(5, 0))
        self.th_label_container.pack(side='left', padx=(5, 0))
        self.checkbox_container.pack_propagate(0)
        self.name_label_container.pack_propagate(0)
        self.rho_label_container.pack_propagate(0)
        self.th_label_container.pack_propagate(0)

        # Adding checkbox and labels
        if flag == True:
            self.checked = tk.IntVar()
            self.checked.set(0)
            self.var_name = tk.StringVar(value=text1)
            self.var_rho = tk.StringVar(value=text2)
            self.var_th = tk.StringVar(value=text3)

            self.checkbox = ttk.Checkbutton(self.checkbox_container,
                                            variable=self.checked,
                                            style='Standard.TCheckbutton')
            self.rho_label = ttk.Label(self.rho_label_container, textvariable=self.var_rho, style='Standard.TLabel')
            self.th_label = ttk.Label(self.th_label_container, textvariable=self.var_th, style='Standard.TLabel')

            self.checkbox.pack(expand=True)
            self.rho_label.pack(expand=True, fill='x')
            self.th_label.pack(expand=True, fill='x')

            self.name_label = ttk.Label(self.name_label_container,
                                        textvariable=self.var_name,
                                        style='LeftAligned.TLabel')
            self.name_label.pack(expand=True, fill='x')

        else:
            self.var_name = tk.StringVar(value=text1)
            self.name_label = ttk.Label(self.name_label_container,
                                        textvariable=self.var_name,
                                        style='LeftAligned.TLabel')
            self.name_label.pack(expand=True, fill='x')
