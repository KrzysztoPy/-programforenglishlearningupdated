import pytest
from tkinter import Tk
from unittest.mock import Mock, patch
from program_for_english_learning_updated_new.screen_resolution_function import return_screen_resolution_width_height, \
    check_the_minimum_resolution_requirements


@pytest.fixture
def tkinter_tk():
    return Tk()


@pytest.fixture
def mock_screen_resolution(tkinter_tk):
    tkinter_tk.winfo_screenwidth = Mock()
    tkinter_tk.winfo_screenheight = Mock()
    return tkinter_tk.winfo_screenwidth, tkinter_tk.winfo_screenheight

@pytest.mark.skip
@pytest.mark.parametrize("tmp_width,tmp_height", (
        (1280, 720),
        (1279, 720),
        (1280, 719),
))
def test_return_screen_resolution_width_height(mock_screen_resolution, tkinter_tk, tmp_width, tmp_height):
    mock_screen_resolution[0].return_value = tmp_width
    mock_screen_resolution[1].return_value = tmp_height

    assert return_screen_resolution_width_height(tkinter_tk) == (tmp_width, tmp_height)


@pytest.mark.parametrize("tmp_width,tmp_height,expected", (
        (1280, 720, True),
        (1279, 720, False),
        (1280, 719, False),
))
def test_check_the_minimum_resolution_requirements(mock_screen_resolution, tkinter_tk, tmp_width, tmp_height, expected):
    mock_screen_resolution[0].return_value = tmp_width
    mock_screen_resolution[1].return_value = tmp_height

    assert check_the_minimum_resolution_requirements(tkinter_tk) == expected
