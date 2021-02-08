TOOLBAR_BACKGROUND = '#262626'
TOOLBAR_BORDER = '#4c4c4c'
TOOLBAR_BUTTON_PRESSED_BACKGROUND = '#b2b2b2'
TOOLBAR_BUTTON_ACTIVE_BACKGROUND = '#808080'

STANDARD_FRAME_BACKGROUND = '#404040'
STANDARD_LABEL_BACKGROUND = '#404040'
STANDARD_BUTTON_BACKGROUND = '#404040'
STANDARD_ENTRY_BACKGROUND = '#404040'

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

# Radiobutton colors
STANDARD_RADIOBUTTON_BACKGROUND = '#404040'
STANDARD_RADIOBUTTON_BACKGROUND_ACTIVE = '#808080'


# Image button colors
IMAGE_BUTTON_PRESSED_BACKGROUND = '#b2b2b2'
IMAGE_BUTTON_ACTIVE_BACKGROUND = '#808080'

# Checkbutton
STANDARD_CHECKBOX_UPPERBORDERCOLOR = '#262626'
STANDARD_CHECKBOX_LOWERBORDERCOLOR = '#262626'
STANDARD_CHECKBOX_BACKGROUND = '#404040'
STANDARD_CHECKBOX_ACTIVE_BACKGROUND = '#b2b2b2'
STANDARD_CHECKBOX_ACTIVE_INDICATORBACKGROUND = '#b2b2b2'
STANDARD_CHECKBOX_INDICATORBACKGROUND = '#808080'
STANDARD_CHECKBOX_INDICATORFOREGROUND = '#e5e5e5'

STANDARD_LABEL_FOREGROUND = '#e5e5e5'
STANDARD_BUTTON_FOREGROUND = '#e5e5e5'

STANDARD_BUTTON_PRESSED_BACKGROUND = '#b2b2b2'
STANDARD_BUTTON_ACTIVE_BACKGROUND = '#808080'

DARK_FRAME_BACKGROUND = '#262626'
DARK_LABEL_BACKGROUND = '#262626'

# Disabled Entry colors
DISABLED_ENTRY_FOREGROUND = '#bfbfbf'
DISABLED_ENTRY_FIELDBACKGROUND = '#595959'
DISABLED_ENTRY_LIGHTCOLOR = '#595959'
DISABLED_ENTRY_BORDERCOLOR = '#999999'

# Disabled Entry colors
WARNING_ENTRY_FOREGROUND = 'black'
WARNING_ENTRY_FIELDBACKGROUND = '#cc0000'
WARNING_ENTRY_LIGHTCOLOR = '#595959'
WARNING_ENTRY_BORDERCOLOR = '#999999'

