import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logic_utils import get_range_for_difficulty


def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert (low, high) == (1, 20)


def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert (low, high) == (1, 100)


def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert (low, high) == (1, 50)
