import pytest

from all_setting_for_gui.notebook_tab_setting import size_new_tab_frame


@pytest.mark.parametrize("top_window_width_size, top_window_height_size, margin_size,expected", (
        (1920, 1080, (20, 10), (1900, 1070)),
        (1600, 900, (46, 46), (1554, 854)),
        (1366, 768, (77, 88), (1289, 680)),
))
def test_size_new_tab_frame(top_window_width_size, top_window_height_size, margin_size, expected):
    assert size_new_tab_frame(top_window_width_size, top_window_height_size, margin_size) == expected
