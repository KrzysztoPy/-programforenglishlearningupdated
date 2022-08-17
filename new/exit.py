def exit_program_with_error(describe_of_the_exception):
    if describe_of_the_exception[0]:
        exit(f"Code error: {describe_of_the_exception[0]} Error description:{describe_of_the_exception[1]}.")


def exit_program_without_error():
    exit()
