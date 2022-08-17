import pytest
from unittest.mock import patch
import new.calculation_initialization

from new.calculation_initialization_decorators import \
    checking_if_the_downloaded_screen_resolution_is_higher_than_the_minimum


@pytest.mark.parametrize("width_height_resolutely,result", (
        ((1920, 1080), True),
        ((1024, 768), True),
        ((1024, 767), False),
        ((1023, 768), False)
))
def test_checking_if_the_downloaded_screen_resolution_is_higher_than_the_minimum(width_height_resolutely, result):
    with patch("new.calculation_initialization.get_screen_result") as mock_get_screen_result:
        mock_get_screen_result.return_value = width_height_resolutely
        if result:
            assert checking_if_the_downloaded_screen_resolution_is_higher_than_the_minimum(
                (lambda width_height: width_height)(width_height_resolutely)) == width_height_resolutely
        # else:
        #     with pytest.raises(RuntimeError,
        #                        match="Your screen resolution is less than the minimum supported screen resolution."):
        #         checking_if_the_downloaded_screen_resolution_is_higher_than_the_minimum(
        #             new.calculation_initialization.get_screen_result())
