import pytest
from unittest.mock import Mock

import update.screen_resolution_function as srf
from update.screen_resolution_function import \
    return_screen_resolution_width_height, check_the_minimum_resolution_requirements, \
    get_and_save_screen_resolution, calculating_the_middle_position_on_screen


@pytest.fixture
def mock_screen_resolution(tkinter_tk):
    tkinter_tk.winfo_screenwidth = Mock()
    tkinter_tk.winfo_screenheight = Mock()
    return tkinter_tk.winfo_screenwidth, tkinter_tk.winfo_screenheight


@pytest.fixture
def set_resolution_for_none():
    srf.screen_resolution_width = None
    srf.screen_resolution_height = None


@pytest.mark.parametrize("glob_screen_width,glob_screen_height,expected", (
        (1280, 720, (1280, 720)),
        (1600, 900, (1600, 900)),

))
def test_save_width_and_height_screen_resolution_if_is_true(set_resolution_for_none, tkinter_tk, mock_screen_resolution,
                                                            glob_screen_width,
                                                            glob_screen_height, expected):
    mock_screen_resolution[0].return_value = glob_screen_width
    mock_screen_resolution[1].return_value = glob_screen_height

    get_and_save_screen_resolution(tkinter_tk)
    result = srf.screen_resolution_width, srf.screen_resolution_height

    assert result == expected


@pytest.mark.parametrize("glob_screen_width,glob_screen_height,new_value_screen_width,new_value_screen_height,expected",
                         (
                                 (1280, 720, 1920, 1080, (1280, 720)),
                                 (1600, 900, 1920, 1080, (1600, 900)),
                         ))
def test_save_width_and_height_screen_resolution_if_is_false(tkinter_tk, mock_screen_resolution, glob_screen_width,
                                                             glob_screen_height, new_value_screen_width,
                                                             new_value_screen_height, expected):
    srf.screen_resolution_width = glob_screen_width
    srf.screen_resolution_height = glob_screen_height
    mock_screen_resolution[0].return_value = new_value_screen_width
    mock_screen_resolution[1].return_value = new_value_screen_height

    get_and_save_screen_resolution(tkinter_tk)
    result = srf.screen_resolution_width, srf.screen_resolution_height

    assert result == expected


@pytest.mark.parametrize("tmp_width,tmp_height", (
        (1280, 720),
        (1279, 720),
        (1280, 719),
))
def test_return_screen_resolution_width_height(set_resolution_for_none, mock_screen_resolution, tkinter_tk, tmp_width,
                                               tmp_height):
    mock_screen_resolution[0].return_value = tmp_width
    mock_screen_resolution[1].return_value = tmp_height
    get_and_save_screen_resolution(tkinter_tk)

    assert return_screen_resolution_width_height() == (tmp_width, tmp_height)


@pytest.mark.parametrize("tmp_width,tmp_height,expected", (
        (1280, 720, True),
        (1279, 720, False),
        (1280, 719, False),
))
def test_check_the_minimum_resolution_requirements(tmp_width, tmp_height, expected):
    srf.screen_resolution_width = tmp_width
    srf.screen_resolution_height = tmp_height

    assert check_the_minimum_resolution_requirements() == expected


@pytest.mark.parametrize("tmp_width_resolution,tmp_height_resolution,expected", (
        (1280, 720, (40, 60)),
        (1600, 900, (200, 150)),
        (1920, 1080, (360, 240)),
        (3840, 2160, (1320, 780)),
))
def test_calculating_the_middle_position_on_screen(tmp_width_resolution, tmp_height_resolution,
                                                   expected):
    srf.screen_resolution_width = tmp_width_resolution
    srf.screen_resolution_height = tmp_height_resolution
    calculating_the_middle_position_on_screen()

    result = srf.horizontal_position_on_screen, srf.vertical_position_on_screen
    assert result == expected
