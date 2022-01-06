import pytest
import tkinter
from unittest.mock import patch

from all_setting_for_gui.main_window_setting import main_window_name
from Tkinter.new_tkinter.create_main_window import set_title, get_screen_result


@pytest.fixture
def root_tk():
    return tkinter.Tk()


@pytest.mark.parametrize("expected", [
    (main_window_name())
])
def test_set_tiitle(root_tk, expected):
    set_title(root_tk)
    assert root_tk.title() == expected


@pytest.mark.parametrize("expected", [
    (1680, 1050),
    (1920, 1080)
],ids=[])
def test_get_screen_result(root_tk, expected):
    if expected == (1680, 1050):
        with patch("tkinter.Tk.winfo_screenwidth") as mock_winfo_screenwidth:
            with patch("tkinter.Tk.winfo_screenheight") as mock_winfo_screenheight:
                mock_winfo_screenwidth.return_value = 1680
                mock_winfo_screenheight.return_value = 1050
                assert get_screen_result(root_tk) == expected
    i
    assert get_screen_result(root_tk) == expected
