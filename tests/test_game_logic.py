import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logic_utils import check_guess, get_range_for_difficulty


def test_guess_win():
    # guess equal to secret -> Win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # guess greater than secret -> Too High
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # guess less than secret -> Too Low
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
