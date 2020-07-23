import pytest
from addition import addition

def test_addition():
    assert addition(9) == 11106
    assert addition(3) == 3702
    assert addition(5) == 6170
    assert addition(4) == 4936
    assert addition(7) == 8638
