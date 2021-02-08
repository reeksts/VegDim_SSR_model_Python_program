import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def change_state():
    if str(button1['state']) == 'disabled':
        button1['state'] = 'normal'
        print(button1.state())
    elif button1['state'] == 'normal':
        (button1['state']) = 'disabled'
        print(button1.state())

button1 = ttk.Button(root, state='disabled', text='test')
button1.pack()

button2 = ttk.Button(root, text='change state', command=change_state)
button2.pack()

root.mainloop()