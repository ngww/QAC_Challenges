import pytest
from sevennotfive import sevennotfive

def test_sevennotfive_string():
    assert type(sevennotfive()) is str

def test_sevennotfive_list():
    assert type(sevennotfive()) != list