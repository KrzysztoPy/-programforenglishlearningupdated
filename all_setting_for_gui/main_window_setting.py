from decorators.mian_window_decorators import rules_for_creating_the_name_of_the_main_window, \
    resctriction_for_minimal_screen_resolution, checking_if_the_downloaded_screen_resolution_is_higher_than_the_minimum


@rules_for_creating_the_name_of_the_main_window
def main_window_name_text():
    return "Program for english learning"


@resctriction_for_minimal_screen_resolution
def minimal_screen_resolution():
    MIN_SCREEN_WIDTH = 1024
    MIN_SCREEN_HEIGHT = 768
    return MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT


@checking_if_the_downloaded_screen_resolution_is_higher_than_the_minimum
def get_screen_result(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    return screen_width, screen_height


def minimal_screen_resolutely_for_messagebox(minimal_screen_resolution):
    min_screen_width, min_screen_height = minimal_screen_resolution()

    MIN_BOX_WIDTH_ = min_screen_width / 2
    MIN_BOX_HEIGHT = min_screen_height / 2

    return MIN_BOX_WIDTH_, MIN_BOX_HEIGHT


def main_loop(root):
    root.mainloop()
