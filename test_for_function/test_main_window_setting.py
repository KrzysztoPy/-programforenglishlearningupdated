import pytest
from unittest.mock import patch

from all_setting_for_gui.main_window_setting import main_window_name, minimal_screen_resolution, \
    rules_for_determining_the_size_of_the_main_window, set_middle_position_for_main_window


@pytest.mark.parametrize("expected",
                         [("Program for english learning")]
                         )
def test_main_window_name(expected):
    assert main_window_name() == expected


@pytest.mark.parametrize("expected",
                         [(1024, 768)]
                         )
def test_minimal_screen_resolution(expected):
    assert minimal_screen_resolution() == expected


@pytest.mark.parametrize("expected",
                         [(512, 384)]
                         )
def test_minimal_screen_resolutely_for_messagebox(expected):
    with patch("all_setting_for_gui.main_window_setting.minimal_screen_resolution") as mock_minimal_screen_resolution:
        mock_minimal_screen_resolution = lambda: (expected[0] * 2, expected[1] * 2)
        assert minimal_screen_resolutely_for_messagebox(mock_minimal_screen_resolution) == expected


@pytest.mark.parametrize("width_sample,height_sample,expected",
                         [(1920, 1080, (384, 135)),
                          (1600, 900, (320, 113)),
                          (1366, 768, (274, 96))
                          ])
def test_rules_for_determining_the_size_of_the_main_window(width_sample, height_sample, expected):
    assert rules_for_determining_the_size_of_the_main_window(width_sample, height_sample) == expected


@pytest.mark.parametrize(
    "width_screen_resolution, height_screen_resolution, width_window_size, height_window_size, expected", [
        (1920, 1080, -(1920 // -5), -(1080 // -8), (768, 472)),
        (1680, 1050, -(1680 // -5), -(1050 // -8), (672, 459)),
        (1366, 768, -(1366 // -5), -(768 // -8), (546, 336)),
    ])
def test_set_middle_position_for_main_window(width_screen_resolution, height_screen_resolution, width_window_size,
                                             height_window_size, expected):
    assert set_middle_position_for_main_window(width_screen_resolution, height_screen_resolution, width_window_size,
                                               height_window_size) == expected
