from tkinter import ttk

from all_setting_for_gui.notebook_tab_setting import title_for_menu_tab


def create_notebook_widget(root):
    return ttk.Notebook(root)


def creating_frame_for_new_tab(notebook_widget, main_window_size, margin_size_for_new_tab):
    width_tab_size = main_window_size[0] - margin_size_for_new_tab[0]
    height_tab_size = main_window_size[1] - margin_size_for_new_tab[1]

    frame_for_new_tab = ttk.Frame(notebook_widget, width=width_tab_size, height=height_tab_size)
    return frame_for_new_tab


def append_new_tab_to_notebook(notebook_widget, frame_for_notebook_tab, tab_name):
    notebook_widget.add(frame_for_notebook_tab, text=tab_name())


def pack_notebook_widget(notebook_widget):
    notebook_widget.pack()
