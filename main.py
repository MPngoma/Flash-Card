from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
words_to_learn = []
# ---------------------- GENERATE RANDOM WORDS ----------------------- #
try:
    with open("data/words_to_learn.csv") as file:
        words = pandas.read_csv(file)
except FileNotFoundError:
    with open("data/french_words.csv") as file:
        words = pandas.read_csv(file)
finally:
    to_learn = words.to_dict(orient="records")
    word = {}
def generate_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(flash_card, image=card_back_img)
    word = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=word["French"], fill="black")
    flip_timer = window.after(3000, func=flip)

# ---------------------------- FLIP CARD ----------------------------- #

def flip():
    global word
    card_front_img = PhotoImage(file="images/card_back.png")
    canvas.itemconfig(flash_card, image=card_front_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word["English"], fill="white")
# -------------------------- SAVE PROGRESS --------------------------- #
def is_known():
    to_learn.remove(word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_word()


# ------------------------------- UI --------------------------------- #
window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip)
card_back_img = PhotoImage(file="images/card_front.png")
canvas = Canvas(window, height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card = canvas.create_image(405, 250, image=card_back_img)
card_title = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=cross_img, command=generate_word)
wrong_btn.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
right_btn = Button(image=check_img, command=is_known)
right_btn.grid(row=1, column=1)

generate_word()
window.mainloop()

