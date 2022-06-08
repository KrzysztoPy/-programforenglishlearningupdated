from update.all_setting import MINIMAL_SUPPORTED_RESOLUTION_WIDTH_HEIGHT

screen_width, screen_height = None, None


def save_width_and_height_screen_resolution(root_tkinter_tk):
    global screen_width, screen_height
    if not (screen_width and screen_height):
        screen_width = root_tkinter_tk.winfo_screenwidth()
        screen_height = root_tkinter_tk.winfo_screenheight()


def return_screen_resolution_width_height():
    return screen_width, screen_height


def check_the_minimum_resolution_requirements():
    if screen_width >= MINIMAL_SUPPORTED_RESOLUTION_WIDTH_HEIGHT[0] and \
            screen_height >= MINIMAL_SUPPORTED_RESOLUTION_WIDTH_HEIGHT[1]:
        return True
    else:
        return False

# def central_position_for_main_window():
#     horizontal_position_on_screen = -(width_screen_resolution // -2) + (width_window_size // -2)
#     vertical_position_on_screen = -(height_screen_resolution // -2) + (height_window_size // -2)
