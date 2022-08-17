from tkinter import Tk
from functools import wraps
from new.settings import minimal_screen_resolution

# from all_setting_for_gui.main_window_setting import minimal_screen_resolution


# from all_setting_for_gui.main_window_setting import minimal_screen_resolution

# def rules_for_creating_the_name_of_the_main_window(func_return_mian_window_name):
#     @wraps(func_return_mian_window_name)
#     def wrapper_return_mian_window_name():
#         mian_window_name = func_return_mian_window_name()
#
#         if type(mian_window_name) is type(''):
#             if mian_window_name != "":
#                 if len(mian_window_name) < 60:
#                     return func_return_mian_window_name()
#                 else:
#                     raise AttributeError('Length name must be shorter than 60 characters.')
#             else:
#                 raise AttributeError("Title can't be empty.")
#         else:
#             raise TypeError("Name must be a string type.")
#
#     return wrapper_return_mian_window_name


"""
Checking if someone has set the resolution below minimal resolution
Minimal resolution can be change but must do so consciously.
"""


# def restriction_for_minimal_screen_resolution(minimal_screen_resolution_func):
#     @wraps(minimal_screen_resolution_func)
#     def wrapper_minimal_screen_resolution_func():
#         min_screen_width, min_screen_height = minimal_screen_resolution_func()
#
#         if min_screen_width < 1024 or min_screen_height < 768:
#             raise RuntimeError(
#                 "Lowest supported resolution is: Width: 1024, Height: 768. \n"
#                 "You can change it, but maybe it cause undesirable effects. You need to check the functionality related \n"
#                 "to scale the size of windows.")
#             sys.exit(1)
#         else:
#             return minimal_screen_resolution_func()
#
#     return wrapper_minimal_screen_resolution_func


def checking_if_the_downloaded_screen_resolution_is_higher_than_the_minimum(get_screen_result):
    @wraps(get_screen_result)
    def wrapper_get_screen_result(root):
        horizontal_screen_resolution, vertical_screen_resolution = get_screen_result(Tk())
        min_horizontal_screen_resolution, min_vertical_screen_resolution = minimal_screen_resolution()

        if horizontal_screen_resolution >= min_horizontal_screen_resolution and \
                vertical_screen_resolution >= min_vertical_screen_resolution:
            return get_screen_result()
        else:
            raise RuntimeError("Your screen resolution is less than the minimum supported screen resolution.")

    return wrapper_get_screen_result
