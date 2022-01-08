import pytest
import tkinter
from unittest.mock import patch

from Tkinter.new_tkinter.create_main_window import set_title, calculating_the_initial_size_of_the_main_window, \
    calculating_middle_position_main_window_on_screen, set_geometry_main_window


@pytest.fixture(scope="function")
def root_tk():
    yield tkinter.Tk()


@pytest.mark.parametrize("sample,expected", [
    ("Program for english learning", "Program for english learning")
])
def test_set_tiitle(root_tk, sample, expected):
    set_title(root_tk, sample)
    assert root_tk.title() == expected


@pytest.fixture(params=[(1920, 1080), (1600, 900), (1366, 768)])
def fixture_calculated_expected_main_window_size(request):
    width_result = -(request.param[0] // -2)
    hight_result = -(request.param[1] // -4)

    yield request.param[0], request.param[1], (width_result, hight_result)


def test_rules_for_determining_the_size_of_the_main_window(fixture_calculated_expected_main_window_size):
    assert calculating_the_initial_size_of_the_main_window(fixture_calculated_expected_main_window_size[0],
                                                           fixture_calculated_expected_main_window_size[1]) == \
           fixture_calculated_expected_main_window_size[2]


@pytest.mark.parametrize(
    "width_screen_resolution, height_screen_resolution, width_window_size, height_window_size, expected", [
        (1920, 1080, -(1920 // -5), -(1080 // -8), (768, 472)),
        (1680, 1050, -(1680 // -5), -(1050 // -8), (672, 459)),
        (1366, 768, -(1366 // -5), -(768 // -8), (546, 336)),
    ])
def test_set_middle_position_for_main_window(width_screen_resolution, height_screen_resolution, width_window_size,
                                             height_window_size, expected):
    assert calculating_middle_position_main_window_on_screen(width_screen_resolution, height_screen_resolution,
                                                             width_window_size,
                                                             height_window_size) == expected


@pytest.fixture(params=[(1920, 1080), (1600, 900), (1366, 768)])
def fixture_test_set_geometry_main_window_data(request):
    width_window_result = -(request.param[0] // -2)
    hight_window_result = -(request.param[1] // -4)
    horizontal_position_on_screen = -(request.param[0] // -2) + (width_window_result // -2)
    vertical_position_on_screen = -(request.param[1] // -2) + (hight_window_result // -2)

    return (lambda: (width_window_result, hight_window_result), \
            lambda: (horizontal_position_on_screen, vertical_position_on_screen))


def test_set_geometry_main_window(root_tk, fixture_test_set_geometry_main_window_data):
    set_geometry_main_window(root_tk, fixture_test_set_geometry_main_window_data[0],
                             fixture_test_set_geometry_main_window_data[1])

    # Rolls out all changes to the object without triggering them
    root_tk.update_idletasks()

    result = (root_tk.winfo_width(), root_tk.winfo_height(), root_tk.winfo_x(), root_tk.winfo_y())

    assert result == (fixture_test_set_geometry_main_window_data[0]()[0],
                      fixture_test_set_geometry_main_window_data[0]()[1],
                      fixture_test_set_geometry_main_window_data[1]()[0],
                      fixture_test_set_geometry_main_window_data[1]()[1])


