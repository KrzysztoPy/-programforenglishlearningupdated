from tkinter import ttk

from all_setting_for_gui.main_window_setting import main_window_name
from decorators.mian_window_decorators import rules_for_creating_the_name_of_the_main_window, \
    resctriction_for_minimal_screen_resolution


def set_title(root):
    root.title(main_window_name())


def get_screen_result(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    return screen_width, screen_height


def set_window_size():
    pass
