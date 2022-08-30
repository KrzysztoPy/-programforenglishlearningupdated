import new.settings_and_remarks.general as general


def get_screen_result(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    return screen_width, screen_height


def calculating_the_size_of_the_main_window(screen_resolution):
    width_screen_resolution, height_screen_resolution = screen_resolution

    width_main_window_size = -(width_screen_resolution // -2)
    height_main_window_size = -(height_screen_resolution // -4)

    return width_main_window_size, height_main_window_size


def calculating_middle_position_main_window_on_screen(width_screen_resolution, height_screen_resolution,
                                                      width_window_size, height_window_size):
    horizontal_position_on_screen = -(width_screen_resolution // -2) + (width_window_size // -2)
    vertical_position_on_screen = -(height_screen_resolution // -2) + (height_window_size // -2)

    return horizontal_position_on_screen, vertical_position_on_screen
