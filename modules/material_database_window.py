import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

con = sqlite3.connect("modules/material_database.db")
cur = con.cursor()

class MaterialDatabaseWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        #self.geometry("1500x500+500+700")
        self.title("Material Database")
        self.resizable(False, False)

        self.entry_container = []

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

        # Adding canvas
        self.canvas = tk.Canvas(self.center_frame, highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky='nsew')

        self.canvas_frame = tk.Frame(self.canvas)
        self.scrollable_window = self.canvas.create_window((0, 0), window=self.canvas_frame, anchor='nw')

        # Adding bindings
        self.canvas_frame.bind("<Configure>", self.configure_scroll_region)
        self.canvas.bind("<Configure>", self.configure_window_size)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        # Adding scrollbar
        self.scrollbar = ttk.Scrollbar(self.center_frame, orient='vertical', command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)


        # Top row label containers
        height = 40
        width = 70
        self.empty_space1_container = ttk.Frame(self.top_label_frame, width=30, height=height, style='DarkFrame.TFrame')
        self.mat_name_container = ttk.Frame(self.top_label_frame, width=250, height=height, style='DarkFrame.TFrame')
        self.mat_height_container = ttk.Frame(self.top_label_frame, width=width, height=height, style='DarkFrame.TFrame')
        self.mat_rhod_container = ttk.Frame(self.top_label_frame, width=width, height=height, style='DarkFrame.TFrame')
        self.mat_rhos_container = ttk.Frame(self.top_label_frame, width=width, height=height, style='DarkFrame.TFrame')
        self.mat_n_container = ttk.Frame(self.top_label_frame, width=width, height=height, style='DarkFrame.TFrame')
        self.mat_w_grav_container = ttk.Frame(self.top_label_frame, width=width, height=height, style='DarkFrame.TFrame')
        self.mat_sp_val_container = ttk.Frame(self.top_label_frame, width=width, height=height, style='DarkFrame.TFrame')
        self.mat_a_val_container = ttk.Frame(self.top_label_frame, width=width, height=height, style='DarkFrame.TFrame')
        self.mat_ku_container = ttk.Frame(self.top_label_frame, width=width, height=height, style='DarkFrame.TFrame')
        self.mat_kf_container = ttk.Frame(self.top_label_frame, width=width, height=height, style='DarkFrame.TFrame')
        self.mat_sr_container = ttk.Frame(self.top_label_frame, width=width, height=height, style='DarkFrame.TFrame')
        self.mat_lf_container = ttk.Frame(self.top_label_frame, width=width, height=height, style='DarkFrame.TFrame')
        self.empty_space2_container = ttk.Frame(self.top_label_frame, width=30, height=height, style='DarkFrame.TFrame')

        # Packing top row label containers
        self.empty_space1_container.pack(side='left', padx=(5, 0))
        self.mat_name_container.pack(side='left', padx=(5, 0))
        self.mat_height_container.pack(side='left', padx=(5, 0))
        self.mat_rhod_container.pack(side='left', padx=(5, 0))
        self.mat_rhos_container.pack(side='left', padx=(5, 0))
        self.mat_n_container.pack(side='left', padx=(5, 0))
        self.mat_w_grav_container.pack(side='left', padx=(5, 0))
        self.mat_sp_val_container.pack(side='left', padx=(5, 0))
        self.mat_a_val_container.pack(side='left', padx=(5, 0))
        self.mat_ku_container.pack(side='left', padx=(5, 0))
        self.mat_kf_container.pack(side='left', padx=(5, 0))
        self.mat_sr_container.pack(side='left', padx=(5, 0))
        self.mat_lf_container.pack(side='left', padx=(5, 0))
        self.empty_space2_container.pack(side='left', padx=(5, 0))

        self.empty_space1_container.pack_propagate(0)
        self.mat_name_container.pack_propagate(0)
        self.mat_height_container.pack_propagate(0)
        self.mat_rhod_container.pack_propagate(0)
        self.mat_rhos_container.pack_propagate(0)
        self.mat_n_container.pack_propagate(0)
        self.mat_w_grav_container.pack_propagate(0)
        self.mat_sp_val_container.pack_propagate(0)
        self.mat_a_val_container.pack_propagate(0)
        self.mat_ku_container.pack_propagate(0)
        self.mat_kf_container.pack_propagate(0)
        self.mat_sr_container.pack_propagate(0)
        self.mat_lf_container.pack_propagate(0)
        self.empty_space2_container.pack_propagate(0)


        # Adding top row labels
        self.mat_name = ttk.Label(self.mat_name_container, text='Material', style='DarkLargeLabel.TLabel')
        self.mat_height = ttk.Label(self.mat_height_container, text='Height', style='DarkLargeLabel.TLabel')
        self.mat_rhod = ttk.Label(self.mat_rhod_container, text='Rhod', style='DarkLargeLabel.TLabel')
        self.mat_rhos = ttk.Label(self.mat_rhos_container, text='Rhos', style='DarkLargeLabel.TLabel')
        self.mat_n = ttk.Label(self.mat_n_container, text='n', style='DarkLargeLabel.TLabel')
        self.mat_w_grav = ttk.Label(self.mat_w_grav_container, text='w%', style='DarkLargeLabel.TLabel')
        self.mat_sp_val = ttk.Label(self.mat_sp_val_container, text='SP', style='DarkLargeLabel.TLabel')
        self.mat_a_val = ttk.Label(self.mat_a_val_container, text='a', style='DarkLargeLabel.TLabel')
        self.mat_ku = ttk.Label(self.mat_ku_container, text='ku', style='DarkLargeLabel.TLabel')
        self.mat_kf = ttk.Label(self.mat_kf_container, text='kf', style='DarkLargeLabel.TLabel')
        self.mat_sr = ttk.Label(self.mat_sr_container, text='sr', style='DarkLargeLabel.TLabel')
        self.mat_lf = ttk.Label(self.mat_lf_container, text='lf', style='DarkLargeLabel.TLabel')

        #Packing top row labels
        self.mat_name.pack(expand=True)
        self.mat_height.pack(expand=True)
        self.mat_rhod.pack(expand=True)
        self.mat_rhos.pack(expand=True)
        self.mat_n.pack(expand=True)
        self.mat_w_grav.pack(expand=True)
        self.mat_sp_val.pack(expand=True)
        self.mat_a_val.pack(expand=True)
        self.mat_ku.pack(expand=True)
        self.mat_kf.pack(expand=True)
        self.mat_sr.pack(expand=True)
        self.mat_lf.pack(expand=True)

        self.display_all_materials()

        # Adding bottom frame with buttons
        self.bottom_button_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.bottom_button_frame.pack(side='top', fill='x')

        self.new_mat = ttk.Button(self.bottom_button_frame,
                                  text="New material",
                                  style='Standard.TButton',
                                  takefocus=False,
                                  command=self.add_new_material)
        self.new_mat.grid(row=0, column=0, columnspan=2, padx=(10, 0))

    def display_all_materials(self):
        materials = cur.execute("SELECT * FROM materials").fetchall()
        for i in materials:
            new_entry = DbEntryLine(self.canvas_frame, self, i)
            self.entry_container.append(new_entry)
            new_entry.pack(side='top', fill='x')

    def configure_scroll_region(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def configure_window_size(self, event):
        self.canvas.itemconfig(self.scrollable_window, width=self.canvas.winfo_width())

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-int(event.delta / 120), "units")

    def db_edit_window(self, id):
        db_edit = DbEdit(id)

    def add_new_material(self):
        new_material = NewDbMaterial()


