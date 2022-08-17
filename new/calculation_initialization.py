from tkinter import Tk

from decorators.mian_window_decorators import checking_if_the_downloaded_screen_resolution_is_higher_than_the_minimum
from new.calculation_size_and_position import calculating_the_initial_size_of_the_main_window
from new.settings import minimal_screen_resolution
import exit


# Checking: +
# @checking_if_the_downloaded_screen_resolution_is_higher_than_the_minimum
def get_screen_result(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    return screen_width, screen_height


def checking_if_the_downloaded_screen_resolution_is_higher_than_the_minimum(downloaded_screen_result):
    min_screen_width, min_screen_height = minimal_screen_resolution
    screen_width, screen_height = downloaded_screen_result

    if screen_width >= min_screen_width and \
            screen_height >= min_screen_height:
        return downloaded_screen_result
    else:
        exit.exit_program_with_error()
        raise RuntimeError("Your screen resolution is less than the minimum supported screen resolution.")


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
