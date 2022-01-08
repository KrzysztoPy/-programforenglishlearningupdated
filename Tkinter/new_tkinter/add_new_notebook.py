from tkinter import ttk


def create_notebook_widget(root):
    return ttk.Notebook(root)


# Problem z tym że przesłane została rodzielczość ekranu a ma zostać przesłana rodzielczość okna głównego
def creating_frame_for_new_notebook_tab(notebook_widget, ):
    width_size, height_size = size_new_tab_frame()
    new_tab = Frame(notebook_widget, width=width_size, height=height_size)
    return new_tab


def set_name_new_notebook_tab(notebook_widget, frame_for_notebook_tab, tab_name):
    notebook_widget.add(frame_for_notebook_tab, text=tab_name())


def pack_notebook_widget(notebook_widget):
    notebook_widget.pack(expand=True, fill=NONE)
