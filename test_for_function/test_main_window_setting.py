import pytest
from unittest.mock import patch
from all_setting_for_gui.main_window_setting import main_window_name, minimal_screen_resolution, \
    minimal_screen_resolutely_for_messagebox


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


# 512, 384  1024 / 2, 768 / 2
@pytest.mark.parametrize("expected",
                         [(512, 384)]
                         )
def test_minimal_screen_resolutely_for_messagebox(expected):
    with patch("all_setting_for_gui.main_window_setting.minimal_screen_resolution") as mock_minimal_screen_resolution:
        mock_minimal_screen_resolution = lambda: (expected[0] * 2, expected[1] * 2)
        assert minimal_screen_resolutely_for_messagebox(mock_minimal_screen_resolution) == expected

