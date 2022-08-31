import pytest
import new.text_information_for_the_user


@pytest.mark.parametrize("screen_width,screen_height",
                         (1023, 768),
                         (1024, 767),
                         (800, 600))
def test_err_too_low_screen_resolution(screen_width, screen_height):
    pass