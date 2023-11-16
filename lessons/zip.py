"""Combining two lists into a dictionary."""


__author__ = "730569615"


def zip(list_str: list[str], list_int: list[int]) -> dict[str, int]:
    """Zips together two lists into a dict."""
    dict_zip: dict[str, int] = {}
    if len(list_str) != len(list_int):
        return dict_zip
    if len(list_str) == 0:
        return dict_zip
    for i in range(len(list_str)):
        dict_zip[list_str[i]] = list_int[i]
    return dict_zip