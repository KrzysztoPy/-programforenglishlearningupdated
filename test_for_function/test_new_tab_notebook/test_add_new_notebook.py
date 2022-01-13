import pytest
from tkinter import Tk, ttk

from Tkinter.new_tkinter.add_new_notebook import create_notebook_widget, creating_frame_for_new_tab, \
    append_new_tab_to_notebook, pack_notebook_widget


@pytest.fixture
def tkinter_root_tk():
    return Tk()


@pytest.fixture
def tkinter_notebook_object(tkinter_root_tk):
    return ttk.Notebook(tkinter_root_tk)


@pytest.fixture
def tkinter_sample_frame(tkinter_notebook_object):
    return ttk.Frame(tkinter_notebook_object)


@pytest.mark.parametrize("expected", ["!notebook"])
def test_create_notebook_widget(tkinter_root_tk, expected):
    assert type(create_notebook_widget(tkinter_root_tk)) is type(ttk.Notebook())
    assert list(tkinter_root_tk.children.keys())[0] == expected


@pytest.mark.parametrize("main_window_size,margin_size_for_new_tab,expected", [
    ((1920, 1080), (20, 10), (1900, 1070)),
    ((1600, 900), (46, 46), (1554, 854)),
    ((1366, 768), (77, 88), (1289, 680)),
])
def test_creating_frame_for_new_tab(tkinter_notebook_object, main_window_size, margin_size_for_new_tab, expected):
    new_frame = creating_frame_for_new_tab(tkinter_notebook_object, main_window_size, margin_size_for_new_tab)
    tkinter_notebook_object.add(new_frame)
    tkinter_notebook_object.pack()
    new_frame.update()

    assert new_frame.winfo_width() == expected[0]
    assert new_frame.winfo_height() == expected[1]


@pytest.mark.parametrize('title_name', (
        lambda: "Sample title 1",
))
def test_append_new_tab_to_notebook(tkinter_notebook_object, tkinter_sample_frame, title_name):
    append_new_tab_to_notebook(tkinter_notebook_object, tkinter_sample_frame, title_name)

    assert list(tkinter_notebook_object.children.values())[0] is tkinter_sample_frame


def test_pack_notebook_widget(tkinter_root_tk, tkinter_notebook_object):
    assert tkinter_root_tk.pack_slaves() == []
    pack_notebook_widget(tkinter_notebook_object)
    assert tkinter_root_tk.pack_slaves()[0] == tkinter_notebook_object
