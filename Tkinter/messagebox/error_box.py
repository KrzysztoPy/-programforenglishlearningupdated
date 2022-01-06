from tkinter import messagebox


def show_error_messagebox(top_root, geometry, error_reason, message):
    top_root.geometry(geometry)
    message.showerror(error_reason, message)


