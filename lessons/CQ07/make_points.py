"""Tests."""

from lessons.CQ07.point import Point

point = Point(5, 5)

scaled = Point.scale(point, 3)

print(scaled.y)