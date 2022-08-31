# Tkinter
MAIN_WINDOW_NAME = "Program for english learning"

# Error
ERROR_FILE_NAME = "Critical resolution error.txt"
ERROR_RESOLUTION_ZERO = "Critical error: The resolution read is 0."

# Screen
MIN_SCREEN_WIDTH = 1024
MIN_SCREEN_HEIGHT = 768


# It can't be here.
def minimal_screen_resolutely_for_messagebox():
    min_screen_width, min_screen_height = MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT

    min_screen_width = min_screen_width / 2
    min_screen_height = min_screen_height / 2

    return min_screen_width, min_screen_height


# It can't be here.
def main_loop(root):
    root.mainloop()
