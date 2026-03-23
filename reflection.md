# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The page showed a simple number guessing game where I had to guess a number between 1 and 100. There was an input box to enter a number and a Submit button to check the guess. After submitting a guess, the game displayed a hint telling me whether I should guess higher or lower.

### Three concrete bugs I noticed at the start

### Bug 1

The hints were sometimes incorrect. For example, when the secret number was 40 and I entered 50, the game told me to guess higher, even though my guess was already higher than the correct number. This means the hint logic is reversed or incorrect.

### Bug 1 Fix: Incorrect hint logic

- Issue: The game gave the wrong hint when the guess was higher than the secret number.
- What I did: I used Copilot and asked it to analyze the comparison logic.
- What AI suggested: Copilot identified that the greater-than condition was reversed and corrected the return messages.
- Final fix: I updated the logic so that when guess > secret, the game tells the player to go lower.
- Result: The hints now correctly guide the player.

### Bug 2

The “Play New Game” button does not properly restart the game. When I press the button, it sometimes displays the message “You already won. Start a new game to play again.” instead of actually resetting the game.

### Bug 2 Fix: New Game button not resetting

- Issue: Pressing "Play New Game" did not properly restart the game. It sometimes still showed the message "You already won."
- What I did: I used Copilot and asked it to analyze how session state was being handled.
- What AI suggested: Copilot updated the New Game logic to fully reset all session state variables, including attempts, secret number, status, history, and score. It also cleared the input field and used st.rerun() to refresh the app.
- Final fix: I applied the updated logic so that all game variables are reinitialized when the button is pressed.
- Result: The game now restarts correctly with a fresh state every time.

3. Difficulty mode updates incorrectly. When I switch between Easy, Medium, and Hard, the number of attempts and the number range displayed do not match the selected mode, which makes the game confusing.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

### Correct AI Suggestion

- What the AI suggested: Copilot identified that the hint logic was reversed and suggested fixing the comparison so that when the guess is higher than the secret number, the game tells the user to go lower.
- Was it correct?: Yes, it was correct.
- How I verified it: I tested the game manually and also wrote pytest tests to confirm that higher guesses return "Too High" and correct hints.

---

### Incorrect or Misleading AI Suggestion

- What the AI suggested: Copilot did not fully fix the difficulty bug and missed that the function get_range_for_difficulty was not implemented in logic_utils.py.
- Was it correct?: It was incomplete and misleading because it did not address the missing function implementation.
- How I verified it: I ran pytest and saw failing tests with a NotImplementedError, which showed the function needed to be implemented manually.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

### Debugging and Testing

- I used pytest to verify my fixes by creating test cases for both the hint logic and difficulty range.
- Initially, some tests failed due to missing implementation in logic_utils.py.
- After fixing the issues, all tests passed successfully.
- I also ran the app using Streamlit and manually tested:
  - Hint messages (high/low)
  - Difficulty changes
  - Game reset functionality
- This confirmed that the game behaves correctly after the fixes.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
