def smallest_number(num_list: list):
    """
    Finds the smallest number from a list.
    """
    num_list.sort()
    return num_list[0]

def highest_number(num_list: list):
    """
    Finds the highest number from a list.
    """
    findmax = max(num_list)
    return findmax

def number_to_string(str_len: int):
    """
    Converts number to string.
    """
    num_to_text = {str(x): x for x in range(str_len)}
    return num_to_text