class StyleConfiguration:
    def __init__(self, style):
        style.theme_use('clam')
        # print(style.theme_names())
        # print(style.theme_use())
        # style.theme_use('clam')

        # Shows the layout of a widget - this allows to know the elememnt of that widget
        # print(style.layout('TLabel'))

        # Then check the costumizable options of each of those elements
        # print(style.element_options('Label.border'))
        # print(style.element_options('Label.padding'))
        # print(style.element_options('Label.label'))

        # This allows to create a new custom style
        # style.configure('CustomEntryStyle.TEntry', padding=20)

        # style.configure("TLabel", bordercolor='#f00')
        # style.configure("TLabel", borderwidth=20)
        # style.configure("TLabel", relief='solid')

        # State specific options can be modified with map() function

        # Changing fonts
        # font.nametofont('TkDefaultFont').configure(size=15)

        # Font changing for entries, textbox and stuff like that:
        # font.nametofont('TkTextFont').configure(size=15)

        # Font families and making named font
        # print(font.families())
        # new_font = font.Font(family='Helvetica', size=15, weight='bold')

        # Toolbar style configuration
        style.configure('ToolBar.TFrame',
                        borderwidth=1,
                        relief='raised',
                        background=TOOLBAR_BACKGROUND,
                        lightcolor=TOOLBAR_BACKGROUND,
                        darkcolor=TOOLBAR_BACKGROUND,
                        bordercolor=TOOLBAR_BORDER)
        style.configure('ToolBar.TButton',
                        borderwidth=0,
                        relief='flat',
                        focusthickness=0,
                        padding=2,
                        background=TOOLBAR_BACKGROUND)
        style.map('ToolBar.TButton',
                  background=[('pressed', '!disabled', TOOLBAR_BUTTON_PRESSED_BACKGROUND),
                              ('active', TOOLBAR_BUTTON_ACTIVE_BACKGROUND)])

        # Standard Button configuration
        style.configure('Standard.TButton',
                        font=('Calibri', 10),
                        background=STANDARD_BUTTON_BACKGROUND,
                        foreground=STANDARD_LABEL_FOREGROUND,)
        style.map('Standard.TButton',
                  background=[('pressed', '!disabled', STANDARD_BUTTON_PRESSED_BACKGROUND),
                              ('active', STANDARD_BUTTON_ACTIVE_BACKGROUND)])

        # Standard Frame configuration
        style.configure('Standard.TFrame',
                        background=STANDARD_FRAME_BACKGROUND)

        # STANDARD_FRAME_BACKGROUND

        # Red Frame configuration
        style.configure('RedRed.TFrame,',
                        background='red')

        # Standard Label configuration
        style.configure('Standard.TLabel',
                        font=('Calibri', 10),
                        background=STANDARD_LABEL_BACKGROUND,
                        anchor='center',
                        foreground=STANDARD_LABEL_FOREGROUND)

        # Standard Entry configuration
        style.configure('Standard.TEntry',
                        foreground=STANDARD_ENTRY_FOREGROUND,)
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

        # Standard Checkbutton configuration
        style.configure('Standard.TCheckbutton',
                        focusthickness=0,
                        indicatorsize=12,
                        indicatormargin=3,
                        upperbordercolor=STANDARD_CHECKBOX_UPPERBORDERCOLOR,
                        lowerbordercolor=STANDARD_CHECKBOX_LOWERBORDERCOLOR,
                        indicatorbackground=STANDARD_CHECKBOX_INDICATORBACKGROUND,
                        indicatorforeground=STANDARD_CHECKBOX_INDICATORFOREGROUND,
                        background=STANDARD_CHECKBOX_BACKGROUND)
        style.map('Standard.TCheckbutton',
                  background=[('active', STANDARD_CHECKBOX_ACTIVE_BACKGROUND)],
                  indicatorbackground=[('active', STANDARD_CHECKBOX_ACTIVE_INDICATORBACKGROUND)])

        # Standard Radiobutton configuration
        style.configure('Standard.TRadiobutton',
                        padding=0,
                        background=STANDARD_RADIOBUTTON_BACKGROUND)
        style.map('Standard.TRadiobutton',
                  background=[('active', STANDARD_RADIOBUTTON_BACKGROUND_ACTIVE)])

        # Left aligned Label configuration
        style.configure('LeftAligned.TLabel',
                        font=('Calibri', 10),
                        background=STANDARD_LABEL_BACKGROUND,
                        foreground=STANDARD_LABEL_FOREGROUND,
                        justify='left',
                        anchor='w')

        # Left aligned Label and bold configuration
        style.configure('LeftAlignedBold.TLabel',
                        font=('Calibri', 10, 'bold'),
                        background=STANDARD_LABEL_BACKGROUND,
                        foreground=STANDARD_LABEL_FOREGROUND,
                        justify='left',
                        anchor='w')

        # Left aligned Label and small and large configuration
        style.configure('LeftAlignedSmall.TLabel',
                        font=('Calibri', 9),
                        background=STANDARD_LABEL_BACKGROUND,
                        foreground=STANDARD_LABEL_FOREGROUND,
                        justify='left',
                        anchor='w')

        # Left aligned and large and bold Label configuration
        style.configure('LeftAlignedLargeBold.TLabel',
                        font=('Calibri', 11, 'bold'),
                        background=STANDARD_LABEL_BACKGROUND,
                        foreground=STANDARD_LABEL_FOREGROUND,
                        justify='left',
                        anchor='w')

        # Large Label configuration:
        style.configure('LargeLabel.TLabel',
                        font=('Calibri', 11, 'bold'),
                        background=STANDARD_LABEL_BACKGROUND,
                        foreground=STANDARD_LABEL_FOREGROUND)

        # Extra large Label configuration:
        style.configure('ExtraLargeLabel.TLabel',
                        font=('Calibri', 13, 'bold'),
                        background=DARK_LABEL_BACKGROUND,
                        foreground=STANDARD_LABEL_FOREGROUND)


        # Dark frame configuration
        style.configure('DarkFrame.TFrame',
                        background=DARK_FRAME_BACKGROUND)

        # Dark and large label configuration
        style.configure('DarkLargeLabel.TLabel',
                        background=DARK_LABEL_BACKGROUND,
                        foreground=STANDARD_LABEL_FOREGROUND,
                        font=('Calibri', 11, 'bold'),
                        anchor='center')

        # Image button configuration
        style.configure('ImageButton.TButton',
                        borderwidth=0,
                        padding=2,
                        background=STANDARD_BUTTON_BACKGROUND)
        style.map('ImageButton.TButton',
                  background=[('pressed', '!disabled', IMAGE_BUTTON_PRESSED_BACKGROUND),
                              ('active', IMAGE_BUTTON_ACTIVE_BACKGROUND)])

        # Test Frame
        style.configure('Test.TFrame',
                        background='yellow')

        # Standard Entry configuration
        style.map('RedWarning.TEntry',
                  foreground=[('disabled', WARNING_ENTRY_FOREGROUND)],
                  fieldbackground=[('disabled', WARNING_ENTRY_FIELDBACKGROUND)],
                  lightcolor=[('disabled', WARNING_ENTRY_LIGHTCOLOR)],
                  bordercolor=[('disabled', WARNING_ENTRY_BORDERCOLOR)])

        # Standard Entry configuration
        style.map('DisabledEntry.TEntry',
                  foreground=[('disabled', DISABLED_ENTRY_FOREGROUND)],
                  fieldbackground=[('disabled', DISABLED_ENTRY_FIELDBACKGROUND)],
                  lightcolor=[('disabled', DISABLED_ENTRY_LIGHTCOLOR)],
                  bordercolor=[('disabled', DISABLED_ENTRY_BORDERCOLOR)])



        # Configuration dictionary for tk.Entry widget

        # Configuration dictionary for tk.Spinbox widget

        # CHECKING ALL THE OPTION HERE -------------------------------------------------------------------------------------

        #print(style.layout('TFrame'))
        #print(style.element_options('Frame.border'))
        #print(style.element_options('Frame.padding'))
        #print(style.element_options('Frame.fill'))

        #print(style.layout('TLabel'))
        #print(style.element_options('Label.border'))
        #print(style.element_options('Label.padding'))
        #print(style.element_options('Label.label'))

        #print(style.layout('TButton'))
        #print(style.element_options('Button.border'))
        #print(style.element_options('Button.focus'))
        #print(style.element_options('Button.padding'))
        #print(style.element_options('Button.label'))

        #print(style.layout('TCombobox'))
        #print(style.element_options('Combobox.downarrow'))
        #print(style.element_options('Combobox.field'))
        #print(style.element_options('Combobox.padding'))
        #print(style.element_options('Combobox.textarea'))

        #print(style.layout('TCheckbutton'))
        #print(style.element_options('Checkbutton.padding'))
        #print(style.element_options('Checkbutton.indicator'))
        #print(style.element_options('Checkbutton.focus'))
        #print(style.element_options('Checkbutton.label'))

        #print(style.layout('TSpinbox'))
        #print(style.element_options('Spinbox.field'))
        #print(style.element_options('Spinbox.uparrow'))
        #print(style.element_options('Spinbox.downarrow'))
        #print(style.element_options('Spinbox.padding'))
        #print(style.element_options('Spinbox.textarea'))

        #print(style.layout('TRadiobutton'))
        #print(style.element_options('TRadiobutton.padding'))
        #print(style.element_options('TRadiobutton.indicator'))
        #print(style.element_options('TRadiobutton.focus'))
        #print(style.element_options('TRadiobutton.label'))

        print(style.layout('TEntry'))
        print(style.element_options('TEntry.field'))
        print(style.element_options('TEntry.padding'))
        print(style.element_options('TEntry.textarea'))