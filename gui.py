import tkinter as tk

# creating a TK window object
root_window = tk.Tk()
root_window.minsize(500, 500)
root_window.title('First GUI program')
root_window.config(padx=20, pady=20) # adding padding across all elements(widgets) in our window

#defining a function that retrieves the user's input
def retrieved_response():
    value = user_input.get()
    my_label.config(text=value)

#adding a label
my_label = tk.Label(text= 'Your main loop', font=('Aerial', 24))
my_label.grid(row=0, column=0) # get it to display on the window
my_label.config(padx=50, pady=50)

# adding a button
submit_button = tk.Button(text= 'submit', command=retrieved_response)
submit_button.grid(row=2, column=2)

# adding a button
submit_button = tk.Button(text= 'type', command=retrieved_response)
submit_button.grid(row=1, column=3)

# adding an input field
user_input = tk.Entry()
user_input.grid(row=3, column=4,)


# keep the window up and running until a close action is performed
root_window.mainloop()