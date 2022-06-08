import pytest
from tkinter import Tk
from unittest.mock import Mock, patch

import update.screen_resolution_function
from update.screen_resolution_function import \
    return_screen_resolution_width_height, check_the_minimum_resolution_requirements, \
    save_width_and_height_screen_resolution


@pytest.fixture
def tkinter_tk():
    return Tk()


@pytest.fixture
def mock_screen_resolution(tkinter_tk):
    tkinter_tk.winfo_screenwidth = Mock()
    tkinter_tk.winfo_screenheight = Mock()
    return tkinter_tk.winfo_screenwidth, tkinter_tk.winfo_screenheight


@pytest.mark.parametrize("glob_screen_width,glob_screen_height,expected", (
        (1280, 720, (1280, 720)),
        (1600, 900, (1600, 900)),

))
def test_save_width_and_height_screen_resolution_if_is_true(tkinter_tk, mock_screen_resolution, glob_screen_width,
                                                            glob_screen_height, expected):
    update.screen_resolution_function.screen_width = None
    update.screen_resolution_function.screen_height = None
    mock_screen_resolution[0].return_value = glob_screen_width
    mock_screen_resolution[1].return_value = glob_screen_height

    save_width_and_height_screen_resolution(tkinter_tk)
    result = update.screen_resolution_function.screen_width, update.screen_resolution_function.screen_height

    assert result == expected


@pytest.mark.parametrize("glob_screen_width,glob_screen_height,new_value_screen_width,new_value_screen_height,expected",
                         (
                                 (1280, 720, 1920, 1080, (1280, 720)),
                                 (1600, 900, 1920, 1080, (1600, 900)),
                         ))
def test_save_width_and_height_screen_resolution_if_is_false(tkinter_tk, mock_screen_resolution, glob_screen_width,
                                                             glob_screen_height, new_value_screen_width,
                                                             new_value_screen_height, expected):
    update.screen_resolution_function.screen_width = glob_screen_width
    update.screen_resolution_function.screen_height = glob_screen_height
    mock_screen_resolution[0].return_value = new_value_screen_width
    mock_screen_resolution[1].return_value = new_value_screen_height

    save_width_and_height_screen_resolution(tkinter_tk)
    result = update.screen_resolution_function.screen_width, update.screen_resolution_function.screen_height

    assert result == expected


@pytest.mark.parametrize("tmp_width,tmp_height", (
        (1280, 720),
        (1279, 720),
        (1280, 719),
))
def test_return_screen_resolution_width_height(mock_screen_resolution, tkinter_tk, tmp_width, tmp_height):
    update.screen_resolution_function.screen_width = None
    update.screen_resolution_function.screen_height = None
    mock_screen_resolution[0].return_value = tmp_width
    mock_screen_resolution[1].return_value = tmp_height
    save_width_and_height_screen_resolution(tkinter_tk)

    assert return_screen_resolution_width_height() == (tmp_width, tmp_height)


@pytest.mark.parametrize("tmp_width,tmp_height,expected", (
        (1280, 720, True),
        (1279, 720, False),
        (1280, 719, False),
))
def test_check_the_minimum_resolution_requirements(mock_screen_resolution, tmp_width, tmp_height, expected):
    mock_screen_resolution[0].return_value = tmp_width
    mock_screen_resolution[1].return_value = tmp_height

    assert check_the_minimum_resolution_requirements() == expected
