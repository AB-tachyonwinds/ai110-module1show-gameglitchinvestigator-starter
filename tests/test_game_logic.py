from logic_utils import check_guess, get_range_for_difficulty
# Generated the below tests with the help of agent mode
def test_win_with_string_secret():
    # A correct guess must register as a Win even when secret is a string.
    outcome, _ = check_guess(50, "50")
    assert outcome == "Win"

def test_too_high_with_string_secret():
    # 9 vs 100: numerically too LOW. Lexicographic comparison ("9" > "100")
    # would wrongly say "Too High" — guard against that regression.
    outcome, _ = check_guess(9, "100")
    assert outcome == "Too Low"


def test_too_low_with_string_secret():
    outcome, _ = check_guess(80, "50")
    assert outcome == "Too High"


def test_easy_range():
    # Easy difficulty spans 1 to 20 inclusive.
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_hard_range():
    # Hard difficulty spans 1 to 50 inclusive.
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_unknown_difficulty_defaults_to_normal_range():
    # Any unrecognized difficulty falls back to the Normal range (1 to 100).
    assert get_range_for_difficulty("Bogus") == (1, 100)

