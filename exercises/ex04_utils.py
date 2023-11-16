"""List exercise."""


author: str = "730569615"


def all(int_list: list[int], num: int) -> bool:
    """Determines if list only contains num."""
    index = 0
    if len(int_list) == 0:
        return_val = False
        return return_val
    while index < len(int_list):
        if int_list[index] == num:
            return_val = True
            index += 1
        else:
            return_val = False
            return return_val
    return return_val


def max(int_list: list[int]) -> int:
    """Returns max val in list."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        index = 0
        max_num = int_list[index]
        while index < len(int_list) - 1:
            if int_list[index + 1] > max_num:
                max_num = int_list[index + 1]
            index += 1
    return max_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Determines is lists are equal."""
    if len(list_1) == len(list_2):
        if len(list_1) == 0:
            return_val = True
            return return_val
        index = 0
        while index < len(list_1):
            if list_1[index] == list_2[index]:
                return_val = True
                index += 1
            else:
                return_val = False
                return return_val
    else:
        return_val = False
        return return_val
    return return_val