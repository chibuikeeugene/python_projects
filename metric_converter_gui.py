import tkinter as tk

# creating window object
window = tk.Tk()
window.title('Mile to KM converter')
window.minsize(300, 150)
window.config(padx=50, pady=50)

def unit_converter():
    miles = float(user_input.get())
    km = miles * 1.609
    output_label.config(text=round(km, 2))

# adding an input field
user_input  = tk.Entry(width=10)
user_input.grid(row=0, column=1)

# adding a label
my_label = tk.Label(text= 'Miles', font=('Aerial', 24))
my_label.grid(row=0, column=2)

# adding a label
my_label = tk.Label(text= 'is equal to', font=('Aerial', 24))
my_label.grid(row=1, column=0)

# adding a label
output_label = tk.Label(text= 0, font=('Aerial', 24))
output_label.grid(row=1, column=1)

# adding a label
my_label = tk.Label(text= 'Km', font=('Aerial', 24))
my_label.grid(row=1, column=2)

# adding a button
submit_button = tk.Button(text= 'Calculate', command=unit_converter)
submit_button.grid(row=2, column=1)

# keeping the window up and running until a close action is performed
window.mainloop()