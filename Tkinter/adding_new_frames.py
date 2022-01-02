from tkinter import *

root = Tk()
frame = LabelFrame(root, text='New frames', padx=50, pady=50)
text = Label(frame, text='Nothing but ALL')
button = Button(frame, text='BLABLABLA', state=DISABLED)
frame.pack(padx=10, pady=10)
text.pack()
button.pack()

root.mainloop()
