from tkinter import Tk, ttk

# from all_setting_for_gui.main_window_setting import main_window_name_text


def set_title(root, title_name):
    root.title(title_name)


def calculating_the_initial_size_of_the_main_window(width_screen_resolution, height_screen_resolution):
    width_main_window_size = -(width_screen_resolution // -2)
    height_main_window_size = -(height_screen_resolution // -4)

    return width_main_window_size, height_main_window_size


def calculating_middle_position_main_window_on_screen(width_screen_resolution, height_screen_resolution,
                                                      width_window_size,
                                                      height_window_size):
    horizontal_position_on_screen = -(width_screen_resolution // -2) + (width_window_size // -2)
    vertical_position_on_screen = -(height_screen_resolution // -2) + (height_window_size // -2)

    return horizontal_position_on_screen, vertical_position_on_screen


def set_geometry_main_window(root, calculating_the_initial_size_of_the_main_window,
                             calculating_middle_position_main_window_on_screen):
    width_window_size, height_window_size = calculating_the_initial_size_of_the_main_window()
    horizontal_position, vertical_position = calculating_middle_position_main_window_on_screen()

    root.geometry(f"{width_window_size}x{height_window_size}+{horizontal_position}+{vertical_position}")
