import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

root = Tk()
root.geometry('1600x800')


def exitt():
    exit()


l = Label(root, text='Frostdata', font=('times', 19, 'bold'))
l.grid(row=0, column=0, sticky=SW, padx=2)

var = StringVar()
global sone

img = ImageTk.PhotoImage(Image.open("klimasoner.png"))
panel = Label(root, image=img)
panel.place(x=250, y=150)

temp_midd = StringVar()
temp_vinteramp = StringVar()
frost_dim = StringVar()
#print('cosinus:' + str(np.cos(np.pi / 4)))
sone = 'sone3'


def avslutt2():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    sone = var.get()
    # lb1 = Label(root, text="sone")
    # lb1.pack()
    print('del 2 - sone  ' + str(sone))


def beregn():
    global sone
    sone = var.get()
    #print('del 1 - sone  ' + str(sone))
    # l.config(text='you have selected ' + var.get())
    # l.pack()
    global temp_midd
    global temp_vinteramp
    global frost_dim
    temp_midd = v1.get()
    temp_vinteramp = v2.get()
    #temp_vinteramp = 12.0
    frost_dim = v3.get()

    #print('xxxxxxxxxxxxxxx  ' + str(temp_midd) + '   ' + str(temp_vinteramp) + '  ' + str(frost_dim))
    root.destroy()


# variabler
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

tk.Label(root, text="Mean annual temperature").grid(row=3, column=0, sticky=W, padx=2)
tk.Label(root, text="Normal winteramplitude").grid(row=4, column=0, sticky=W, padx=2)
tk.Label(root, text="Frost index (hC)").grid(row=5, column=0, sticky=W, padx=2)

e1 = tk.Entry(root, textvar=v1).grid(row=3, column=1, sticky=E, padx=2)
e2 = tk.Entry(root, textvar=v2).grid(row=4, column=1, sticky=E, padx=2)
e3 = tk.Entry(root, textvar=v3).grid(row=5, column=1, sticky=E, padx=2)

blank_linje = tk.Label(root, text=" ")
blank_linje.grid(row=6, column=0)

overskrift = tk.Label(root, text="Select temperature zone ", font=('times', 19, 'bold'))
overskrift.grid(row=7, column=0)

# soner
i = int(0)
values = {
    "Østlandet 1 ": 'sone1',
    "Østlandet 2  ": 'sone2',
    "Østlandet 3 ": 'sone3',
    "Høgfjellet 4 ": 'sone4',
    "Fjordstrøk og indrestrøk, vestkysten 5": 'sone5',
    "Fjordstrøk og indrestrøk, vestkysten 6": 'sone6',
    "Fjordstrøk og indrestrøk, vestkysten 7": 'sone7',
    "Indre Finnmark 8": 'sone8',
    "Vestkysten 9": 'sone9',
    "Vestkysten 10": 'sone10',
    "Vestkysten 11": 'sone11'}

for (text, value) in values.items():
    Radiobutton(root, text=text, variable=var,value=value).grid(row=15 + i, column=0, sticky=SW)
    # place(x = 10, y = 150+i*30, width=300, height=25, anchor=SW)
    i = i + 1

# bt1 = Button(root, text='Lagre', command=avslutt).pack(pady=10)

# print('inside - sone: ' + str(sone))


tk.Button(root, text='End', command=exitt).place(x=20, y=500)
# grid(row=200, column=0, sticky=E, padx=1)
tk.Button(root, text='Calculate', command=beregn).place(x=80, y=500)
# grid(row=200, column=1, sticky=E, padx=1)

root.mainloop()

rot = Tk()
rot.geometry('1600x1200')

# print('outside')

