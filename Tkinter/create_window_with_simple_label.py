from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel_1 = Label(root, text='Hello World')
myLabel_2 = Label(root, text='My name is Krzysztof')

# Shoving it onto she screen
# Use grid when you want choose place for yours widget
# Use pack when you want only adding widget to main root
# You can't using pack and grid the same time.
myLabel_1.pack()
myLabel_2.pack()

# run loop
root.mainloop()
