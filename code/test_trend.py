import pytest
from feature_judge import *

def test_monotone_increase():
    result = trend_judge()
    assert result == True

def test_high_two():
    result = threadshold_judge()
    assert result == True

