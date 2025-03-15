import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data =  pd.read_csv('flash-card-project-start/data/french_words.csv')
dict_data = data.to_dict(orient='records')

english_word = ''



# ---------------------------- GENERATE NEXT CARD LOGIC ------------------------------- #
def next_card():
    global english_word

    current_card_data = random.choice(dict_data)
    
    english_word = current_card_data['English']
    
    canvas.itemconfig(language_text, text = 'French', fill ='black')
    canvas.itemconfig(word_text, text = current_card_data['French'], fill = 'black')
    canvas.itemconfig(canvas_image, image = front_img)

    # call the loop that gets the card flipped
    window.after(3000, func= flip_card)

# ----------------------------- CARD FLIP LOGIC ----------------------------------- #

def flip_card():
    """the logic for card flipping. It provides the English word."""

    # config the canvas text with the new english word
    canvas.itemconfig(word_text, text =  english_word, fill = 'white')

    # config the canvas language text
    canvas.itemconfig(language_text, text = 'English', fill = 'white')

    # config the canvas image
    canvas.itemconfig(canvas_image, image = back_img)


# ---------------------------- CREATE NEW FLASH CARD UI------------------------------- #
window = tk.Tk()
window.title('Flash Card App')
window.minsize(width=850, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# ---------------------------- CREATE CANVAS ------------------------------- #
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

front_img =  tk.PhotoImage(file='flash-card-project-start/images/card_front.png')
back_img = tk.PhotoImage(file='flash-card-project-start/images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=front_img)


# ---------------------------- CREATE TEXT ------------------------------- #
language_text = canvas.create_text(400, 150, fill= 'black', text='', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, fill= 'black', text='', font=('Arial', 60, 'bold'))

# call the first card using the next_card function
next_card()


# ---------------------------- CREATE BUTTONS ------------------------------- #
right_img = tk.PhotoImage(file='flash-card-project-start/images/right.png')
check_button = tk.Button(
    image=right_img,
    font=('Arial', 20, 'bold'),
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    border=0,
    command= next_card
    )
check_button.grid(row=1, column=0)


wrong_img = tk.PhotoImage(file='flash-card-project-start/images/wrong.png')
cancel_buttton = tk.Button(
    image=wrong_img,
    font=('Arial', 20, 'bold'),
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    border=0,
    command=next_card
    )
cancel_buttton.grid(row=1, column=1)


window.mainloop() # run the main event loop