import pytest
from rectangle import Rectangle
from random import randint

def test_area():
    for _ in range(20):
        length = randint(1, 100)
        width = randint(1, 100)
        if length != width:
            Rect = Rectangle(length, width)
            assert Rect.area() == length*width
        else:
            pass