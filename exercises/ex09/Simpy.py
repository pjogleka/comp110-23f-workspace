"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730569615"


class Simpy:
    """Simpy class."""
    values: list[float]

    def __init__(self, inp_values: list[float]):
        """Initialize Simpy."""
        self.values = inp_values

    def __str__(self) -> str:
        """String method."""
        return f"Simpy({self.values})"
    
    def fill(self, val: float, reps: int) -> None:
        """Fill a Simpy array."""
        self.values = []
        for i in range(reps):
            self.values.append(val)
        return None

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Arange method."""
        assert step != 0.0
        self.values.append(start)
        if stop > start:
            while self.values[-1] < stop:
                self.values.append(self.values[-1] + step)
            self.values.pop(-1)
        if stop < start:
            while self.values[-1] > stop:
                self.values.append(self.values[-1] + step)
            self.values.pop(-1)
        return None
    
    def sum(self) -> float:
        """Sum Simpy array."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload add method."""
        added = Simpy([])
        if type(rhs) is type(self):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                added.values.append(self.values[i] + rhs.values[i])
        if type(rhs) is float:
            for i in range(len(self.values)):
                added.values.append(self.values[i] + rhs)
        return added
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload power method."""
        expd = Simpy([])
        if type(rhs) is type(self):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                expd.values.append(self.values[i] ** rhs.values[i])
        if type(rhs) is float:
            for i in range(len(self.values)):
                expd.values.append(self.values[i] ** rhs)
        return expd
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload equality mask method."""
        mask = []
        if type(rhs) is type(self):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    mask.append(True)
                else:
                    mask.append(False)
        if type(rhs) is float:
            for i in range(len(self.values)):
                if self.values[i] == rhs:
                    mask.append(True)
                else:
                    mask.append(False)
        return mask
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload greater than mask method."""
        mask = []
        if type(rhs) is type(self):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    mask.append(True)
                else:
                    mask.append(False)
        if type(rhs) is float:
            for i in range(len(self.values)):
                if self.values[i] > rhs:
                    mask.append(True)
                else:
                    mask.append(False)
        return mask
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription."""
        if type(rhs) is int:
            return self.values[rhs]
        if type(rhs) is list:
            mask = Simpy([])
            for i in range(len(self.values)):
                if rhs[i] is True:
                    mask.values.append(self.values[i])
            self = mask
            return mask