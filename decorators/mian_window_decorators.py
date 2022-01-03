# """
# :arg
# checked - Is element which checking
# *args   - Tupla with restrictions / rules for checking element
# """


def rules_for_creating_the_name_of_the_main_window(func_return_mian_window_name):
    mian_window_name = func_return_mian_window_name()

    if type(mian_window_name) is type(''):
        if mian_window_name != "":
            if len(mian_window_name) < 60:
                return mian_window_name
            else:
                raise AttributeError('Length name must be shorter than 60 characters.')
        else:
            raise AttributeError("Title can't be empty.")
    else:
        raise TypeError("Name must be a string type.")


def resctriction_for_minimal_screen_resolution(minimal_screen_resolution):
    width, height = minimal_screen_resolution()
    if width < 1024 or height < 768:
        raise Exception(
            "Lowest supported resolution is: Width: 1024, Height: 768. \n"
            "You can change it, but maybe it cause undesirable effects. You need to check the functionality related \n"
            "to scale the size of windows ")

