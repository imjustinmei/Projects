import tkinter as tk
from tkinter import font

root = tk.Tk()

coords = [[5, 1], [5, 2], [5, 3], [4, 1], [4, 2], [4, 3], [3, 1], [3, 2], [3, 3]]
opcoords = [[3, 4], [4, 4], [2, 2], [2, 3], [2, 4], [2, 1], [5, 4]]
operations = ["+", "-", "*", "/", "X", "x^2", "."]

decimal = True
exp = True

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.entry()
        for i, j in enumerate(opcoords):
            self.create_operations(operations[i], j)
        for i in range(0, 9):
            self.create_nums(i+1, coords[i])
        self.zero()
        self.clear()
        self.enter()
    
    def create_nums(self, value, coord):
        self.num = tk.Button(self)
        self.num["text"] = value
        self.num["command"] = lambda: self.append(value)
        self.num["width"] = 6
        self.num["height"] = 3
        self.num.config(font=("Helvetica", 9))
        self.num.grid(row = coord[0], column = coord[1])

    def create_operations(self, operation, coord):
        self.op = tk.Button(self)
        self.op["text"] = operation
        self.op["command"] = lambda: self.append(operation)
        self.op["width"] = 6
        self.op["height"] = 3
        self.op.config(font=("Helvetica", 9))
        self.op.grid(row = coord[0], column = coord[1])

    def zero(self):
        self.num = tk.Button(self)
        self.num["text"] = "0"
        self.num["command"] = lambda: self.append(0)
        self.num["width"] = 13
        self.num["height"] = 3
        self.num.config(font=("Helvetica", 9))
        self.num.grid(column = 1, row = 6, columnspan = 2)

    def entry(self):
        global text
        text = tk.StringVar()
        self.entry = tk.Entry(self, justify="right", textvariable=text, state="readonly")
        self.entry["width"] = 12
        self.entry.place(height = 10)
        self.entry.config(font=("Helvetica", 23))
        self.entry.grid(row = 1, column = 1, columnspan = 5)

    def enter(self):
        self.enter = tk.Button(self)
        self.enter["text"] = "="
        self.enter["command"] = lambda: self.ent()
        self.enter["width"] = 6
        self.enter["height"] = 3
        self.enter.grid(row = 6, column = 4)

    def clear(self):
        global text
        self.clear = tk.Button(self)
        self.clear["text"] = "CE"
        self.clear["command"] = lambda: text.set('')
        self.clear["width"] = 6
        self.clear["height"] = 3
        self.clear.config(font=("Helvetica", 9))
        self.clear.grid(row = 6, column = 3)

    def ent(self):
        global decimal, exp
        decimal, exp = True, True
        sol = eval(text.get())
        if len(str(sol)) > 12:
            text.set(sol[:12])
        else:
            text.set(sol)

    def append(self, x):
        global decimal, exp
        cur = text.get()
        if (len(cur)+1>12):
            return
        if str(x).isdigit():
            text.set(cur + str(x))
        elif (len(cur)+1>11):
                return
        elif x == ".":
            if decimal == True:
                decimal = False
                text.set(cur + str("."))
        elif cur == '':
            return
        elif x == 'x^2':
            if exp == True:
                exp = False
                text.set(cur + str('**'))
        elif x == 'X':
            text.set(cur[:-1])
        else:
            if cur[-1].isdigit():
                exp, decimal = True, True
                text.set(cur + str(x))
            else:
                text.set(cur[:-1] + str(x))

root.title("calculator")
root.maxsize(350,350)
root.minsize(350,350)
app = Application(master=root)
app.mainloop()