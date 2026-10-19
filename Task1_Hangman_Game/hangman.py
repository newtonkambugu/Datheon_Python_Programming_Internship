import random

def play_game():
    with open("words.txt","r") as file:
        words =file.read().splitlines()

    secret_word=random.choice(words).upper()
    guessed_letters=set()
    attempts = 6
    display_word = ["_" for _ in secret_word]

    stages = [
"""
  -----
  |   |
      |
      |
      |
      |
  =========
""",
"""
  -----
  |   |
  O   |
      |
      |
      |
  =========
""",
"""
  -----
  |   |
  O   |
  |   |
      |
      |
  =========
""",
"""
  -----
  |   |
  O   |
 /|   |
      |
      |
  =========
""",
"""
  -----
  |   |
  O   |
 /|\\  |
      |
      |
  =========
""",
"""
  -----
  |   |
  O   |
 /|\\  |
 /    |
      |
  =========
""",
"""
  -----
  |   |
  O   |
 /|\\  |
 / \\  |
      |
  =========
"""
]


    while attempts > 0 and"_" in display_word:
        print(stages[6 - attempts])
        print("Word:", " ".join(display_word))
        print("Guessed Letters:", " ".join(sorted(guessed_letters)))

        guess = input("Enter a letter:").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (A-Z).")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good job! That letter is in the word.")
            for i, letter in enumerate(secret_word):
                if letter==guess:
                    display_word[i]=guess
        else:
            print("Sorry, that letter is not in the word.")
            attempts -=1 

        print("\n")  

    if "_" not in display_word:
        print("Congratulations! You guessed the word:",secret_word)
    else:
        print(stages[-1])
        print("Game Over! The word was:", secret_word)

while True:
    play_game()
    again = input("Do you want to play again? (Y/N): ").upper()
    if again != "Y":
        print("Thanks for playing Hangman! Goodbye")
        break                 