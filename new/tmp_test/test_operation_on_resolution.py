import pytest
import tkinter
from unittest.mock import patch

import new.operation_on_resolution as operation_on_resolution


@pytest.fixture(scope="module")
def root_tk():
    return tkinter.Tk()


@pytest.mark.parametrize("expected", [
    (1366, 768),
    (1680, 1050),
    (1920, 1080)
])
def test_get_screen_result(root_tk, expected):
    with patch("tkinter.Tk.winfo_screenwidth") as mock_winfo_screenwidth:
        with patch("tkinter.Tk.winfo_screenheight") as mock_winfo_screenheight:
            mock_winfo_screenwidth.return_value = expected[0]
            mock_winfo_screenheight.return_value = expected[1]
            assert operation_on_resolution.get_screen_result(root_tk) == expected


@pytest.mark.parametrize("samples,expected", [
    ((1366, 768), (683, 192)),
    ((1680, 1050), (840, 263)),
    ((1920, 1080), (960, 270)),
])
def test_calculating_the_size_of_the_main_window(samples, expected):
    assert operation_on_resolution.calculating_the_size_of_the_main_window(samples) == expected


@pytest.mark.parametrize(
    "width_screen_resolution,height_screen_resolution,width_window_size,height_window_size,expected", [
        (1366, 768, 683, 192, (341, 288)),
        (1680, 1050, 840, 263, (420, 393)),
        (1920, 1080, 960, 270, (480, 405)),
    ])
def test_calculating_middle_position_main_window_on_screen(width_screen_resolution, height_screen_resolution,
                                                           width_window_size, height_window_size, expected):
    assert operation_on_resolution.calculating_middle_position_main_window_on_screen(width_screen_resolution,
                                                                                     height_screen_resolution,
                                                                                     width_window_size,
                                                                                     height_window_size) == expected
