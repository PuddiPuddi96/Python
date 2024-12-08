from math import floor
from tkinter import Button, Canvas, Label, PhotoImage, Tk
from time import gmtime, strftime

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

LABEL_TITLE_FONT = (FONT_NAME, 50, "bold")
TIMER_TEXT_FONT = (FONT_NAME, 35, "bold")
LABEL_CHECK_MARKS_FONT = (FONT_NAME, 15, "bold")

reps = 0
timer = None

def get_time_formatting(seconds):
    return strftime("%M:%S", gmtime(seconds))

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0

    window.after_cancel(timer) # Stop the timer
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="Timer")
    label_check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_title.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_title.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        label_title.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    canvas.itemconfig(timer_text, text=get_time_formatting(count))
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = floor(reps / 2)
        for _ in range (work_sessions):
            marks += "✅"
        label_check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro Timer")
window.config(padx=100, pady=80, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg_img = PhotoImage(file="./asset/tomato.png")
canvas.create_image(100, 112, image=bg_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=TIMER_TEXT_FONT)
canvas.grid(row=1, column=1)

label_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=LABEL_TITLE_FONT)
label_title.grid(row=0, column=1)

button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
button_reset.grid(row=2, column=2)

label_check_marks = Label(fg=GREEN, bg=YELLOW, font=LABEL_CHECK_MARKS_FONT)
label_check_marks.grid(row=3, column=1)

window.mainloop()
