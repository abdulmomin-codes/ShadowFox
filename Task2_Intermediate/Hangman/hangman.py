# #hangman game
# Word Selection: Choose a random word from a predefined list.
# Game Setup: Initialize variables for the chosen word, guessed letters, incorrect
# guesses, and maximum allowed attempts.
# Display Interface: Create a simple text-based interface showing the hangman
# figure and the partially revealed word.
# User Input: Prompt the player to guess a letter and validate the input.
# Check Guess: Validate the guessed letter against the word and update the
# interface accordingly.
# Win/Loss Conditions: Continuously check for win or loss conditions.
# Game Loop: Implement a loop to keep the game running until the player wins or
# loses.
# Play Again: Offer the option to play again once the game concludes. Reset the
# game state if chosen.
import random
categories = {
    "Animals": ["tiger", "lion", "elephant", "giraffe", "zebra"],
    "Countries": ["india", "canada", "japan", "brazil", "germany"],
    "Programming": ["python", "java", "coding", "developer", "algorithm"]
}




hangman_art = {0: (
               "  +---+",
    "  |   |",
    "      |",
    "      |",
    "      |",
    "      |",
    "========="
), 
1: (
    "  +---+",
    "  |   |",
    "  O   |",
    "      |",
    "      |",
    "      |",
    "========="
),   
2: (
    "  +---+",
    "  |   |",
    "  O   |",
    "  |   |",
    "      |",
    "      |",
    "========="
),
3: (
    "  +---+",
    "  |   |",
    "  O   |",
    " /|   |",
    "      |",
    "      |",
    "========="
),
4: (
    "  +---+",
    "  |   |",
    "  O   |",
    " /|\\  |",
    "      |",
    "      |",
    "========="
),
5: (
    "  +---+",
    "  |   |",
    "  O   |",
    " /|\\  |",
    " /    |",
    "      |",
    "========="
),
6: (
    "  +---+",
    "  |   |",
    "  O   |",
    " /|\\  |",
    " / \\  |",
    "      |",
    "========="
)
}


def display_hangman(wrong_guesses):
    print("*************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*************")    
def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    print(" ".join(answer))
def play_game():
    print("Choose a category:")
    for category in categories:
      print("-", category)

    selected_category = input("Enter category: ").title()

    while selected_category not in categories:
      print("Invalid category. Please try again.")
      selected_category = input("Enter category: ").title()

    answer = random.choice(categories[selected_category])
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        print("Guessed Letters:", sorted(guessed_letters))
        guess = input("Guess a letter: ").lower()


        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                print("Correct guess!")
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1
            print("Wrong guess!")
        
        
        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("Congratulations! You've guessed the word:", answer)
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("Game Over! The word was:", answer)
            is_running = False


if __name__ == "__main__":
    while True:
        play_game()

        play_again = input("\nDo you want to play again? (y/n): ").lower()

        if play_again != "y":
            print("Thanks for playing!")
            break
