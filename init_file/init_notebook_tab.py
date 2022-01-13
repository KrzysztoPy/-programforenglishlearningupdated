from Tkinter.new_tkinter.add_new_notebook import create_notebook_widget, creating_frame_for_new_tab, \
    append_new_tab_to_notebook, pack_notebook_widget
from all_setting_for_gui.main_window_setting import get_screen_result, main_loop

root = None
notebook_widget = None
main_window_size = None
main_window_position = None
margin_size_for_new_tab = None


def set_create_notebook_widget_and_root(main_root, main_window_width_and_height_size, mian_window_position,
                                        margin_size_new_tab):
    global root
    global notebook_widget
    global main_window_size
    global main_window_position
    global margin_size_for_new_tab
    root = main_root
    notebook_widget = create_notebook_widget(root)
    main_window_size = main_window_width_and_height_size
    main_window_position = mian_window_position
    margin_size_for_new_tab = margin_size_new_tab()


def creating_and_addition_new_tab(new_table_title):
    frame_for_new_tab = creating_frame_for_new_tab(notebook_widget, main_window_size, margin_size_for_new_tab)
    append_new_tab_to_notebook(notebook_widget, frame_for_new_tab, new_table_title)
    pack_notebook_widget(notebook_widget)
