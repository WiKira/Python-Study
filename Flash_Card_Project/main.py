import time

import pandas
import random
from tkinter import *

WORDS_DICT = {}
current_card = {}
EVENT_ID = None
data = pandas.DataFrame()

def import_data():
    global WORDS_DICT
    try:
        data = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        data = pandas.read_csv("data/french_words.csv")
    finally:
        WORDS_DICT = data.to_dict(orient='records')


def is_known():
    WORDS_DICT.remove(current_card)

    df = pandas.DataFrame(WORDS_DICT)
    df.to_csv("data/words_to_learn.csv", mode="w", index=False)
    change_card()

def change_card():
    global EVENT_ID, current_card
    window.after_cancel(str(EVENT_ID))

    current_card = random.choice(WORDS_DICT)

    canvas.itemconfig(lbl_title, text="French", fill="black")
    canvas.itemconfig(lbl_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card, image=front_image)

    EVENT_ID = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(lbl_title, text="English", fill="white")
    canvas.itemconfig(lbl_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card, image=back_image)


BACKGROUND_COLOR = "#B1DDC6"


import_data()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

canvas = Canvas(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 265, image=front_image)
lbl_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
lbl_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

button_wrong = Button(image=wrong_image, highlightthickness=0, background=BACKGROUND_COLOR, command=change_card)
button_wrong.grid(column=0, row=1)

button_right = Button(image=right_image, highlightthickness=0, background=BACKGROUND_COLOR, command=is_known)
button_right.grid(column=1, row=1)

change_card()

window.mainloop()
