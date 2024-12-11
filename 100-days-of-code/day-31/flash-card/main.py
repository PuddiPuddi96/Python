from pandas import read_csv, DataFrame
from random import choice
from tkinter import Button, Canvas, PhotoImage, Tk

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
PAUSE_TIME = 3000

# ---------------------------- GLOBAL VALUES ------------------------------- #
current_card = {}
flip_timer = None
to_learn = {}

# ---------------------------- UTILS ------------------------------- #
def go_to_next_card():
    global current_card, flip_timer
    
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    
    flip_timer = window.after(PAUSE_TIME, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    
    words_to_learn = DataFrame(to_learn)
    words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    
    go_to_next_card()

# ---------------------------- LOAD DATA ------------------------------- #
try:
    data = read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- SETUP UI ------------------------------- #
window = Tk()

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(PAUSE_TIME, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)

canvas.grid(row=0, column=0, columnspan=2)

wrong_button_image = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_button_image, highlightthickness=0, bd=0, command=go_to_next_card)
button_wrong.grid(row=1, column=0)

right_button_image = PhotoImage(file="./images/right.png")
button_right = Button(image=right_button_image, highlightthickness=0, bd=0, command=is_known)
button_right.grid(row=1, column=1)

go_to_next_card()

window.mainloop()
