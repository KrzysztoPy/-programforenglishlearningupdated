import pytest
from unittest.mock import patch
import tkinter

from all_setting_for_gui.main_window_setting import main_window_name_text, minimal_screen_resolution, get_screen_result


@pytest.mark.parametrize("expected",
                         [("Program for english learning")]
                         )
def test_main_window_name(expected):
    assert main_window_name_text() == expected


@pytest.mark.parametrize("expected",
                         [(1024, 768)]
                         )
def test_minimal_screen_resolution(expected):
    assert minimal_screen_resolution() == expected


@pytest.fixture(scope="module")
def root_tk():
    return tkinter.Tk()


@pytest.mark.parametrize("expected", [
    (1680, 1050),
    (1920, 1080)
])
def test_get_screen_result(root_tk, expected):
    if expected == (1680, 1050):
        with patch("tkinter.Tk.winfo_screenwidth") as mock_winfo_screenwidth:
            with patch("tkinter.Tk.winfo_screenheight") as mock_winfo_screenheight:
                mock_winfo_screenwidth.return_value = 1680
                mock_winfo_screenheight.return_value = 1050
                assert get_screen_result(root_tk) == expected
    else:
        assert get_screen_result(root_tk) == expected
