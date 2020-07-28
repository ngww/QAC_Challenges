import pytest
from amsterdam import name

def test_name():
    assert name("Am I in Amsterdam") == 1

# Test that caps doesn't matter, will still pick up "am"
def test_caps():
    assert name("Am AM aM am") == 4

# Test that a sentence with no "am" returns 0
def test_no_am():
    assert name("I have been in Amsterdam") == 0