class DbEntryLine(ttk.Frame):
    def __init__(self, parent, controller, vals):
        super().__init__(parent)
        self['style'] = 'Standard.TFrame'
        self.parent = parent
        self.controller = controller
        self.item_id = vals[0]

        self.edit_image = tk.PhotoImage(file="modules/icons/cog_icon&16.png")

        # Adding label containers
        height = 40
        width = 70
        self.empty_space1_container = ttk.Frame(self, width=30, height=height, style='RedRed.TFrame')
        self.mat_name_container = ttk.Frame(self, width=250, height=height, style='Standard.TFrame')
        self.mat_height_container = ttk.Frame(self, width=width, height=height, style='Red.TFrame')
        self.mat_rhod_container = ttk.Frame(self, width=width, height=height, style='Standard.TFrame')
        self.mat_rhos_container = ttk.Frame(self, width=width, height=height, style='Standard.TFrame')
        self.mat_n_container = ttk.Frame(self, width=width, height=height, style='Standard.TFrame')
        self.mat_w_grav_container = ttk.Frame(self, width=width, height=height, style='Standard.TFrame')
        self.mat_sp_val_container = ttk.Frame(self, width=width, height=height, style='Standard.TFrame')
        self.mat_a_val_container = ttk.Frame(self, width=width, height=height, style='Standard.TFrame')
        self.mat_ku_container = ttk.Frame(self, width=width, height=height, style='Standard.TFrame')
        self.mat_kf_container = ttk.Frame(self, width=width, height=height, style='Standard.TFrame')
        self.mat_sr_container = ttk.Frame(self, width=width, height=height, style='Standard.TFrame')
        self.mat_lf_container = ttk.Frame(self, width=width, height=height, style='Standard.TFrame')
        self.empty_space2_container = ttk.Frame(self, width=30, height=height, style='Standard.TFrame')

        # Packing label containers
        self.empty_space1_container.pack(side='left', padx=(5, 0))
        self.mat_name_container.pack(side='left', padx=(5, 0))
        self.mat_height_container.pack(side='left', padx=(5, 0))
        self.mat_rhod_container.pack(side='left', padx=(5, 0))
        self.mat_rhos_container.pack(side='left', padx=(5, 0))
        self.mat_n_container.pack(side='left', padx=(5, 0))
        self.mat_w_grav_container.pack(side='left', padx=(5, 0))
        self.mat_sp_val_container.pack(side='left', padx=(5, 0))
        self.mat_a_val_container.pack(side='left', padx=(5, 0))
        self.mat_ku_container.pack(side='left', padx=(5, 0))
        self.mat_kf_container.pack(side='left', padx=(5, 0))
        self.mat_sr_container.pack(side='left', padx=(5, 0))
        self.mat_lf_container.pack(side='left', padx=(5, 0))
        self.empty_space2_container.pack(side='left', padx=(5, 7))

        self.empty_space1_container.pack_propagate(0)
        self.mat_name_container.pack_propagate(0)
        self.mat_height_container.pack_propagate(0)
        self.mat_rhod_container.pack_propagate(0)
        self.mat_rhos_container.pack_propagate(0)
        self.mat_n_container.pack_propagate(0)
        self.mat_w_grav_container.pack_propagate(0)
        self.mat_sp_val_container.pack_propagate(0)
        self.mat_a_val_container.pack_propagate(0)
        self.mat_ku_container.pack_propagate(0)
        self.mat_kf_container.pack_propagate(0)
        self.mat_sr_container.pack_propagate(0)
        self.mat_lf_container.pack_propagate(0)
        self.empty_space2_container.pack_propagate(0)

        # Adding labels
        self.empty_label = ttk.Label(self.empty_space1_container, text=vals[0], style='Standard.TLabel')
        self.mat_name = ttk.Label(self.mat_name_container, text=vals[1], style='Standard.TLabel')
        self.mat_height = ttk.Label(self.mat_height_container, text=vals[2], style='Standard.TLabel')
        self.mat_rhod = ttk.Label(self.mat_rhod_container, text=vals[3], style='Standard.TLabel')
        self.mat_rhos = ttk.Label(self.mat_rhos_container, text=vals[3], style='Standard.TLabel')
        self.mat_n = ttk.Label(self.mat_n_container, text=vals[3], style='Standard.TLabel')
        self.mat_w_grav = ttk.Label(self.mat_w_grav_container, text=vals[4], style='Standard.TLabel')
        self.mat_sp_val = ttk.Label(self.mat_sp_val_container, text=vals[5], style='Standard.TLabel')
        self.mat_a_val = ttk.Label(self.mat_a_val_container, text=vals[6], style='Standard.TLabel')
        self.mat_ku = ttk.Label(self.mat_ku_container, text=vals[7], style='Standard.TLabel')
        self.mat_kf = ttk.Label(self.mat_kf_container, text=vals[8], style='Standard.TLabel')
        self.mat_sr = ttk.Label(self.mat_sr_container, text=vals[9], style='Standard.TLabel')
        self.mat_lf = ttk.Label(self.mat_lf_container, text=vals[10], style='Standard.TLabel')
        self.edit_button = tk.Button(self.empty_space2_container,
                                     image=self.edit_image,
                                     borderwidth=2,
                                     command=lambda: self.controller.db_edit_window(self.item_id))

        #image = self.edit_image,

        # Packing labels
        self.empty_label.pack(expand=True)
        self.mat_name.pack(expand=True)
        self.mat_height.pack(expand=True)
        self.mat_rhod.pack(expand=True)
        self.mat_rhos.pack(expand=True)
        self.mat_n.pack(expand=True)
        self.mat_w_grav.pack(expand=True)
        self.mat_sp_val.pack(expand=True)
        self.mat_a_val.pack(expand=True)
        self.mat_ku.pack(expand=True)
        self.mat_kf.pack(expand=True)
        self.mat_sr.pack(expand=True)
        self.mat_lf.pack(expand=True)
        self.edit_button.place(relx=0.5, rely=0.5, anchor='center')

    def delete_object(self):
        pass

    def repack_objects(self):
        pass

