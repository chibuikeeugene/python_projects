import tkinter as tk
from tkinter import messagebox




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_value = website_entry_.get()
    email_value = email_entry_.get()
    password_value = password_entry_.get()

    # validate if the user has left any field empty
    if len(website_value) == 0 or len(password_value) == 0:
        complete_input_dialog = messagebox.showinfo(title='Oops', message='Please make sure you haven\'t left any fields empty.')
        
    else:
        # show user if he/she is happy with the input
        dialog = messagebox.askokcancel(title=website_value, message=f'These are the details entered: \nEmail: {email_value}\nPassword: {password_value}\nIs it ok to save?')
        
        if dialog: # if the user is happy with the input - that is, if the user clicks 'ok'
            with open('password-manager/data.txt', 'a') as data:
                data.write(f'{website_value} | {email_value} | {password_value}\n')
                website_entry_.delete(0, tk.END)
                password_entry_.delete(0, tk.END)
                website_entry_.focus()

    
    

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk() # instantiate an object of the Tk class
window.title('Password Manager')
window.minsize(300, 300) # set the minimum size of the window
window.config(padx=50, pady=50) # set the padding of the window



canvas = tk.Canvas(window, height=200, width=200)
canvas.grid(row=0, column=1)


img =  tk.PhotoImage(file='password-manager/logo.png')
canvas.create_image(100, 100, image=img)        

# Labels
text_field_1 = tk.Label(text='Website:')
text_field_1.grid(row=1, column=0)

text_field_2 = tk.Label(text='Email/Username:')
text_field_2.grid(row=2, column=0)

text_field_3 = tk.Label(text='Password:')
text_field_3.grid(row=3, column=0)

# Entries
website_entry_ = tk.Entry(width=38, justify='left')
website_entry_.grid(row=1, column=1, columnspan=2)
website_entry_.focus()


email_entry_ = tk.Entry(width=38, justify='left')
email_entry_.grid(row=2, column=1, columnspan=2)
email_entry_.insert(0, 'spiky@gmail.com')


password_entry_ = tk.Entry(width=21)
password_entry_.grid(row=3, column=1)


# Buttons
password_button = tk.Button(text='Generate Password')
password_button.grid(row=3, column=2)

add_button =  tk.Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


tk.mainloop()