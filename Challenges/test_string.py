import pytest
from string_gen import string_gen

def test_string_string():
    assert type(string_gen()) is str

def test_string_len():
    assert len(string_gen()) == 5

def test_string_lowercase():
    string = string_gen()
    assert string.islower()