import pytest
from tkinter import Tk, ttk
from unittest.mock import patch

# from init_file.init_notebook_tab import set_create_notebook_widget_and_root, root, notebook_widget, main_window_size, \
#     main_window_position
from init_file import init_notebook_tab


@pytest.fixture
def fixture_tk_root():
    root = Tk()
    return root


@pytest.fixture
def fixture_ttk_notebook(fixture_tk_root):
    return ttk.Notebook(fixture_tk_root)


# from init_file import init_notebook_tab as init_tab

@pytest.mark.parametrize("width_window,height_window,horizontal_window_position,vertical_window_position", (
        (1920, 1080, 45, 33),
        (1680, 1050, 125, 47),
        (1368, 768, -15, -85),

))
@patch.object(init_notebook_tab, "create_notebook_widget")
def test_set_create_notebook_widget_and_root(mock_create_notebook_widget, fixture_tk_root, fixture_ttk_notebook,
                                             width_window, height_window, horizontal_window_position,
                                             vertical_window_position):
    mock_create_notebook_widget.return_value = fixture_ttk_notebook
    init_notebook_tab.set_create_notebook_widget_and_root(fixture_tk_root, (width_window, height_window),
                                                          (horizontal_window_position, vertical_window_position))
    assert init_notebook_tab.root is fixture_tk_root
    assert init_notebook_tab.notebook_widget is fixture_ttk_notebook
    assert init_notebook_tab.main_window_size == (width_window, height_window)
    assert init_notebook_tab.main_window_position == (horizontal_window_position, vertical_window_position)
