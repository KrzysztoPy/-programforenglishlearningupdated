from tkinter import *

root = Tk()

var = IntVar()


def show():
    myLabel = Label(root, text=var.get()).pack()


check_box = Checkbutton(root, text='Check this box, I dare you!', variable=var).pack()

button = Button(root, text='Show selection', command=show).pack()

root.mainloop()
