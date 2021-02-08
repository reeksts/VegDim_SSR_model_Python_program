import tkinter as tk

class MenuBar(tk.Menu):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller  # controller is main.py

        # File menu options
        self.file_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(label="New..", command=self.new_file)
        self.file_menu.add_command(label="Open File...", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", command=self.save)
        self.file_menu.add_command(label="Save As...", command=self.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit)

        # Edit menu options
        self.edit_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Edit", menu=self.edit_menu)

        self.edit_menu.add_command(label="Edit", command=self.edit)

        # View menu options
        self.view_menu = tk.Menu(self,  tearoff=0)
        self.add_cascade(label="View", menu=self.view_menu)

        self.show_toolbar = tk.BooleanVar(value=True)
        self.show_file_explorer = tk.BooleanVar(value=True)
        self.show_figures = tk.BooleanVar(value=True)
        self.resizable_window = tk.BooleanVar(value=False)

        self.view_menu.add_checkbutton(onvalue=True,
                                       offvalue=False,
                                       label='Toolbar',
                                       variable=self.show_toolbar,
                                       command=lambda: self.controller.toolbar_on_off(self.show_toolbar.get()))
        self.view_menu.add_checkbutton(onvalue=True,
                                       offvalue=False,
                                       label='File explorer',
                                       variable=self.show_file_explorer)
        self.view_menu.add_checkbutton(onvalue=True,
                                       offvalue=False,
                                       label='Show figures',
                                       variable=self.show_figures,
                                       command=lambda: self.controller.show_hide_figures(self.show_figures.get()))
        self.view_menu.add_checkbutton(onvalue=True,
                                       offvalue=False,
                                       label='Resizable',
                                       variable=self.resizable_window,
                                       command=lambda: self.controller.resizable_window(self.resizable_window.get()))

        # Preferences menu options

        self.preferences_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Preferences", menu=self.preferences_menu)

        self.clim_mod_selec = tk.IntVar(value=1)
        self.climate_model = tk.Menu(self, tearoff=0)
        self.preferences_menu.add_cascade(label="Climate model", menu=self.climate_model)
        self.climate_model.add_radiobutton(label="General",
                                           value=1,
                                           variable=self.clim_mod_selec,
                                           command=self.switch_climate_model)
        self.climate_model.add_radiobutton(label="Special",
                                           value=2,
                                           variable=self.clim_mod_selec,
                                           command=self.switch_climate_model)

        self.flux_model_selection = tk.IntVar(value=1)
        self.flux_model = tk.Menu(self, tearoff=0)
        self.preferences_menu.add_cascade(label="Flux model", menu=self.flux_model)
        self.flux_model.add_radiobutton(label="By gradT",
                                           value=1,
                                           variable=self.flux_model_selection,
                                           command=self.switch_flux_model)
        self.flux_model.add_radiobutton(label="By flux",
                                           value=2,
                                           variable=self.flux_model_selection,
                                           command=self.switch_flux_model)


        # Help menu options
        self.help_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Help", menu=self.help_menu)

        self.help_menu.add_command(label="Documentation", command=self.documentation)
        self.help_menu.add_command(label="About", command=self.about)

    def new_file(self):
        pass

    def open_file(self):
        pass

    def save(self):
        pass

    def save_as(self):
        pass

    def exit(self):
        pass

    def edit(self):
        pass

    def documentation(self):
        pass

    def about(self):
        pass

    def switch_climate_model(self):
        self.controller.switch_climate_model(self.clim_mod_selec.get())

    def switch_flux_model(self):
        self.controller.switch_flux_model(self.flux_model_selection.get())