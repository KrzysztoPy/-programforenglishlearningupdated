import pytest
from unittest.mock import MagicMock

from decorators.mian_window_decorators import rules_for_creating_the_name_of_the_main_window, \
    resctriction_for_minimal_screen_resolution, checking_if_the_downloaded_screen_resolution_is_higher_than_the_minimum


@pytest.mark.parametrize("sample, exception_type, expected", [
    (lambda: 1, TypeError, "Name must be a string type."),
    (lambda: "", AttributeError, "Title can't be empty."),
    (lambda: '60charactertext' * 4, AttributeError, 'Length name must be shorter than 60 characters.'),
    (lambda: '60charactertext' * 4 + ' ', AttributeError, 'Length name must be shorter than 60 characters.'),
])
def test_rules_for_creating_the_name_of_the_main_window(sample, exception_type, expected):
    decorator_func_result = rules_for_creating_the_name_of_the_main_window(sample)

    with pytest.raises(exception_type) as exc_info:
        decorator_func_result()
    assert exc_info.type is exception_type
    assert str(exc_info.value) == expected


@pytest.mark.parametrize("sample, exception_type, expected", (
        (lambda: (1023, 768), RuntimeError, "Lowest supported resolution is: Width: 1024, Height: 768. \n"
                                            "You can change it, but maybe it cause undesirable effects. You need to check the functionality related \n"
                                            "to scale the size of windows."),
        (lambda: (1024, 767), RuntimeError, "Lowest supported resolution is: Width: 1024, Height: 768. \n"
                                            "You can change it, but maybe it cause undesirable effects. You need to check the functionality related \n"
                                            "to scale the size of windows."),
        (lambda: (1023, 767), RuntimeError, "Lowest supported resolution is: Width: 1024, Height: 768. \n"
                                            "You can change it, but maybe it cause undesirable effects. You need to check the functionality related \n"
                                            "to scale the size of windows."),
))
def test_resctriction_for_minimal_screen_resolution(sample, exception_type, expected):
    decorator_func_result = resctriction_for_minimal_screen_resolution(sample)

    with pytest.raises(exception_type) as exc_info:
        decorator_func_result()
    assert exc_info.type is exception_type
    assert str(exc_info.value) == expected
