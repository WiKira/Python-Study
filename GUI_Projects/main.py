import tkinter
from tkinter import *

window = Tk()

window.title("My first GUI Program :D")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100,y=200)
my_label.grid(column=0, row=0)

my_label["text"] = "New text 1"
my_label.config(text="New text 2", padx=50, pady=20)


def button_clicked():
    text = input_str.get()
    my_label.config(text=f"{text}")


button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button2 = Button(text="Button 2", command=button_clicked)
# button.pack()
button2.grid(column=2, row=0)

input_str = Entry(width=10)
input_str.insert(END, "String to begin with.")
# input_str.pack()
input_str.grid(column=3, row=2)

# multiline = Text(height=5, width=30)
# multiline.focus()
# multiline.insert(END, "Initial text just for lorem ipsum lopes abra cadabra num toque vira magica"
#                       "acredite que tudo é de verdade")
# print(multiline.get("1.0", END))
# multiline.pack()
#
#
# def spinbox_used():
#     print(spin.get())
#
#
# spin = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spin.pack()
#
#
# def scale_used(value):
#     print(value)
#
#
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
#
# def checkbutton_used():
#     print(checked_state.get())
#
#
# checked_state = IntVar()
# check = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# check.pack()
#
#
# def radio_used():
#     print(radio_state.get())
#
#
# radio_state = IntVar()
# radio_button1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
# radio_button1.pack()
# radio_button2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
# radio_button2.pack()
#
#
# def list_box_used(event):
#     print(list_box.get(list_box.curselection()))
#
#
# list_box = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana", "Pineapple"]
#
# for item in fruits:
#     list_box.insert(fruits.index(item), item)
#
# list_box.bind("<<ListboxSelect>>", list_box_used)
# list_box.pack()


window.mainloop()
