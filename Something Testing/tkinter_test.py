from tkinter import *

root = Tk()
top = Toplevel()

# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

screen_width = Toplevel().winfo_screenwidth()
screen_height = Toplevel().winfo_screenheight()

print('screen_width: ' + str(screen_width))
print('screen_height: ' + str(screen_height))
