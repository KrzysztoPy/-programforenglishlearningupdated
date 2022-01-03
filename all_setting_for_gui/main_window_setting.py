from decorators.mian_window_decorators import rules_for_creating_the_name_of_the_main_window, \
    resctriction_for_minimal_screen_resolution


@rules_for_creating_the_name_of_the_main_window
def main_window_name():
    return "Program for english learning"


@resctriction_for_minimal_screen_resolution
def minimal_screen_resolution():
    width = 1024
    height = 768
    return width, height

# def resstriction_for_main_windows_name():
#     name_must_be_of_type_string = lambda text: type(text) is type('')
#     name_cant_be_empty = lambda text: text != ""
#     name_cant_be_longer_than_60_characters = lambda text: len(text) < 60
#
#     # Old solution
#     # name_must_be_of_type_string = "type()",type('').__name__, True
#     # name_cant_be_empty = "!=", "", False
#     # name_cant_be_longer_than_60_characters = "<", 60, True
#
#     return name_must_be_of_type_string, name_cant_be_empty, name_cant_be_longer_than_60_characters
