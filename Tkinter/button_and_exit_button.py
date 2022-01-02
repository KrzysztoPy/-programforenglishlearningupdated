from tkinter import *

root = Tk()


def click_my_button():
    my_label = Label(root, text="You clicked button")
    my_label.pack()


my_button = Button(root, text='Click Me!', padx=50, pady=20, command=click_my_button, fg='blue', bg='red')
my_button.pack()

button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()

root.mainloop()

'''Available parameters
padx=50 - width
pady=50 - height
state=DISABLED - setting button status
command=function_name - 
fg='blue' - Change text color
bg='red - Change background color
'''
