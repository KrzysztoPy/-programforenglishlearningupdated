from decorators.mian_window_decorators import rules_for_creating_the_name_of_the_main_window, \
    resctriction_for_minimal_screen_resolution


@rules_for_creating_the_name_of_the_main_window
def main_window_name_text():
    return "Program for english learning"


@resctriction_for_minimal_screen_resolution
def minimal_screen_resolution():
    MIN_SCREEN_WIDTH = 1024
    MIN_SCREEN_HEIGHT = 768
    return MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT


def minimal_screen_resolutely_for_messagebox(minimal_screen_resolution):
    min_screen_width, min_screen_height = minimal_screen_resolution()

    MIN_BOX_WIDTH_ = min_screen_width / 2
    MIN_BOX_HEIGHT = min_screen_height / 2

    return MIN_BOX_WIDTH_, MIN_BOX_HEIGHT


def rules_for_determining_the_size_of_the_main_window(width_screen_resolution, height_screen_resolution):
    width_main_window_size = -(width_screen_resolution // -2)
    height_main_window_size = -(height_screen_resolution // -4)

    return width_main_window_size, height_main_window_size


def set_middle_position_for_main_window(width_screen_resolution, height_screen_resolution, width_window_size,
                                        height_window_size):
    horizontal_position_on_screen = -(width_screen_resolution // -2) + (width_window_size // -2)
    vertical_position_on_screen = -(height_screen_resolution // -2) + (height_window_size // -2)

    return horizontal_position_on_screen, vertical_position_on_screen
