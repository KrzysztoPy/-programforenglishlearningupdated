import pytest
from tkinter import Tk
from unittest.mock import Mock, MagicMock, patch
from program_for_english_learning_updated_new.screen_resolution_function import return_screen_resolution_width_height


@pytest.fixture
def tkinter_tk():
    return Tk()


@pytest.mark.parametrize("tmp_width,tmp_height", (
        (1280, 720),
        (1279, 720),
        (1280, 719),
))
def test_return_screen_resolution_width_height(tkinter_tk, tmp_width, tmp_height):
    tkinter_tk.winfo_screenwidth = Mock()
    tkinter_tk.winfo_screenheight = Mock()
    tkinter_tk.winfo_screenwidth.return_value = tmp_width
    tkinter_tk.winfo_screenheight.return_value = tmp_height

    assert return_screen_resolution_width_height(tkinter_tk) == (tmp_width, tmp_height)
