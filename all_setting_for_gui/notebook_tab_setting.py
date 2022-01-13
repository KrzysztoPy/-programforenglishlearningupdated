from decorators.add_new_notebook_decorators import decorator_maximal_length_of_the_tab_name


def maximal_length_of_the_tab_name_settings():
    return 40


def margin_size_for_new_tab():
    horizontal_margines = 10
    vertical_margines = 30
    return horizontal_margines, vertical_margines


def size_new_tab_frame(top_window_width_size, top_window_height_size, margin_size):
    width_new_tab = top_window_width_size - margin_size[0]
    height_new_tab = top_window_height_size - margin_size[1]

    return width_new_tab, height_new_tab


@decorator_maximal_length_of_the_tab_name(maximal_length_of_the_tab_name_settings)
def title_for_menu_tab():
    return "Menu"


@decorator_maximal_length_of_the_tab_name(maximal_length_of_the_tab_name_settings)
def title_for_typing_a_new_word_list_tab():
    return "Typing a new list with words"


@decorator_maximal_length_of_the_tab_name(maximal_length_of_the_tab_name_settings)
def title_for_repeating_a_selected_word_list_tab():
    return "Repeating a selected word list"
