import pytest
from tkinter import Tk
from unittest.mock import patch

from init_file.init_main_window import return_calculating_the_initial_size_of_the_main_window, \
    return_calculating_the_middle_position_for_main_window, main_window_init
from init_file import init_main_window


@pytest.fixture
def fixture_tk_root_object():
    return Tk()


@pytest.mark.parametrize("width_resolute,height_resolute,expected", [
    (1600, 900, (-(1600 // -2), -(900 // -4))),
    (1920, 1080, (-(1920 // -2), -(1080 // -4))),
    (1366, 768, (-(1366 // -2), -(768 // -4)))
])
@patch.object(init_main_window, 'get_screen_result')
def test_return_calculating_the_initial_size_of_the_main_window(get_screen_result_mock, fixture_tk_root_object,
                                                                width_resolute, height_resolute, expected):
    get_screen_result_mock.return_value = (width_resolute, height_resolute)

    assert return_calculating_the_initial_size_of_the_main_window(fixture_tk_root_object) == expected


@pytest.mark.parametrize("width_resolute,height_resolute,window_width_size,window_height_size", [
    (1600, 900, -(1600 // -2), -(900 // -4)),
    (1920, 1080, -(1920 // -2), -(1080 // -4)),
    (1366, 768, -(1366 // -2), -(768 // -4))
])
@patch.object(init_main_window, "get_screen_result")
def test_return_calculating_the_middle_position_for_main_window(get_screen_result_mock, fixture_tk_root_object,
                                                                width_resolute, height_resolute, window_width_size,
                                                                window_height_size):
    get_screen_result_mock.return_value = (width_resolute, height_resolute)
    expected_horizontal_position_on_screen = -(get_screen_result_mock()[0] // -2) + (window_width_size // -2)
    expected_vertical_position_on_screen = -(get_screen_result_mock()[1] // -2) + (window_height_size // -2)

    assert return_calculating_the_middle_position_for_main_window(fixture_tk_root_object,
                                                                  (window_width_size, window_height_size)) == \
           (expected_horizontal_position_on_screen, expected_vertical_position_on_screen)



def test_main_window_init(fixture_tk_root_object):
    main_window_init