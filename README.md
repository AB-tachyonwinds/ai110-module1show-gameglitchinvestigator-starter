# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User decides to stay on Normal difficulty
2. User enters a guess of 20
3. Game returns "Too Low"
4. User enters a guess of 70 → "Too High"
5. Score updates correctly after each guess
6. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
=============================================================================== test session starts ===============================================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\angel\AppData\Local\Python\pythoncore-3.14-64\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\angel\Downloads\projects\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 6 items                                                                                                                                                                  
tests/test_game_logic.py::test_win_with_string_secret PASSED                                                                                                                 [ 16%]
tests/test_game_logic.py::test_too_high_with_string_secret PASSED                                                                                                            [ 33%]
tests/test_game_logic.py::test_too_low_with_string_secret PASSED                                                                                                             [ 50%]
tests/test_game_logic.py::test_easy_range PASSED                                                                                                                             [ 66%]
tests/test_game_logic.py::test_hard_range PASSED                                                                                                                             [ 83%]
tests/test_game_logic.py::test_unknown_difficulty_defaults_to_normal_range PASSED                                                                                            [100%]

================================================================================ 6 passed in 0.02s ================================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
