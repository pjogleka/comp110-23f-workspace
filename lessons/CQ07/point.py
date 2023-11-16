"""CQ07."""

from __future__ import annotations

__author__ = '730569616'


class Point:
    """Defining a new class."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """My constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int):
        """Scale by mutating."""
        self.x *= factor
        self.y *= factor
        return self.x, self.y
    
    def scale(self, factor: int) -> Point:
        """New point with scale."""
        new_Point: Point = Point(self.x, self.y)
        new_Point.x = self.x * factor
        new_Point.y = self.y * factor
        return new_Point
    
    def __str__(self) -> None:
        """Overload str."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """Overload mul."""
        new_Point = Point(self.x * factor, self.y * factor)
        return new_Point
    
    def __add__(self, factor: int | float) -> Point:
        """Overload add."""
        new_Point = Point(self.x + factor, self.y + factor)
        return new_Point