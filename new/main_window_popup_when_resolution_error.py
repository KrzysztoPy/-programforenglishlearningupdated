import calculation_size_and_position_main_window as calc
from new.tkinter import setting_tkinter


def create_mian_window_error(root, screen_resolution, error_title):
    window_width, window_height = calc.calculating_the_size_of_the_main_window(
        screen_resolution)
    horizontal_position_on_screen, vertical_position_on_screen = calc.calculating_middle_position_main_window_on_screen(
        screen_resolution[0], screen_resolution[1], window_width, window_height)

    setting_tkinter.set_title(error_title)
    setting_tkinter.set_geometry_main_window(root, window_width, window_height, horizontal_position_on_screen,
                                             vertical_position_on_screen)
