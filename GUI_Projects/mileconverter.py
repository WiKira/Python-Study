from tkinter import *

window = Tk()

window.title("Mile to Km Converter")
window.minsize(width=250, height=50)
window.config(padx=20, pady=20)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)
label2 = Label(text="is equal to")
label2.grid(column=0, row=1)
label3 = Label(text="0")
label3.grid(column=1, row=1)
label4 = Label(text="Km")
label4.grid(column=2, row=1)

input_str = Entry(width=10)
input_str.insert(END, "0")
input_str.grid(column=1, row=0)


def calculate():
    value = input_str.get()
    if str.isnumeric(value):
        label3.config(text = f"{round(float(value) * 1.60934, 2)}")


calculate_button = Button()
calculate_button.config(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()
