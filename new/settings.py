def main_window_name_text():
    return "Program for english learning"


def minimal_screen_resolution():
    min_screen_width = 1024
    min_screen_height = 768
    return min_screen_width, min_screen_height


def minimal_screen_resolutely_for_messagebox():
    min_screen_width, min_screen_height = minimal_screen_resolution()

    min_screen_width = min_screen_width / 2
    min_screen_height = min_screen_height / 2

    return min_screen_width, min_screen_height


# It can't be here.
def main_loop(root):
    root.mainloop()
