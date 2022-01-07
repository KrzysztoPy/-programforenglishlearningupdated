from functools import wraps


def decorator_maximal_length_of_the_tab_name(maximal_name_length):
    def maximal_length_of_the_tab_name(func_tabe_name):
        @wraps(func_tabe_name)
        def wrapper_func_tabe_name():
            var_maximal_length_of_the_tab_name_settings = maximal_name_length()
            checking_tab_len_name = len(func_tabe_name())

            if checking_tab_len_name < var_maximal_length_of_the_tab_name_settings:
                return func_tabe_name()
            else:
                raise IndexError(
                    f"Maximal avaible length for tab name is: {var_maximal_length_of_the_tab_name_settings} "
                    f"Your tab name length: {checking_tab_len_name}")

        return wrapper_func_tabe_name

    return maximal_length_of_the_tab_name


