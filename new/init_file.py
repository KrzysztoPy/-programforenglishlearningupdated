from tkinter import Tk

import new.control_file as control_file

# from new.calculation_initialization import return_calculating_the_initial_size_of_the_main_window, \
#     return_calculating_the_middle_position_for_main_window, main_window_init
from init_file.init_notebook_tab import set_create_notebook_widget_and_root, creating_and_addition_new_tab

from all_setting_for_gui.notebook_tab_setting import title_for_menu_tab, title_for_typing_a_new_word_list_tab, \
    title_for_repeating_a_selected_word_list_tab, margin_size_for_new_tab

# from all_setting_for_gui.main_window_setting import main_loop

root = Tk()
screen_resolution = control_file.re_screen_resolution(root)
error_control = control_file.that_the_resolution_meets_the_minimum_requirements(screen_resolution, root)
main_window_size = control_file.return_size_of_the_main_window(root)
main_window_position = control_file.return_position_for_main_window(screen_resolution, main_window_size)

if control_file.check_error_control(error_control, screen_resolution):
    pass
else:
    main_window = control_file.init_create_main_window()

#

# mian_window_position = return_calculating_the_middle_position_for_main_window(root, main_window_resolutely)
#
# main_window_init(root, lambda: main_window_resolutely, lambda: mian_window_position)
# set_create_notebook_widget_and_root(root, main_window_resolutely, mian_window_position,
#                                     margin_size_for_new_tab)
#
# creating_and_addition_new_tab(title_for_menu_tab)
# creating_and_addition_new_tab(title_for_typing_a_new_word_list_tab)
# creating_and_addition_new_tab(title_for_repeating_a_selected_word_list_tab)
#
# main_loop(root)