# print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# print('sone  ' + str(sone))
sone1 = {
    "konst1": 1.022,
    "dag1": -22,
    "konst2": 0.067,
    "dag2": 11
}
sone2 = {
    "konst1": 0.986,
    "dag1": -20,
    "konst2": 0.041,
    "dag2": 14
}
sone3 = {
    "konst1": 0.947,
    "dag1": -18,
    "konst2": 0.026,
    "dag2": -51
}
sone4 = {
    "konst1": 1.060,
    "dag1": -26,
    "konst2": 0.101,
    "dag2": -6
}
sone5 = {
    "konst1": 1.036,
    "dag1": -23,
    "konst2": 0.075,
    "dag2": 4
}
sone6 = {
    "konst1": 1.027,
    "dag1": -23,
    "konst2": 0.070,
    "dag2": -5
}
sone7 = {
    "konst1": 1.083,
    "dag1": -23,
    "konst2": 0.131,
    "dag2": -10
}
sone8 = {
    "konst1": 1.047,
    "dag1": -23,
    "konst2": 0.082,
    "dag2": -2
}
sone9 = {
    "konst1": 1.048,
    "dag1": -30,
    "konst2": 0.072,
    "dag2": -10
}
sone10 = {
    "konst1": 1.104,
    "dag1": -28,
    "konst2": 0.161,
    "dag2": -10
}
sone11 = {
    "konst1": 1.095,
    "dag1": -31,
    "konst2": 0.171,
    "dag2": -13
}

temp_sone = {
    "sone1": sone1,
    "sone2": sone2,
    "sone3": sone3,
    "sone4": sone4,
    "sone5": sone5,
    "sone6": sone6,
    "sone7": sone7,
    "sone8": sone8,
    "sone9": sone9,
    "sone10": sone10,
    "sone11": sone11
}

konst1 = temp_sone[sone]["konst1"]
dag1 = temp_sone[sone]["dag1"]
konst2 = temp_sone[sone]["konst2"]
dag2 = temp_sone[sone]["dag2"]
#tekst = ('c1: ' + str(konst1) + '  t1: ' + str(dag1) + '  c2: ' + str(konst2) + '  t2: ' + str(dag2) + ' t_m: ' + str(
#    temp_midd) + ' t_v: ' + str(temp_vinteramp) + ' f_d: ' + str(frost_dim))
# print('c1: '+ str(konst1) + '  t1: '+str(dag1)+'  c2: '+ str(konst2) + '  t2: '+str(dag2) + ' t_m: ' + str(temp_midd) + ' t_v: ' + str(temp_vinteramp) + ' f_d: ' + str(frost_dim))
tekst = "Equation: V(t) = Vm + (Vnav + dVva) * N(t) \n Vm - mean annual temperature \n Vnav - normal winter amplitude \n dVav - increase in design value for the winter amplitude  \n Winter amplitude = Vnav + dVav\n\n N(t) = c1 * cos(w*(t+t1)) + c2 cos(w*(t+t2))\n w - 2*PI/365 \n c1, c2 - amplitude 1. and 2. part \n t1, t2 - time delay from 1. July\nt - time (days)"


lab1 = tk.Label(rot, text="Koeffisienter for bruk i beregning av vinteramplirude")
labfont1 = ('times', 16, 'bold')
lab1.config(bg='white', fg='blue')
lab1.config(font=labfont1)
lab1.config(height=3, width=100)

lab1.grid(row=1, column=0, sticky=W, padx=2)

lab2 = tk.Label(rot, text=tekst)

labfont2 = ('times', 16, 'bold')
lab2.config(bg='blue', fg='white')
lab2.config(font=labfont2)
lab2.config(height=12, width=100)

lab2.grid(row=3, column=0, sticky=W, padx=2)

# print('c1:  ' + str(konst1) + '   c2:  ' + str(konst2))
konst1 = float(konst1)
dag1 = float(dag1)
konst2 = float(konst2)
dag2 = float(dag2)
temp_midd = float(temp_midd)
temp_vinteramp = float(temp_vinteramp)
norm_v_amp = float(temp_vinteramp)
frostm = float(0.0)
frost_dim = float(frost_dim)
tid = float()


def timegrader(temp_m, temp_v, c1, t1, c2, t2):
    frostm = 0.0
    for tid in range(0, 300, 1):
        var1 = c1 * (np.cos(2 * np.pi / 365 * (t1 + tid))) + c2 * (np.cos(4 * np.pi / 365 * (t2 + tid)))
        #print(f'norm_v_amp {norm_v_amp}')
        #print(f'temp_v {temp_v}')
        #if var1 >= 0:
        #    t_d = temp_m + norm_v_amp * var1
        #else:
        t_d = temp_m + temp_v * var1
        if t_d <= 0:
            frostm = frostm + t_d * 24

    return frostm


