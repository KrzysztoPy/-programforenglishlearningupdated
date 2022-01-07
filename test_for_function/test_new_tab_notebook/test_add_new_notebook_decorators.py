import pytest

from decorators.add_new_notebook_decorators import decorator_maximal_length_of_the_tab_name


@pytest.mark.parametrize("argument,sample,exception_expected,expected", [
    (lambda: 40, lambda: "c" * 40, IndexError, f"Maximal avaible length for tab name is: {40} "
                                               f"Your tab name length: {len('c' * 40)}"),
    (lambda: 40, lambda: "c" * 41, IndexError, f"Maximal avaible length for tab name is: {40} "
                                               f"Your tab name length: {len('c' * 41)}")

])
def test_decorator_maximal_length_of_the_tab_name(argument, sample, exception_expected, expected):
    with pytest.raises(exception_expected) as exception_info:
        result = decorator_maximal_length_of_the_tab_name(argument)(sample)
        result()
    assert exception_info.type is exception_expected
    assert str(exception_info.value) == expected
