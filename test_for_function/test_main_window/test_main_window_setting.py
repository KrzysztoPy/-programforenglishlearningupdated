import pytest
from unittest.mock import patch

from all_setting_for_gui.main_window_setting import main_window_name_text, minimal_screen_resolution, \
    rules_for_determining_the_size_of_the_main_window, set_middle_position_for_main_window


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


@pytest.fixture(params=[(1920, 1080), (1600, 900), (1366, 768)])
def fixture_calculated_expected(request):
    width_result = -(request.param[0] // -2)
    hight_result = -(request.param[1] // -4)

    yield request.param[0], request.param[1], (width_result, hight_result)


def test_rules_for_determining_the_size_of_the_main_window(fixture_calculated_expected):
    assert rules_for_determining_the_size_of_the_main_window(fixture_calculated_expected[0],
                                                             fixture_calculated_expected[1]) == \
           fixture_calculated_expected[2]


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
