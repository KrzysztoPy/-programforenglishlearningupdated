from tkinter import *

root = Tk()

top = Toplevel()

var = StringVar()


def show():
    myLabel = Label(top, text=var.get()).pack()


check_box = Checkbutton(top, text='Check this box, I dare you!', variable=var, onvalue='On', offvalue='Off').pack()

button = Button(top, text='Show selection', command=show).pack()

root.mainloop()
