import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import wikipedia as wiki


root = tk.Tk()

# defining the size of the gui window
canvas = tk.Canvas(root, height=700, width=675)
canvas.pack()

# adding an image to the background using pillow library
bg_img = ImageTk.PhotoImage(Image.open('2.jpg'))
label_img = tk.Label(root, image=bg_img)
label_img.place(relwidth=1, relheight=1)


def clear():
    entry.delete(0, END)
    my_text.delete(0.0, END)


def search():
    try:
        data = wiki.page(entry.get())
        # clear the screen
        clear()

        my_text.insert(0.0, data.content)

    except Exception as e:
        clear()
        my_text.insert(0.0, e)


# create upper frame
frame1 = tk.LabelFrame(root, text='Search Wikipedia', font=('Arial', 12))
frame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

# create an entry box within frame1
entry = tk.Entry(frame1, font=('Arial', 15))
entry.place(relwidth=0.75, relheight=1)

# create a button within frame1
button = tk.Button(frame1, text='Search', font=('Arial', 15), command=search)
button.place(relx=0.78, rely=0, relwidth=0.2, relheight=1)


# Lower Frame
lower_frame = tk.Frame(root, bg='#80c1ff')
lower_frame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

# Vertical Scrollbar
scroll_bar = tk.Scrollbar(lower_frame)
scroll_bar.pack(side='right', fill='y')

# Horizontal Scrollbar
scroll_bar2 = tk.Scrollbar(lower_frame, orient='horizontal')
scroll_bar2.pack(side='bottom', fill='x')

# create a text box within lower_frame
my_text = tk.Text(lower_frame, yscrollcommand=scroll_bar.set, xscrollcommand=scroll_bar2.set, wrap='no')
my_text.pack(fill='both', expand='True')

# configuring the scrollbar
scroll_bar.config(command=my_text.yview)
scroll_bar2.config(command=my_text.xview)


# frame3
frame3 = tk.Frame(root, bg='#80c1ff')
frame3.place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.05)

# delete button within frame3
button = tk.Button(frame3, text='Clear the Screen', font=('Arial', 18), command=clear)
button.place(relheight=1, relwidth=1)


root.mainloop()

