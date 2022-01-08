from tkinter import Tk

from Tkinter.new_tkinter.create_main_window import set_title, set_geometry_main_window, \
    calculating_the_initial_size_of_the_main_window, calculating_middle_position_main_window_on_screen
from all_setting_for_gui.main_window_setting import main_window_name_text, get_screen_result


def return_calculating_the_initial_size_of_the_main_window(root):
    width_size, height_size = get_screen_result(root)
    return calculating_the_initial_size_of_the_main_window(width_size, height_size)


def return_calculating_the_middle_position_for_main_window(root, main_window_width_and_height_size):
    return calculating_middle_position_main_window_on_screen(get_screen_result(root)[0],
                                                             get_screen_result(root)[1],
                                                             main_window_width_and_height_size[0],
                                                             main_window_width_and_height_size[1], )


def main_window_init(root, main_window_geometry, main_window_position):
    set_title(root, main_window_name_text())
    set_geometry_main_window(root, main_window_geometry, main_window_position)