class DbEdit(tk.Toplevel):
    def __init__(self, id):
        super().__init__()
        self.geometry("+600+600")
        self.resizable(False, False)
        self.title("Edit material")
        self.item_id = id

        material = cur.execute("SELECT * FROM materials WHERE mat_id=?", (self.item_id,)).fetchall()
        self.var_name = tk.StringVar(value=material[0][1])
        self.var_height = tk.StringVar(value=material[0][2])
        self.var_rho = tk.StringVar(value=material[0][3])
        self.var_w_grav = tk.StringVar(value=material[0][4])
        self.var_sp_val = tk.StringVar(value=material[0][5])
        self.var_a_val = tk.StringVar(value=material[0][6])
        self.var_ku = tk.StringVar(value=material[0][7])
        self.var_kf = tk.StringVar(value=material[0][8])
        self.var_sr = tk.StringVar(value=material[0][9])
        self.var_lf = tk.StringVar(value=material[0][10])

        self.main_frame = ttk.Frame(self, style='Standard.TFrame')
        self.main_frame.pack(side='top', fill='both', expand=True, )

        self.inner_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.inner_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)

        # Adding entry name labels
        self.mat_name = ttk.Label(self.inner_frame, text='Material name', style='LeftAligned.TLabel')
        self.mat_height = ttk.Label(self.inner_frame, text='Default height (h)', style='LeftAligned.TLabel')
        self.mat_rho = ttk.Label(self.inner_frame, text='Density (rho)', style='LeftAligned.TLabel')
        self.mat_w_grav = ttk.Label(self.inner_frame, text='Water content (w%)', style='LeftAligned.TLabel')
        self.mat_sp_val = ttk.Label(self.inner_frame, text='Segregation Potential (SP)', style='LeftAligned.TLabel')
        self.mat_a_val = ttk.Label(self.inner_frame, text='a', style='LeftAligned.TLabel')
        self.mat_ku = ttk.Label(self.inner_frame, text='Unfrozen thermal conductivity (ku)', style='LeftAligned.TLabel')
        self.mat_kf = ttk.Label(self.inner_frame, text='Frozen thermal conductivity (kf)', style='LeftAligned.TLabel')
        self.mat_sr = ttk.Label(self.inner_frame, text='Degree of saturation (Sr)', style='LeftAligned.TLabel')
        self.mat_lf = ttk.Label(self.inner_frame, text='Latent heat (Lf)', style='LeftAligned.TLabel')

        # Adding entry fields
        self.entry_name = ttk.Entry(self.inner_frame, textvariable=self.var_name, width=18, style='Standard.TEntry')
        self.entry_height = ttk.Entry(self.inner_frame, textvariable=self.var_height, width=18, style='Standard.TEntry')
        self.entry_rho = ttk.Entry(self.inner_frame, textvariable=self.var_rho, width=18, style='Standard.TEntry')
        self.entry_w_grav = ttk.Entry(self.inner_frame, textvariable=self.var_w_grav, width=18, style='Standard.TEntry')
        self.entry_sp_val = ttk.Entry(self.inner_frame, textvariable=self.var_sp_val, width=18, style='Standard.TEntry')
        self.entry_a_val = ttk.Entry(self.inner_frame, textvariable=self.var_a_val, width=18, style='Standard.TEntry')
        self.entry_ku = ttk.Entry(self.inner_frame, textvariable=self.var_ku, width=18, style='Standard.TEntry')
        self.entry_kf = ttk.Entry(self.inner_frame, textvariable=self.var_kf, width=18, style='Standard.TEntry')
        self.entry_sr = ttk.Entry(self.inner_frame, textvariable=self.var_sr, width=18, style='Standard.TEntry')
        self.entry_lf = ttk.Entry(self.inner_frame, textvariable=self.var_lf, width=18, style='Standard.TEntry')

        # Adding entry unit labels
        self.mat_height_unit = ttk.Label(self.inner_frame, text='[m]', style='LeftAligned.TLabel')
        self.mat_rho_unit = ttk.Label(self.inner_frame, text='[g/cm3]', style='LeftAligned.TLabel')
        self.mat_w_grav_unit = ttk.Label(self.inner_frame, text='[%]', style='LeftAligned.TLabel')
        self.mat_sp_val_unit = ttk.Label(self.inner_frame, text='[unit]', style='LeftAligned.TLabel')
        self.mat_a_val_unit = ttk.Label(self.inner_frame, text='[unit]', style='LeftAligned.TLabel')
        self.mat_ku_unit = ttk.Label(self.inner_frame, text='[W/mK]', style='LeftAligned.TLabel')
        self.mat_kf_unit = ttk.Label(self.inner_frame, text='[W/mK]', style='LeftAligned.TLabel')
        self.mat_sr_unit = ttk.Label(self.inner_frame, text='[unit]', style='LeftAligned.TLabel')
        self.mat_lf_unit = ttk.Label(self.inner_frame, text='[unit]', style='LeftAligned.TLabel')

        # Packing entry name labels
        self.mat_name.grid(row=0, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_height.grid(row=1, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_rho.grid(row=2, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_w_grav.grid(row=3, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_sp_val.grid(row=4, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_a_val.grid(row=5, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_ku.grid(row=6, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_kf.grid(row=7, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_sr.grid(row=8, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_lf.grid(row=9, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')

        # Packing entry fields
        self.entry_name.grid(row=0, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_height.grid(row=1, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_rho.grid(row=2, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_w_grav.grid(row=3, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_sp_val.grid(row=4, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_a_val.grid(row=5, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_ku.grid(row=6, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_kf.grid(row=7, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_sr.grid(row=8, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_lf.grid(row=9, column=1, padx=(10, 0), pady=(6, 0))

        # Packing entry unit labels
        self.mat_height_unit.grid(row=1, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_rho_unit.grid(row=2, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_w_grav_unit.grid(row=3, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_sp_val_unit.grid(row=4, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_a_val_unit.grid(row=5, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_ku_unit.grid(row=6, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_kf_unit.grid(row=7, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_sr_unit.grid(row=8, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_lf_unit.grid(row=9, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')

        # Add control buttons
        self.save_button = ttk.Button(self.inner_frame,
                                      width=20,
                                      text='Save',
                                      style='Standard.TButton',
                                      takefocus=False,
                                      command=self.save_material)
        self.save_button.grid(row=10, column=0, padx=(10, 0), pady=(14, 10), sticky='w')
        self.cancel_button = ttk.Button(self.inner_frame,
                                        width=20,
                                        text='Cancel',
                                        style='Standard.TButton',
                                        takefocus=False,
                                        command=self.cancel_operation)
        self.cancel_button.grid(row=10, column=1, columnspan=2, padx=(10, 0), pady=(14, 10), sticky='e')

    def save_material(self):
        material_name = self.var_name.get()
        height = self.var_height.get()
        rho = self.var_rho.get()
        w_grav = self.var_w_grav.get()
        sp_val = self.var_sp_val.get()
        a_val = self.var_a_val.get()
        ku = self.var_ku.get()
        kf = self.var_kf.get()
        sr = self.var_sr.get()
        lf = self.var_lf.get()

        def check_if_empty():
            check_list = [material_name, height, rho, w_grav, sp_val, a_val, ku, kf, sr, lf]
            for i in check_list:
                if i == "":
                    return False
            return True

        if check_if_empty():
            try:
                query = """UPDATE materials set mat_name=?,
                                                mat_height=?,
                                                mat_rho=?,
                                                mat_w_grav=?,
                                                mat_sp_val=?,
                                                mat_a_val=?,
                                                mat_ku=?,
                                                mat_kf=?,
                                                mat_sr=?,
                                                mat_lf=? WHERE mat_id=?"""
                cur.execute(query, (material_name, height, rho, w_grav, sp_val, a_val, ku, kf, sr, lf, self.item_id))
                con.commit()
                messagebox.showinfo("Success", "Successfully updated!", icon='info')

            except:
                messagebox.showerror("Error", "Can't add to database!", icon='warning')

        else:
            messagebox.showerror("Error", "Fields cannot be empty", icon='warning')

    def cancel_operation(self):
        self.destroy()

class NewDbMaterial(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("+600+600")
        self.resizable(False, False)
        self.title('Add new material')

        self.main_frame = ttk.Frame(self, style='Standard.TFrame')
        self.main_frame.pack(side='top', fill='both', expand=True,)

        self.inner_frame = ttk.Frame(self.main_frame, style='Standard.TFrame')
        self.inner_frame.pack(side='top', fill='both', expand=True, padx=10, pady=10)

        # Adding entry name labels
        self.mat_name = ttk.Label(self.inner_frame, text='Material name', style='LeftAligned.TLabel')
        self.mat_height = ttk.Label(self.inner_frame, text='Default height (h)', style='LeftAligned.TLabel')
        self.mat_rho = ttk.Label(self.inner_frame, text='Density (rho)', style='LeftAligned.TLabel')
        self.mat_w_grav = ttk.Label(self.inner_frame, text='Water content (w%)', style='LeftAligned.TLabel')
        self.mat_sp_val = ttk.Label(self.inner_frame, text='Segregation Potential (SP)', style='LeftAligned.TLabel')
        self.mat_a_val = ttk.Label(self.inner_frame, text='a', style='LeftAligned.TLabel')
        self.mat_ku = ttk.Label(self.inner_frame, text='Unfrozen thermal conductivity (ku)', style='LeftAligned.TLabel')
        self.mat_kf = ttk.Label(self.inner_frame, text='Frozen thermal conductivity (kf)', style='LeftAligned.TLabel')
        self.mat_sr = ttk.Label(self.inner_frame, text='Degree of saturation (Sr)', style='LeftAligned.TLabel')
        self.mat_lf = ttk.Label(self.inner_frame, text='Latent heat (Lf)', style='LeftAligned.TLabel')

        # Adding entry fields
        self.entry_name = ttk.Entry(self.inner_frame, width=18, style='Standard.TEntry')
        self.entry_height = ttk.Entry(self.inner_frame, width=18, style='Standard.TEntry')
        self.entry_rho = ttk.Entry(self.inner_frame, width=18, style='Standard.TEntry')
        self.entry_w_grav = ttk.Entry(self.inner_frame, width=18, style='Standard.TEntry')
        self.entry_sp_val = ttk.Entry(self.inner_frame, width=18, style='Standard.TEntry')
        self.entry_a_val = ttk.Entry(self.inner_frame, width=18, style='Standard.TEntry')
        self.entry_ku = ttk.Entry(self.inner_frame, width=18, style='Standard.TEntry')
        self.entry_kf = ttk.Entry(self.inner_frame, width=18, style='Standard.TEntry')
        self.entry_sr = ttk.Entry(self.inner_frame, width=18, style='Standard.TEntry')
        self.entry_lf = ttk.Entry(self.inner_frame, width=18, style='Standard.TEntry')

        # Adding entry unit labels
        self.mat_height_unit = ttk.Label(self.inner_frame, text='[m]', style='LeftAligned.TLabel')
        self.mat_rho_unit = ttk.Label(self.inner_frame, text='[g/cm3]', style='LeftAligned.TLabel')
        self.mat_w_grav_unit = ttk.Label(self.inner_frame, text='[%]', style='LeftAligned.TLabel')
        self.mat_sp_val_unit = ttk.Label(self.inner_frame, text='[unit]', style='LeftAligned.TLabel')
        self.mat_a_val_unit = ttk.Label(self.inner_frame, text='[unit]', style='LeftAligned.TLabel')
        self.mat_ku_unit = ttk.Label(self.inner_frame, text='[W/mK]', style='LeftAligned.TLabel')
        self.mat_kf_unit = ttk.Label(self.inner_frame, text='[W/mK]', style='LeftAligned.TLabel')
        self.mat_sr_unit = ttk.Label(self.inner_frame, text='[unit]', style='LeftAligned.TLabel')
        self.mat_lf_unit = ttk.Label(self.inner_frame, text='[unit]', style='LeftAligned.TLabel')

        # Packing entry name labels
        self.mat_name.grid(row=0, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_height.grid(row=1, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_rho.grid(row=2, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_w_grav.grid(row=3, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_sp_val.grid(row=4, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_a_val.grid(row=5, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_ku.grid(row=6, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_kf.grid(row=7, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_sr.grid(row=8, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')
        self.mat_lf.grid(row=9, column=0, padx=(10, 0), pady=(6, 0), sticky='ew')

        # Packing entry fields
        self.entry_name.grid(row=0, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_height.grid(row=1, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_rho.grid(row=2, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_w_grav.grid(row=3, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_sp_val.grid(row=4, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_a_val.grid(row=5, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_ku.grid(row=6, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_kf.grid(row=7, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_sr.grid(row=8, column=1, padx=(10, 0), pady=(6, 0))
        self.entry_lf.grid(row=9, column=1, padx=(10, 0), pady=(6, 0))

        # Packing entry unit labels
        self.mat_height_unit.grid(row=1, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_rho_unit.grid(row=2, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_w_grav_unit.grid(row=3, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_sp_val_unit.grid(row=4, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_a_val_unit.grid(row=5, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_ku_unit.grid(row=6, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_kf_unit.grid(row=7, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_sr_unit.grid(row=8, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')
        self.mat_lf_unit.grid(row=9, column=2, padx=(10, 10), pady=(6, 0), sticky='ew')

        # Add control buttons
        self.save_button = ttk.Button(self.inner_frame,
                                      width=20,
                                      text='Save',
                                      style='Standard.TButton',
                                      takefocus=False,
                                      command=self.save_new_material)
        self.save_button.grid(row=10, column=0, padx=(10, 0), pady=(14, 10), sticky='w')
        self.cancel_button = ttk.Button(self.inner_frame,
                                        width=20,
                                        text='Cancel',
                                        style='Standard.TButton',
                                        takefocus=False,
                                        command=self.cancel_operation)
        self.cancel_button.grid(row=10, column=1, columnspan=2, padx=(10, 0), pady=(14, 10), sticky='e')


    def save_new_material(self):
        material_name = self.entry_name.get()
        height = self.entry_height.get()
        rho = self.entry_rho.get()
        w_grav = self.entry_w_grav.get()
        sp_val = self.entry_sp_val.get()
        a_val = self.entry_a_val.get()
        ku = self.entry_ku.get()
        kf = self.entry_kf.get()
        sr = self.entry_sr.get()
        lf = self.entry_lf.get()

        def check_if_empty():
            check_list = [material_name, height, rho, w_grav, sp_val, a_val, ku, kf, sr, lf]
            for i in check_list:
                if i == "":
                    return False
            return True

        if check_if_empty():
            try:
                query = """INSERT INTO 'materials' (mat_name,
                                                    mat_height,
                                                    mat_rho,
                                                    mat_w_grav,
                                                    mat_sp_val,
                                                    mat_a_val,
                                                    mat_ku,
                                                    mat_kf,
                                                    mat_sr,
                                                    mat_lf) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                cur.execute(query, (material_name, height, rho, w_grav, sp_val, a_val, ku, kf, sr, lf))
                con.commit()
                messagebox.showinfo("Success", "Successfully added to database!", icon='info')

            except:
                messagebox.showerror("Error", "Can't add to database!", icon='warning')


        else:
            messagebox.showerror("Error", "Fields cannot be empty", icon='warning')

    def cancel_operation(self):
        self.destroy()