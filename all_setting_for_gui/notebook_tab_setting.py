from decorators.add_new_notebook_decorators import decorator_maximal_length_of_the_tab_name


def maximal_length_of_the_tab_name_settings():
    return 40


@decorator_argument_maximal_length_of_the_tab_name(maximal_length_of_the_tab_name_settings())
def tab_menu_name_text():
    return "Menu"


def tab_typing_a_new_word_list_text():
    return "Typing a new list with words"


def tab_repeating_a_selected_word_list():
    return "Repeating a selected word list"
