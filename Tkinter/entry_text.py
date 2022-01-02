from tkinter import *

root = Tk()

e = Entry(root)
e.pack()
e.insert(22, 'Bla', )


def click_my_button():
    my_label = Label(root, text=e.get())
    my_label.pack()


my_button = Button(root, text='Click Me!', padx=50, pady=20, command=click_my_button)
my_button.pack()

root.mainloop()

'''
width=50
height=50
borderwidth=5
e.get()-return entry text 
e.insert(0,)- predefine text
'''
