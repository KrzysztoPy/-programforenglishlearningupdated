from decorators.add_new_notebook_decorators import decorator_maximal_length_of_the_tab_name



def maximal_length_of_the_tab_name_settings():
    return 40


def margin_size_for_new_tab():
    return 10


def size_new_tab_frame(main_width_size, main_height_size, margin_size):
    width_new_tab = main_width_size - margin_size
    height_new_tab = main_height_size - margin_size

    return width_new_tab, height_new_tab


@decorator_maximal_length_of_the_tab_name(maximal_length_of_the_tab_name_settings())
def tab_menu_name_text():
    return "Menu"


@decorator_maximal_length_of_the_tab_name(maximal_length_of_the_tab_name_settings())
def tab_typing_a_new_word_list_text():
    return "Typing a new list with words"


@decorator_maximal_length_of_the_tab_name(maximal_length_of_the_tab_name_settings())
def tab_repeating_a_selected_word_list():
    return "Repeating a selected word list"
