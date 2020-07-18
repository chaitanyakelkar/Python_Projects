from tkinter import *
from tkinter import font

root = Tk()


def click_event(number):
    e.config(state=NORMAL)
    text = e.get()
    e.delete(0, END)
    e.insert(0, text + str(number))
    e.config(state=DISABLED)

    
def equal():
    e.config(state=NORMAL)
    result = eval(e.get())
    e.delete(0, END)
    e.insert(0, result)
    e.config(state=DISABLED)


p_font = font.Font(size=20)
e = Entry(font=p_font, width=40, state=DISABLED)
e.grid(row=0, columnspan=3, ipady=10)

button_1 = Button(height=5, width=27, text="1", command=lambda: click_event(1))
button_2 = Button(height=5, width=27, text="2", command=lambda: click_event(2))
button_3 = Button(height=5, width=27, text="3", command=lambda: click_event(3))
button_4 = Button(height=5, width=27, text="4", command=lambda: click_event(4))
button_5 = Button(height=5, width=27, text="5", command=lambda: click_event(5))
button_6 = Button(height=5, width=27, text="6", command=lambda: click_event(6))
button_7 = Button(height=5, width=27, text="7", command=lambda: click_event(7))
button_8 = Button(height=5, width=27, text="8", command=lambda: click_event(8))
button_9 = Button(height=5, width=27, text="9", command=lambda: click_event(9))
button_0 = Button(height=5, width=27, text="0", command=lambda: click_event(0))
button_clear = Button(height=5, width=27, text="Clear", command=lambda: e.delete(0, END))
button_add = Button(height=5, width=27, text="+", command=lambda: click_event("+"))
button_subtract = Button(height=5, width=27, text="-", command=lambda: click_event("-"))
button_multiply = Button(height=5, width=27, text="x", command=lambda: click_event("*"))
button_divide = Button(height=5, width=27, text="/", command=lambda: click_event("/"))
button_exponential = Button(height=5, width=27, text="Exponent", command=lambda: click_event("**"))
button_remainder = Button(height=5, width=27, text="remainder", command=lambda: click_event("%"))
button_equal = Button(height=5, width=27, text="=", command=equal)

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
button_clear.grid(row=5, column=2)
button_divide.grid(row=6, column=0)
button_remainder.grid(row=5, column=1)
button_exponential.grid(row=6, column=1)
button_equal.grid(row=6, column=2)

root.mainloop()
