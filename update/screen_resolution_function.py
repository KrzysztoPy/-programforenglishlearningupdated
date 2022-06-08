from update.all_setting import MINIMAL_SUPPORTED_RESOLUTION_WIDTH_HEIGHT, MAIN_WINDOW_RESOLUTION

screen_resolution_width, screen_resolution_height = None, None


def save_width_and_height_screen_resolution(root_tkinter_tk):
    global screen_resolution_width, screen_resolution_height
    if not (screen_resolution_width and screen_resolution_height):
        screen_resolution_width = root_tkinter_tk.winfo_screenwidth()
        screen_resolution_height = root_tkinter_tk.winfo_screenheight()


def return_screen_resolution_width_height():
    return screen_resolution_width, screen_resolution_height


def check_the_minimum_resolution_requirements():
    if screen_resolution_width >= MINIMAL_SUPPORTED_RESOLUTION_WIDTH_HEIGHT[0] and \
            screen_resolution_height >= MINIMAL_SUPPORTED_RESOLUTION_WIDTH_HEIGHT[1]:
        return True
    else:
        return False


def calculating_the_middle_position_on_screen():
    horizontal_position_on_screen = -(screen_resolution_width // -2) + (MAIN_WINDOW_RESOLUTION[0] // -2)
    vertical_position_on_screen = -(screen_resolution_height // -2) + (MAIN_WINDOW_RESOLUTION[1] // -2)
    return horizontal_position_on_screen, vertical_position_on_screen
