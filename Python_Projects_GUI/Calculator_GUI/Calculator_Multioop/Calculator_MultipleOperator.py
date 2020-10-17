from tkinter import *
from tkinter import font
import tkinter.messagebox


root = Tk()
new_window = Toplevel(root)

root.title("Calculator")
new_window.title("History")
new_window.withdraw()


def click_event(number):
    e.config(state=NORMAL)
    text = e.get()
    e.delete(0, END)
    e.insert(0, text + str(number))
    e.config(state=DISABLED)

    
def equal():
    try:
        result = eval(e.get())
        with open('History.txt','a+') as f:
            f.write(f"{e.get()} = {result} \n")
        e.config(state=NORMAL)
        e.delete(0, END)
        e.insert(0, result)
        e.config(state=DISABLED)
    except SyntaxError:
        tkinter.messagebox.showerror("Invalid Syntax",f"Syntax error in {e.get()}")
        e.config(state=NORMAL)
        e.delete(0, END)
        e.config(state=DISABLED)


def history():
    new_window.deiconify()
    with open('History.txt',"r") as f:
        his = f.read()
    text.config(text=his)


def ok():
    new_window.withdraw()


def clear():
    e.config(state=NORMAL)
    e.delete(0, END)
    e.config(state = DISABLED)


p_font = font.Font(size=20)
text = Message(new_window)
e = Entry(font=p_font, width=40, state=DISABLED)

text.grid(row=0)
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

button_clear = Button(height=5, width=27, text="Clear", command=clear)
button_add = Button(height=5, width=27, text="+", command=lambda: click_event("+"))
button_subtract = Button(height=5, width=27, text="-", command=lambda: click_event("-"))
button_multiply = Button(height=5, width=27, text="x", command=lambda: click_event("*"))
button_divide = Button(height=5, width=27, text="/", command=lambda: click_event("/"))
button_exponential = Button(height=5, width=27, text="Exponent", command=lambda: click_event("**"))
button_remainder = Button(height=5, width=27, text="remainder", command=lambda: click_event("%"))
button_equal = Button(height=5, width=27, text="=", command=equal)
button_history = Button(height=2, width=84, text="History", command=history)
button_ok = Button(new_window,text="OK",command=ok)


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
button_history.grid(row=7, columnspan=3)
button_ok.grid(row=1)

root.mainloop()
