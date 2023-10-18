def smallest_number(num_list: list) -> int:
    """
    Finds the smallest number from a list.

    :param num_list: list of numbers
    :return: smallest number from the list
    """
    num_list.sort()
    return num_list[0]


def highest_number(num_list: list) -> int:
    """
    Finds the highest number from a list.

    :param num_list: list of numbers
    :return: highest number from the list
    """
    findmax = max(num_list)
    return findmax


def number_to_string(str_len: int) -> dict:
    """
    Creates a dictionary of numbers from 0 to str_len.

    :param str_len: length of the dictionary
    :return: dictionary of numbers from 0 to str_len
    """
    num_to_text = {str(x): x for x in range(str_len)}
    return num_to_text
