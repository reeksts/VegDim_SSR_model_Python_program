import tkinter as tk
from tkinter import ttk
import tkinter.font as font


# Frame colors
STANDARD_FRAME_BACKGROUND = '#404040'

# Label colors
STANDARD_LABEL_BACKGROUND = '#404040'
STANDARD_LABEL_FOREGROUND = '#e5e5e5'

# Entry colors
STANDARD_ENTRY_FOREGROUND = '#e5e5e5'
STANDARD_ENTRY_BORDER_FOCUS = '#b2b2b2'
STANDARD_ENTRY_BORDER_NOT_FOCUS = '#b2b2b2'
STANDARD_ENTRY_FIELDBACKGROUND_FOCUS = '#404040'
STANDARD_ENTRY_FIELDBACKGROUND_NOT_FOCUS = '#404040'
STANDARD_ENTRY_LIGHTCOLOR_FOCUS = '#404040'
STANDARD_ENTRY_LIGHTCOLOR_NOT_FOCUS = '#404040'
STANDARD_ENTRY_SELECT_BACKGROUND_FOCUS = '#e5e5e5'
STANDARD_ENTRY_SELECT_FOREGROUND_FOCUS = '#404040'
STANDARD_ENTRY_SELECT_BACKGROUND_NOT_FOCUS = '#404040'
STANDARD_ENTRY_SELECT_FOREGROUND_NOT_FOCUS = '#e5e5e5'

# Combobox colors
STANDARD_COMBOBOX_BORDER = '#b2b2b2'
STANDARD_COMBOBOX_DARKCOLOR = '#404040'
STANDARD_COMBOBOX_LIGHTCOLOR = '#404040'
STANDARD_COMBOBOX_ARROW_COLOR = '#404040'
STANDARD_COMBOBOX_FIELD_BACKGROUND_FOCUS = '#404040'
STANDARD_COMBOBOX_FIELD_BACKGROUND_NOT_FOCUS = '#404040'
STANDARD_COMBOBOX_SELECT_FOREGROUND_FOCUS = '#e5e5e5'
STANDARD_COMBOBOX_SELECT_FOREGROUND_NOT_FOCUS = '#e5e5e5'
STANDARD_COMBOBOX_SELECT_BACKGROUND_FOCUS = '#404040'
STANDARD_COMBOBOX_SELECT_BACKGROUND_NOT_FOCUS = '#404040'
STANDARD_COMBOBOX_ARROW_BACKGROUND = '#b2b2b2'
STANDARD_COMBOBOX_ARROW_BACKGROUND_ACTIVE = '#f2f2f2'
STANDARD_COMBOBOX_FOREGROUND = '#e5e5e5'

# Spinbox colors
STANDARD_SPINBOX_BORDER = '#b2b2b2'
STANDARD_SPINBOX_FIELDBACKGROUND = '#404040'
STANDARD_SPINBOX_FOREGROUND = '#e5e5e5'
STANDARD_SPINBOX_LIGHTCOLOR = '#404040'
STANDARD_SPINBOX_DARKCOLOR = '#404040'
STANDARD_SPINBOX_ARROW_BACKGROUND = '#b2b2b2'
STANDARD_SPINBOX_ARROW_BACKGROUND_ACTIVE = '#f2f2f2'
STANDARD_SPINBOX_ARROW_COLOR = '#404040'
STANDARD_SPINBOX_SELECT_BACKGROUND_FOCUS = '#e5e5e5'
STANDARD_SPINBOX_SELECT_FOREGROUND_FOCUS = '#404040'
STANDARD_SPINBOX_SELECT_BACKGROUND_NOT_FOCUS = '#404040'
STANDARD_SPINBOX_SELECT_FOREGROUND_NOT_FOCUS = '#e5e5e5'


STANDARD_BUTTON_PRESSED_BACKGROUND = '#b2b2b2'
STANDARD_BUTTON_ACTIVE_BACKGROUND = '#808080'

# Radiobutton colors
STANDARD_RADIOBUTTON_BACKGROUND = '#404040'
STANDARD_RADIOBUTTON_BACKGROUND_ACTIVE = '#808080'


root = tk.Tk()
root.geometry('300x300+600+600')

style = ttk.Style()
style.theme_use('clam')

print(style.layout('TRadiobutton'))
print(style.element_options('TRadiobutton.padding'))
print(style.element_options('TRadiobutton.indicator'))
print(style.element_options('TRadiobutton.focus'))
print(style.element_options('TRadiobutton.label'))

standard_spinbox_font = font.nametofont('TkTextFont').copy()
standard_spinbox_font.configure(family='Calibri', size=10)

standard_entry_font = font.nametofont('TkTextFont').copy()
standard_entry_font.configure(family='Calibri', size=10)

# Standard Label configuration
style.configure('Standard.TLabel',
                font=('Calibri', 10),
                background=STANDARD_LABEL_BACKGROUND,
                anchor='center',
                foreground=STANDARD_LABEL_FOREGROUND)

# Standard Frame configuration
style.configure('Standard.TFrame',
                 background=STANDARD_FRAME_BACKGROUND)

# Standard Frame configuration
style.configure('Standard.TSpinbox',
                 background=STANDARD_FRAME_BACKGROUND)

# Standard Entry configuration
style.configure('Standard.TEntry',
                foreground=STANDARD_ENTRY_FOREGROUND)
