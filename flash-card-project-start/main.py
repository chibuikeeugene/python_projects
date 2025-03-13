import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data =  pd.read_csv('flash-card-project-start/data/french_words.csv')

# list_of_data_dict = data.to_dict(orient='records')
# print(data_dict[0])



# ---------------------------- GENERATE RANDOM WORD ------------------------------- #
def generate_random_french_word():
    random_word = random.choice(data['French'])
    canvas.itemconfig(language_text, text = 'French')
    canvas.itemconfig(french_word_text, text = random_word)
    return random_word

# ----------------------------- CARD FLIP LOGIC ----------------------------------- #

def flip_card():
    """the logic for card flipping. It provides the English word."""
    # call the french word generator function
    french_word =  generate_random_french_word()

    # get its English translation
    english_word = data[data['French'] == str(french_word)]['English']

    # config the canvas text with the new english word
    canvas.itemconfig(french_word_text, text =  english_word.values[0], fill = 'white')

    # config the canvas language text
    canvas.itemconfig(language_text, text = 'English', fill = 'white')

    # config the canvas image
    canvas.itemconfig(canvas_image, image = back_img)

    # window.after_cancel(card_flip_loop)

# ---------------------------- CREATE NEW FLASH CARD UI------------------------------- #
window = tk.Tk()
window.title('Flash Card App')
window.minsize(width=850, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# flip the card after 3 secs
card_flip_loop = window.after(3000, func= flip_card)


# ---------------------------- CREATE CANVAS ------------------------------- #
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

front_img =  tk.PhotoImage(file='flash-card-project-start/images/card_front.png')
back_img = tk.PhotoImage(file='flash-card-project-start/images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=front_img)

# ---------------------------- CREATE TEXT ------------------------------- #
language_text = canvas.create_text(400, 150, fill= 'black', text='french', font=('Arial', 40, 'italic'))
french_word_text = canvas.create_text(400, 263, fill= 'black', text='mois', font=('Arial', 60, 'bold'))


# ---------------------------- CREATE BUTTONS ------------------------------- #
right_img = tk.PhotoImage(file='flash-card-project-start/images/right.png')
check_button = tk.Button(
    image=right_img,
    font=('Arial', 20, 'bold'),
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    border=0,
    command= generate_random_french_word
    )
check_button.grid(row=1, column=0)

wrong_img = tk.PhotoImage(file='flash-card-project-start/images/wrong.png')
cancel_buttton = tk.Button(
    image=wrong_img,
    font=('Arial', 20, 'bold'),
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    border=0,
    command=generate_random_french_word
    )
cancel_buttton.grid(row=1, column=1)


window.mainloop() # run the main event loop