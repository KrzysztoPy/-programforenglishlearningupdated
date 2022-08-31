import pytest
from unittest.mock import patch
import tkinter




@pytest.fixture(scope="module")
def root_tk():
    return tkinter.Tk()


# # DONE
# @pytest.mark.parametrize("expected", [
#     (1366, 768),
#     (1680, 1050),
#     (1920, 1080)
# ])
# def test_get_screen_result(root_tk, expected):
#     with patch("tkinter.Tk.winfo_screenwidth") as mock_winfo_screenwidth:
#         with patch("tkinter.Tk.winfo_screenheight") as mock_winfo_screenheight:
#             mock_winfo_screenwidth.return_value = expected[0]
#             mock_winfo_screenheight.return_value = expected[1]
#             assert get_screen_result(root_tk) == expected


@pytest.mark.parametrize("expected,tmp", (
        ((1366, 768), True),
        ((1680, 1050), True),
        ((1920, 1080), True)))
def test_tmp(expected, tmp):
    assert expected
    assert tmp
