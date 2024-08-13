from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global REPS, TIMER
    window.after_cancel(str(TIMER))
    label_timer.config(text="Timer", foreground=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    label_check["text"] = ""
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global REPS
    REPS += 1

    if REPS % 2 == 1:
        count_down(WORK_MIN * 60)
        label_timer.config(text="Work", foreground=GREEN)
    elif REPS % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label_timer.config(text="Break", foreground=RED)
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label_timer.config(text="Break", foreground=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global REPS, TIMER
    count_min = count // 60
    count_seg = count % 60
    canvas.itemconfig(timer_text, text=str(f"{count_min:0>2}:{count_seg:0>2}"))
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if REPS % 2 == 0:
            label_check["text"] += "✓"

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)
window.config(background=YELLOW)

canvas = Canvas(width=206, height=224, background=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=photo_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

label_timer = Label(text="TIMER", font=(FONT_NAME, 56, "normal"), foreground=GREEN, background=YELLOW)
label_timer.grid(column=1, row=0)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

label_check = Label(text="", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 20, "bold"))
label_check.grid(column=1, row=3)


window.mainloop()