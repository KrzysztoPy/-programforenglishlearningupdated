from tkinter import Tk

from new.calculation_initialization import return_calculating_the_initial_size_of_the_main_window, \
    return_calculating_the_middle_position_for_main_window, main_window_init
from init_file.init_notebook_tab import set_create_notebook_widget_and_root, creating_and_addition_new_tab

from all_setting_for_gui.notebook_tab_setting import title_for_menu_tab, title_for_typing_a_new_word_list_tab, \
    title_for_repeating_a_selected_word_list_tab, margin_size_for_new_tab
from all_setting_for_gui.main_window_setting import main_loop

root = Tk()

main_window_size = return_calculating_the_initial_size_of_the_main_window(root)


mian_window_position = return_calculating_the_middle_position_for_main_window(root, main_window_size)

main_window_init(root, lambda: main_window_size, lambda: mian_window_position)
set_create_notebook_widget_and_root(root, main_window_size, mian_window_position,
                                    margin_size_for_new_tab)

creating_and_addition_new_tab(title_for_menu_tab)
creating_and_addition_new_tab(title_for_typing_a_new_word_list_tab)
creating_and_addition_new_tab(title_for_repeating_a_selected_word_list_tab)

main_loop(root)
