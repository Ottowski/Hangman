import random

# Predefined list of words
word_list = ['hangman', 'developer', 'computer', 'python', 'programming']

# Computer chooses a random word
secret_word = random.choice(word_list)
guessed_letters = []
max_attempts = 6
attempts = 0

# Function to display current status of the word
def display_word():
    display = ''
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

print("Project Hangman!")
print("Guess the word:", display_word())
print(f"You have {max_attempts} attempts.\n")

while attempts < max_attempts:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
    else:
        print("Oops, wrong guess!")
        attempts += 1

    print("Word:", display_word())
    print(f"Wrong guesses: {attempts}/{max_attempts}\n")

    # Check if the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print(f"Congratulations! The word was: {secret_word}")
        print("You won!")
        break
else:
    print(f"Sorry, you lost. The word was: {secret_word}")
