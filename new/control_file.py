import new.operation_on_resolution as resolutely
import new.error.error_handle as error_handle


def re_screen_resolution(root_tk):
    return resolutely.get_screen_result(root_tk)


def that_the_resolution_meets_the_minimum_requirements(screen_resolution, root):
    return error_handle.checking_if_the_downloaded_screen_resolution_is_higher_than_the_minimum(screen_resolution)


def return_size_of_the_main_window(screen_resolution):
    return resolutely.calculating_the_size_of_the_main_window(screen_resolution)


def return_position_for_main_window(screen_resolution, window_size):
    return resolutely.calculating_middle_position_main_window_on_screen(
        screen_resolution[0], screen_resolution[1], window_size[0], window_size[1], )


def check_error_control(error_control, tuple_of_additional_parameters):
    if error_control:
        error_handle.dictionary_with_errors(error_control, tuple_of_additional_parameters)


def init_create_main_window(root, window_size, window_position):

    pass