frost0 = -timegrader(temp_midd, temp_vinteramp, konst1, dag1, konst2, dag2)
frost1 = -timegrader(temp_midd, temp_vinteramp + 5.0, konst1, dag1, konst2, dag2)
print("Frostmengde 0 = ", frost0, "   Frostmengde 1 = ", frost1)

a = (frost1 - frost0) / 5.0
b = frost0 - a * temp_vinteramp
temp_v_dim = (frost_dim - b) / a

print("Dimensjonerende vinteramplitude ", temp_v_dim)

frost2 = -timegrader(temp_midd, temp_v_dim, konst1, dag1, konst2, dag2)
print(f'frost2 is {frost2}')

#print("Angitt dim. frostmengde xxxxxxxxxxxx = ", frost_dim, "   Beregnet dim. frostmengde xxxxxxxxxxxxx = ", frost2)
i = 0.0

if frost2 >= frost_dim:
    while i < 10.0:
        temp_v_dim = temp_v_dim - i
        frost2 = -timegrader(temp_midd, temp_v_dim, konst1, dag1, konst2, dag2)
        #print('Differanse: ', frost2 - frost_dim, 'i: ', i)
        i += 0.0001
        if (frost2 - frost_dim) < 5:
            #print("temp1", temp_v_dim, "diff", frost2 - frost_dim)
            break
else:
    while i < 10.0:
        temp_v_dim = temp_v_dim + i
        frost2 = -timegrader(temp_midd, temp_v_dim, konst1, dag1, konst2, dag2)
        #print('Differanse xxxxxxxxxx: ', frost2 - frost_dim, 'i: ', i)
        i += 0.0001
        if (frost2 - frost_dim) > -5:
            #print("temp2", temp_v_dim, "diff", frost2 - frost_dim)
            break

frost3 = -timegrader(temp_midd, temp_v_dim, konst1, dag1, konst2, dag2)
print("Frostmengde: ", frost3, "Dimensjonerende viteramplitude: ", temp_v_dim)


#tekst2 = ('Frostmengde: %6.2f gir dimensjonerende viteramplitude: %8.2f ' % (frost3, temp_v_dim))
#lab3 = tk.Label(rot, text=tekst2)
#labfont3 = ('times', 20, 'bold')
#lab3.config(bg='yellow', fg='blue')
##lab3.config(font=labfont1)
#lab3.config(height=3, width=100)

#lab3.grid(row=4, column=0, sticky=W, padx=2)

# tekst2=('Frostmengde: %6.2f gir dimensjonerende viteramplitude: %8.2f ' % (frost3, temp_v_dim))

tekst2 = (
            'c1: %2.3f, t1: %3d, c2: %2.3f, t2: %3d, mean annual temperature: %2.1f, winter amplitude: %3.2f -> FROST INDEX = %6.1f' % (
    konst1, dag1, konst2, dag2, temp_midd, temp_v_dim, frost3))
lab4 = tk.Label(rot, text=tekst2)
labfont4 = ('times', 12, 'bold')
lab4.config(bg='white', fg='black')
lab4.config(font=labfont1)
lab4.config(height=3, width=100)

lab4.grid(row=4, column=0, sticky=W, padx=2)

tk.Button(rot, text='Avslutt', command=exitt).place(x=50, y=700)

tid1 = np.arange(0.0, 365.0, 1.0)
n_f = konst1 * (np.cos(2 * np.pi / 365 * (dag1 + tid1))) + konst2 * (np.cos(4 * np.pi / 365 * (dag2 + tid1)))



variasjon1 = temp_midd + temp_v_dim * n_f

fig, ax = plt.subplots()
ax.plot(tid1, variasjon1)
ax.set(xlabel='Dager fra 1. juli', ylabel='Temperatur', title='Temperaturvariasjon')
ax.grid()
fig.savefig("test.png")
# plt.show()

img2 = ImageTk.PhotoImage(Image.open("test.png"))
panel2 = Label(rot, image=img2)
panel2.place(x=300, y=480)

rot.mainloop()
