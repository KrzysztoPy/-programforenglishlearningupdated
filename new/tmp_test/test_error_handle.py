import pytest
import new.error.error_handle as error_handle
import new.settings_and_remarks.general as general

def test_err_critical_resolution():
    error_handle.err_critical_resolution()
    with open(general.ERROR_FILE_NAME, "r") as file:
        text = file.read()
    assert



def test_dictionary_with_errors():
    pass
