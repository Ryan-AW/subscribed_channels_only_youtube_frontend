""" Converts large integers into humanreadable strings """


def human_readable_large_numbers(num: int | None) -> str | None:
    """ Converts a large integer into a humanreadable string """

    # Account for view_count being None
    if num is None:
        return None

    suffixes = ['', 'K', 'M', 'B']

    i = 0
    while num >= 1000 and i < len(suffixes) - 1:
        num /= 1000
        i += 1

    if i == 0:
        return str(int(num))
    return f'{num:.1f}{suffixes[i]}'
