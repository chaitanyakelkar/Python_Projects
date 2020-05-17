from tkinter import *
from tkinter import messagebox
import json
import difflib

root = Tk()
data = json.load(open("data.json"))


def translator(word):
    if word in data:
        return data[word]
    elif bool(difflib.get_close_matches(word, data, 1, 0.7)):
        show = messagebox.askyesno(title="Approx. Word", message=f"Did you mean {difflib.get_close_matches(word, data, 1, 0.7)[0]}?")
        if show:
            return data[difflib.get_close_matches(word, data, 1, 0.7)[0]]
        else:
            return "Sorry, We don't have such word!"
    else:
        return "Sorry, We don't understand what you are saying!!"


def search():
    global output_label
    try:
        output_label.destroy()
        search_func()
    except NameError:
        search_func()


def search_func():
    global output_label
    final = ""
    user_input = entry_var.get()
    output = translator(user_input)
    output_label = Label(text="")
    output_label.grid(row=0, columnspan=3)
    if isinstance(output, str):
        output_label.configure(text=output)
    else:
        for word in output:
            final += word
        output_label.configure(text=final)


def clear():
    entry.delete(0, END)


button_search = Button(height=2, width=10, text="Search", command=search)
button_clear = Button(height=2, width=10, text="Clear", command=clear)
button_exit = Button(height=2, width=10, text="Exit", command=root.quit)
button_search.grid(row=2, column=0)
button_clear.grid(row=2, column=1)
button_exit.grid(row=2, column=2)

entry_var = StringVar()
entry = Entry(width=40, textvar=entry_var)
entry1 = Entry(width=40)
entry.grid(row=1, columnspan=3)
root.mainloop()
