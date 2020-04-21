from tkinter import *

root = Tk()
first_no = 0
operator = ""


def click_event(number):
    text = e.get()
    e.delete(0, END)
    e.insert(0, text + str(number))


def add():
    global first_no, operator
    first_no = e.get()
    e.delete(0, END)
    operator = "add"


def subtract():
    global first_no, operator
    first_no = e.get()
    e.delete(0, END)
    operator = "subtract"


def multiply():
    global first_no, operator
    first_no = e.get()
    e.delete(0, END)
    operator = "multiply"


def divide():
    global first_no, operator
    first_no = e.get()
    e.delete(0, END)
    operator = "divide"


def equal():
    global first_no, operator
    second_no = e.get()
    e.delete(0, END)
    if operator == "add":
        result = int(first_no) + int(second_no)
    if operator == "subtract":
        result = int(first_no) - int(second_no)
    if operator == "multiply":
        result = int(first_no) * int(second_no)
    if operator == "divide":
        result = int(first_no) / int(second_no)
    e.insert(0, result)


e = Entry(width=40)
e.grid(row=0, columnspan=3)

button_1 = Button(height=5, width=10, text="1", command=lambda: click_event(1))
button_2 = Button(height=5, width=10, text="2", command=lambda: click_event(2))
button_3 = Button(height=5, width=10, text="3", command=lambda: click_event(3))
button_4 = Button(height=5, width=10, text="4", command=lambda: click_event(4))
button_5 = Button(height=5, width=10, text="5", command=lambda: click_event(5))
button_6 = Button(height=5, width=10, text="6", command=lambda: click_event(6))
button_7 = Button(height=5, width=10, text="7", command=lambda: click_event(7))
button_8 = Button(height=5, width=10, text="8", command=lambda: click_event(8))
button_9 = Button(height=5, width=10, text="9", command=lambda: click_event(9))
button_0 = Button(height=5, width=10, text="0", command=lambda: click_event(0))
button_clear = Button(height=5, width=22, text="Clear", command=lambda: e.delete(0, END))
button_add = Button(height=5, width=10, text="+", command=add)
button_subtract = Button(height=5, width=10, text="-", command=subtract)
button_multiply = Button(height=5, width=10, text="x", command=multiply)
button_divide = Button(height=5, width=10, text="/", command=divide)
button_equal = Button(height=5, width=22, text="=", command=equal)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_divide.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)

root.mainloop()