style.map('Standard.TEntry',
          fieldbackground=[('focus', STANDARD_ENTRY_FIELDBACKGROUND_FOCUS),
                           ('!focus', STANDARD_ENTRY_FIELDBACKGROUND_NOT_FOCUS)],
          lightcolor=[('focus', STANDARD_ENTRY_LIGHTCOLOR_FOCUS),
                      ('!focus', STANDARD_ENTRY_LIGHTCOLOR_NOT_FOCUS)],
          bordercolor=[('focus', STANDARD_ENTRY_BORDER_FOCUS),
                      ('!focus', STANDARD_ENTRY_BORDER_NOT_FOCUS)],
          selectbackground=[('focus', STANDARD_ENTRY_SELECT_BACKGROUND_FOCUS),
                            ('!focus', STANDARD_ENTRY_SELECT_BACKGROUND_NOT_FOCUS)],
          selectforeground=[('focus', STANDARD_ENTRY_SELECT_FOREGROUND_FOCUS),
                            ('!focus', STANDARD_ENTRY_SELECT_FOREGROUND_NOT_FOCUS)])

# Standard Radiobutton configuration
style.configure('Standard.TRadiobutton',
                padding=0,
                background=STANDARD_RADIOBUTTON_BACKGROUND)
style.map('Standard.TRadiobutton',
          background=[('active', STANDARD_RADIOBUTTON_BACKGROUND_ACTIVE)])

# Standard Spinbox configuration
style.configure('Standard.TSpinbox',
                bordercolor=STANDARD_SPINBOX_BORDER,
                fieldbackground=STANDARD_SPINBOX_FIELDBACKGROUND,
                lightcolor=STANDARD_SPINBOX_LIGHTCOLOR,
                darkcolor=STANDARD_SPINBOX_DARKCOLOR,
                arrowsize=11,
                arrowcolor=STANDARD_SPINBOX_ARROW_COLOR,
                background=STANDARD_SPINBOX_ARROW_BACKGROUND,
                foreground=STANDARD_SPINBOX_FOREGROUND)
style.map('Standard.TSpinbox',
          selectbackground=[('focus', STANDARD_SPINBOX_SELECT_BACKGROUND_FOCUS),
                            ('!focus', STANDARD_SPINBOX_SELECT_BACKGROUND_NOT_FOCUS)],
          selectforeground=[('focus', STANDARD_SPINBOX_SELECT_FOREGROUND_FOCUS),
                            ('!focus', STANDARD_SPINBOX_SELECT_FOREGROUND_NOT_FOCUS)],
          background=[('active', STANDARD_SPINBOX_ARROW_BACKGROUND_ACTIVE)])

# Standard Combobox configuration
style.configure('Standard.TCombobox',
                arrowsize=15,
                background=STANDARD_COMBOBOX_ARROW_BACKGROUND,
                bordercolor=STANDARD_COMBOBOX_BORDER,
                darkcolor=STANDARD_COMBOBOX_DARKCOLOR,
                lightcolor=STANDARD_COMBOBOX_LIGHTCOLOR,
                arrowcolor=STANDARD_COMBOBOX_ARROW_COLOR)
style.map('Standard.TCombobox',
          fieldbackground=[('focus', STANDARD_COMBOBOX_FIELD_BACKGROUND_FOCUS),
                            ('!focus', STANDARD_COMBOBOX_FIELD_BACKGROUND_NOT_FOCUS)],
          selectforeground=[('focus', STANDARD_COMBOBOX_SELECT_FOREGROUND_FOCUS),
                            ('!focus', STANDARD_COMBOBOX_SELECT_FOREGROUND_NOT_FOCUS)],
          selectbackground=[('focus', STANDARD_COMBOBOX_SELECT_BACKGROUND_FOCUS),
                            ('!focus', STANDARD_COMBOBOX_SELECT_BACKGROUND_NOT_FOCUS)],
          foreground=[('!focus', STANDARD_COMBOBOX_FOREGROUND)],
          background=[('active', STANDARD_COMBOBOX_ARROW_BACKGROUND_ACTIVE)])



frame = ttk.Frame(root, style='Standard.TFrame')
frame.pack(fill='both', expand=True)


spinbox = ttk.Spinbox(frame,
                      font=standard_spinbox_font,
                      from_=0.01, to=10, format="%.2f", increment=0.01, style='Standard.TSpinbox')
spinbox.pack(pady=(20, 0))

entry = ttk.Entry(frame, style='Standard.TEntry', font=standard_entry_font)
entry.pack(pady=(20, 0))

var = tk.StringVar()
radiobutton1 = ttk.Radiobutton(frame, takefocus=False, variable=var, value='1', style='Standard.TRadiobutton')
radiobutton1.pack(pady=(20, 0))

radiobutton2 = ttk.Radiobutton(frame, takefocus=False, variable=var, value='2', style='Standard.TRadiobutton')
radiobutton2.pack(pady=(20, 0))

var2 = tk.StringVar()
radiobutton3 = tk.Radiobutton(frame, variable=var2, value='3', fg='blue', bg='green',
                            activebackground='pink', activeforeground='red', selectcolor='yellow')
radiobutton3.pack(pady=(20, 0))
radiobutton4 = tk.Radiobutton(frame, variable=var2, value='4', fg='yellow', bg='green',
                            activebackground='green', activeforeground='yellow', selectcolor='green')
radiobutton4.pack(pady=(20, 0))


combobox1 = ttk.Combobox(frame, values=[1, 2, 3], state='readonly', style='Standard.TCombobox')
combobox1.pack(pady=(20, 0))

combobox2 = ttk.Combobox(frame, values=[1, 2, 3], state='readonly', style='Standard.TCombobox')
combobox2.pack(pady=(20, 0))







root.mainloop()