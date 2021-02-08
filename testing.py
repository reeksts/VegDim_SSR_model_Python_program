import tkinter as tk
from tkinter import ttk

class NewFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()
        self.object_container = []

        self.label = tk.Label(self, text='buttons')
        self.label.grid(row=0, column=0)

        self.label = tk.Label(self, text='comboboxes')
        self.label.grid(row=0, column=1)

        for i in range(1, 6):
            new_combo = NewLineClass(self, i)
            new_combo.packing()
            self.object_container.append(new_combo)

    def delete_line(self, row):
        self.object_container[row - 1].destroying()
        del self.object_container[row - 1]
        print(row)
        print(len(self.object_container))
        for entry_line in self.object_container[row-1:]:
            print('yooo')
            #entry_line.row -= 1
            #entry_line.forgetting()
            #entry_line.packing()


    def print_line_number(self, row):
        print(row)


class NewLineClass():
    def __init__(self, parent, row):
        self.parent = parent
        self.row = row

        self.button = tk.Button(self.parent, text='delete',
                                command=lambda: self.parent.delete_line(self.row),
                                )
        self.combobox = ttk.Combobox(self.parent, values=[1, 2])
        self.combobox.bind('<<ComboboxSelected>>',
                           lambda x=self.row: self.parent.print_line_number(self.row))

    def packing(self):
        self.button.grid(row=self.row, column=0)
        self.combobox.grid(row=self.row, column=1)

    def destroying(self):
        self.button.destroy()
        self.combobox.destroy()

    def forgetting(self):
        self.button.grid_forget()
        self.combobox.grid_forget()

root = tk.Tk()
NewFrame(root)
root.mainloop()