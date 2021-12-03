
import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Python GUI")

a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)

def click_me():
    action.configure(text='Hello ' + name.get())
    print(number.get())

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)                          # column 0

action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=2, row=1)                                # <= change column to 2

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
# StringVar() 타입의 변수를 콤보 박스에 사용합니다.
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number)
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)                         # <= Combobox in column 1
number_chosen.current(0)

name_entered.focus()


win.mainloop()