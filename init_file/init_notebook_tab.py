from Tkinter.new_tkinter.add_new_notebook import create_notebook_widget, creating_frame_for_new_notebook_tab, \
    set_name_new_notebook_tab, pack_notebook_widget
from all_setting_for_gui.main_window_setting import get_screen_result, main_loop
from all_setting_for_gui.notebook_tab_setting import tab_menu_name_text

root = None
notebook_widget = None
main_window_size = None
main_window_position = None


def set_create_notebook_widget_and_root(main_root, main_window_width_and_height_size, mian_window_position):
    global root
    global notebook_widget
    global main_window_size
    global main_window_position
    root = main_root
    notebook_widget = create_notebook_widget(root)
    main_window_size = main_window_width_and_height_size
    main_window_position = mian_window_position


def menu_tab_init():
    menu_frame = creating_frame_for_new_notebook_tab(notebook_widget, get_screen_result(root))
    set_name_new_notebook_tab(notebook_widget, menu_frame, tab_menu_name_text)
    pack_notebook_widget(notebook_widget)


def typing_a_new_list_tab_init():
    pass


def reoeating_tab_init():
    pass
