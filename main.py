from tkinter import *

# TEST PROGRRAM
# root = Tk()
# ttk.Button(root, text="Hello World").grid()
# root.mainloop()


window = Tk()
window.title("Hello")
window.geometry('200x200')

lbl = Label(window, text="Hello, Click this Button")
lbl.grid(column=0, row=0)

def clicked():
    lbl.configure(text="Button Clicked!")

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=1)

window.mainloop()