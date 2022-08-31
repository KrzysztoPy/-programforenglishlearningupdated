import new.settings_and_remarks.general as general
import new.exit



def dictionary_with_errors(error_code, tuple_of_additional_parameters):
    error_dict = {
        1: lambda: err_critical_resolution(),
        2: lambda params: err_too_low_screen_resolution(params)
    }

    return error_dict.get(error_code, "None")(tuple_of_additional_parameters)


def err_critical_resolution():
    with open(general.ERROR_FILE_NAME, "w") as file:
        file.write(general.ERROR_RESOLUTION_ZERO)
    new.exit.exit_program()


def checking_if_the_downloaded_screen_resolution_is_higher_than_the_minimum(screen_resolution):
    min_screen_width, min_screen_height = general.MIN_SCREEN_WIDTH, general.MIN_SCREEN_HEIGHT
    if screen_resolution[0] < min_screen_width or \
            screen_resolution[1] < min_screen_height:
        return 1
    elif screen_resolution[0] == 0 or \
            screen_resolution[1] == 0:
        return 2
    else:
        return 0


def err_too_low_screen_resolution(screen_resolution_and_root_tk):
    min_screen_width, min_screen_height = general.MIN_SCREEN_WIDTH, general.MIN_SCREEN_HEIGHT

    raise Exception(f"Your resolution is below the minimum required resolution. "
                    f"Minimal required resolution: {min_screen_width, min_screen_height} "
                    f"Your screen resolution {screen_resolution_and_root_tk}")
