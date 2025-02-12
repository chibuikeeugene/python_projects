import tkinter as tk

# creating a TK window object
root_window = tk.Tk()
root_window.minsize(500, 500)
root_window.title('First GUI program')


#adding a label
my_label = tk.Label(text= 'Your main loop', font=('Aerial', 24))
my_label.pack() # get it to display on the window

#defining a function that retrieves the user's input
def retrieved_response():
    value = user_input.get()
    my_label.config(text=value)

# adding a button
submit_button = tk.Button(text= 'submit', command=retrieved_response)
submit_button.pack()

# adding an input field
user_input = tk.Entry()
user_input.pack()


# keep the window up and running until a close action is performed
root_window.mainloop()