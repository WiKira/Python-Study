from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo("Oops", "Please make sure you haven't left leave any fields empty!")
        return

    response = messagebox.askokcancel(title="website", message=f"These are the details entered: "
                                                    f"\nEmail: {username} \nPassword: {password} "
                                                    f"\nIs it ok to save?")
    if response:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as write_file:
                json.dump(new_data, write_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", mode="w") as write_file:
                json.dump(data, write_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_password():
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message=f"There's no password save yet.")
    else:
        website = entry_website.get()
        try:
            username = data[website]["username"]
            password = data[website]["password"]
        except KeyError:
            messagebox.showerror(title="Error", message=f"No password saved for {website}")
        else:
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(background="white", width=200, height=200, padx=50, pady=50)

canvas = Canvas(background="white", width=200, height=200, highlightthickness=0)
photo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_image)
canvas.grid(column=1, row=0)

lbl_website = Label(text="Website:", background="white", padx=5)
lbl_website.grid(column=0, row=1)
lbl_username = Label(text="Email/Username:", background="white", padx=5)
lbl_username.grid(column=0, row=2)
lbl_password = Label(text="Password:", background="white", padx=5)
lbl_password.grid(column=0, row=3)

entry_website = Entry(width=33, background="white")
entry_website.grid(column=1, row=1)
entry_website.focus()
entry_username = Entry(width=52, background="white")
entry_username.grid(column=1, row=2, columnspan=2)
entry_username.insert(0, "DEAFULT_EMAIL")
entry_password = Entry(width=33, background="white")
entry_password.grid(column=1, row=3)

button_search = Button(text="Search", width=15, background="white", command=search_password)
button_search.grid(column=2, row=1)
button_generate = Button(text="Generate Password", command=generate_password, background="white")
button_generate.grid(column=2, row=3)
button_add = Button(text="Add", padx=5, width=43, command=save_password, background="white")
button_add.grid(column=1, row=4, columnspan=2)




window.mainloop()
