# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game has a gray-ish blue interface. It seems to be running okay, but there are some inconsistencies with the logic. The game visually looks usable, but definitely not perfect yet.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
After submitting a guess, the hint text telling you higher or lower is backwards (it tells you to go higher when the number is lower and vice versa).
You can't properly start a new game once you win. You have to refresh the page.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 50 | Hint says go lower | Hint says go higher | 0: 50 |
| winning then pressing start a new game | Game will reset and attempts will reset | no visible change, gives a new number but cannot play game | none |
| Playing Easy and guessing outside of the 1-20 range | Not the answer | The answer is outside 1-20 range (mine was 78) | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Code for this project, as given to us by the class.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
When looking for bugs, Claude suggested a bug that I had not noticed prior. It suggested that when selecting Easy and starting a new game, it would still be in the range between 1-100, which is incorrect. I did not notice this initially because the random number was in the 1-20 range. I verified the results by reproducing the bug on my end and also looking at the problematic area noted by the AI (app.py134-138).
When fixing the game logic app for giving the correct hint, the AI provided the code that it would replace it with and asked for my permission before changing. I verified by cross-referencing it to the previous code and seeing what important details were changed.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When I was creating a new test for the test_game_logic.py for the first bug I was fixing, I didn't word it properly or clearly enough and it created an entirely different test folder with its own test cases. I verified this by reading what it wanted to edit and then allowing it to edit to fully confirm. In most cases, I would not let the edit go through, but I figured I could revert the changes back and this is a low-stakes environment.
Another small thing it would often do is ask me to change the test cases to fit my current logic, which I felt very dangerous. While I do think the initial tests in tests are not accurate to the tuple logic used in the original app.py, I do not like the idea of altering tests even though it would more accurately suit the problem being tested.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was really fixed when the behavior acts as intended on the deployed app and once I understand how the bug was fixed. We want to be diligent to avoid unintended behaviors and also understand what we are applying to the codebase.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One test I ran was test_winning_guess while I was editing the logic. It kept returning False when I was confident my code worked with the implementation it had previously. That was when I decided to investigate test_winning_guess and noticed how it asserts its tests. The tests do not unpack the tuple at all which is why it fails.
- Did AI help you design or understand any tests? How?
The AI helped me design tests for the two bugs I was testing (difficulty and giving the correct hint). It gave me a guideline and explanation about how to make a test. It also made me understand the tests that was currently there by explaining tuples to me and why the assert may be failing.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
When you interact with the application and input something, Streamlit re-executes the backend code (or the Python script basically). Data in regular Python variables cannot be stored properly and they will get wiped on a rerun. The session state helps keep information between reruns by storing it like a dictionary!

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I want to reuse the testing process and structured strategy. It gives me a guideline on what to do and how to debug with AI.
- What is one thing you would do differently next time you work with AI on a coding task?
I need to be more specific about my prompting. Sometimes, the code would do something I didn't ask it to because I worded it incorrectly and implied a different path. I need to be much more careful, overall.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I think AI generated code can still be very dangerous, especially if you do not understand what it is actually doing, but it can definitely be helpful for finding a starting point.
