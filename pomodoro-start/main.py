import tkinter as tk
import math
from timeit import default_timer as timer
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 #25
SHORT_BREAK_MIN = 0.1#5
LONG_BREAK_MIN = 0.5 #20
reps =  0
timer_countdown = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_countdown) # stopping the timer
    promodoro_canvas.itemconfig(timer_text, text='00:00') # resetting the timer
    check_marks.config(text='') # resetting the check marks
    title_Label.config(text='Timer', fg=GREEN) # resetting the title
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_min_secs = WORK_MIN * 60
    short_break_min_secs = SHORT_BREAK_MIN * 60
    long_break_min_secs = LONG_BREAK_MIN * 60
    
    # if it's the 8th rep
    if reps % 8 == 0:
        count_down(long_break_min_secs)
        title_Label.config(text='Break', fg=RED)
    # if it's the 2nd, 4th, 6th rep
    elif reps % 2 == 0:
        count_down(short_break_min_secs)
        title_Label.config(text='Break', fg=PINK)
    else:
        # if it's the 1st, 3rd, 5th, 7th rep
        count_down(work_min_secs)
        title_Label.config(text='Work', fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    elif count_sec < 10:
        count_sec = f'0{count_sec}'
    promodoro_canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}') # printing the count
    if count > 0:
        global timer_countdown
        timer_countdown = window.after(1000, count_down, count - 1) # calling the function after 1000ms
    else:
        start_timer()
        if reps % 2 == 0:
            check_marks.config(text='✔' * int(reps / 2))

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk() # creating window object
window.title('Pomodoro')
window.minsize(400, 400) # setting the minimum size of the window
window.config(padx=100, pady=50, bg=YELLOW)

title_Label = tk.Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50)) # creating a label object
title_Label.grid(row=0, column=1) # adding the label to the window

promodoro_canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # creating a canvas object
tomato_img = tk.PhotoImage(file='pomodoro-start/tomato.png') # loading the image
promodoro_canvas.create_image(100, 112, image=tomato_img) # adding the image to the canvas
promodoro_canvas.grid(row=1, column=1) # adding the canvas to the window

timer_text = promodoro_canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold')) # adding text to the canvas


start_button = tk.Button(text='Start', highlightthickness=0, command=start_timer) # creating a button object
start_button.grid(row=2, column=0) # adding the button to the window


reset_button = tk.Button(text='Reset', highlightthickness=0, command=reset_timer) # creating a button object
reset_button.grid(row=2, column=2) # adding the button to the window

check_marks = tk.Label( fg=GREEN, bg=YELLOW) # creating a label object
check_marks.grid(row=3, column=1) # adding the label to the window






window.mainloop() # keeping the window up and running until a close action is performed