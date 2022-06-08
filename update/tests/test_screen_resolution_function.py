import pytest
from tkinter import Tk
from unittest.mock import Mock

import update.screen_resolution_function
from update.screen_resolution_function import \
    return_screen_resolution_width_height, check_the_minimum_resolution_requirements, \
    save_width_and_height_screen_resolution, calculating_the_middle_position_on_screen


@pytest.fixture
def tkinter_tk():
    return Tk()


@pytest.fixture(name="resolution_to_none")
def setting_the_saved_screen_resolution_to_none():
    update.screen_resolution_function.screen_resolution_width = None
    update.screen_resolution_function.screen_resolution_height = None


@pytest.fixture
def mock_screen_resolution(tkinter_tk):
    tkinter_tk.winfo_screenwidth = Mock()
    tkinter_tk.winfo_screenheight = Mock()
    return tkinter_tk.winfo_screenwidth, tkinter_tk.winfo_screenheight


@pytest.mark.parametrize("glob_screen_width,glob_screen_height,expected", (
        (1280, 720, (1280, 720)),
        (1600, 900, (1600, 900)),

))
def test_save_width_and_height_screen_resolution_if_is_true(resolution_to_none, tkinter_tk, mock_screen_resolution,
                                                            glob_screen_width, glob_screen_height, expected):
    mock_screen_resolution[0].return_value = glob_screen_width
    mock_screen_resolution[1].return_value = glob_screen_height

    save_width_and_height_screen_resolution(tkinter_tk)
    result = update.screen_resolution_function.screen_resolution_width, \
             update.screen_resolution_function.screen_resolution_height

    assert result == expected


@pytest.mark.parametrize("glob_screen_width,glob_screen_height,new_value_screen_width,new_value_screen_height,expected",
                         (
                                 (1280, 720, 1920, 1080, (1280, 720)),
                                 (1600, 900, 1920, 1080, (1600, 900)),
                         ))
def test_save_width_and_height_screen_resolution_if_is_false(tkinter_tk, mock_screen_resolution, glob_screen_width,
                                                             glob_screen_height, new_value_screen_width,
                                                             new_value_screen_height, expected):
    update.screen_resolution_function.screen_resolution_width = glob_screen_width
    update.screen_resolution_function.screen_resolution_height = glob_screen_height
    mock_screen_resolution[0].return_value = new_value_screen_width
    mock_screen_resolution[1].return_value = new_value_screen_height

    save_width_and_height_screen_resolution(tkinter_tk)
    result = update.screen_resolution_function.screen_resolution_width, \
             update.screen_resolution_function.screen_resolution_height

    assert result == expected


@pytest.mark.parametrize("tmp_width_resolution,tmp_height_resolution", (
        (1280, 720),
        (1279, 720),
        (1280, 719),
))
def test_return_screen_resolution_width_height(resolution_to_none, mock_screen_resolution, tkinter_tk,
                                               tmp_width_resolution,
                                               tmp_height_resolution):
    mock_screen_resolution[0].return_value = tmp_width_resolution
    mock_screen_resolution[1].return_value = tmp_height_resolution
    save_width_and_height_screen_resolution(tkinter_tk)

    assert return_screen_resolution_width_height() == (tmp_width_resolution, tmp_height_resolution)


@pytest.mark.parametrize("tmp_width_resolution,tmp_height_resolution,expected", (
        (1280, 720, True),
        (1279, 720, False),
        (1280, 719, False),
))
def test_check_the_minimum_resolution_requirements(mock_screen_resolution, tmp_width_resolution, tmp_height_resolution,
                                                   expected):
    mock_screen_resolution[0].return_value = tmp_width_resolution
    mock_screen_resolution[1].return_value = tmp_height_resolution

    assert check_the_minimum_resolution_requirements() == expected


@pytest.mark.parametrize("tmp_width_resolution,tmp_height_resolution,expected", (
        (1280, 720, (40, 60)),
        (1600, 900, (200, 150)),
        (1920, 1080, (360, 240)),
        (3840, 2160, (1320, 780)),
))
def test_calculating_the_middle_position_on_screen(resolution_to_none, tmp_width_resolution,
                                                   tmp_height_resolution, expected):
    update.screen_resolution_function.screen_resolution_width = tmp_width_resolution
    update.screen_resolution_function.screen_resolution_height = tmp_height_resolution

    result = calculating_the_middle_position_on_screen()
    assert result == expected
