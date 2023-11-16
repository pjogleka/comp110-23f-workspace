"""Summing the elements of a list using different loops."""


__author__ = "730569615"


def w_sum(vals: list[float]) -> float:
    """Calculates sum using while loop."""
    i = 0
    sum = 0.0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Calculates sum using for loop."""
    sum = 0.0
    for i in vals:
        sum += i
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Calculates sum using for/range loop."""
    sum = 0.0
    for i in range(len(vals)):
        sum += vals[i]
    return sum