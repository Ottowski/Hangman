import random
import tkinter as tk
from tkinter import messagebox

# Predefined list of words
word_list = ['hangman', 'developer', 'computer', 'python', 'programming']

# Computer chooses a random word
secret_word = ""
guessed_letters = []
max_attempts = 6
attempts = 0

# Setup main window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x300")

# UI Components
word_label = tk.Label(root, text="", font=20)
word_label.pack(pady=10)

info_label = tk.Label(root, text="Guess a letter or the full word:")
info_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()
guess_entry.bind("<Return>", lambda event: check_guess())

attempts_label = tk.Label(root, text="")
attempts_label.pack(pady=10)

guessed_label = tk.Label(root, text="Guessed letters: ")
guessed_label.pack(pady=5)


def display_word():
    display = ''
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()


def update_display():
    word_label.config(text=display_word())
    attempts_label.config(text=f"Attempts left: {max_attempts - attempts}")
    guessed_label.config(text=f"Guessed letters: {', '.join(guessed_letters)}")


def check_guess():
    global attempts

    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if not guess.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter only letters.")
        return

    if len(guess) > 1:
        # Full word guess
        if guess == secret_word:
            update_display()
            messagebox.showinfo("You Win!", f"Nice! You guessed the word: {secret_word}")
            ask_restart()
        else:
            attempts += 1
            if attempts >= max_attempts:
                update_display()
                messagebox.showinfo("Game Over", f"Sorry, you lose. The word was: {secret_word}")
                ask_restart()
            else:
                messagebox.showinfo("Incorrect", f"'{guess}' is not the word.")
        update_display()
        return

    # Single letter guess
    if guess in guessed_letters:
        messagebox.showinfo("Already Guessed", f"You already guessed '{guess}'.")
        return

    guessed_letters.append(guess)

    if guess in secret_word:
        if all(letter in guessed_letters for letter in secret_word):
            update_display()
            messagebox.showinfo("You Win!", f"Congratulations! The word was: {secret_word}")
            ask_restart()
    else:
        attempts += 1
        if attempts >= max_attempts:
            update_display()
            messagebox.showinfo("Game Over", f"Sorry, you lose. The word was: {secret_word}")
            ask_restart()

    update_display()


def start_new_game():
    global secret_word, guessed_letters, attempts
    secret_word = random.choice(word_list)
    guessed_letters = []
    attempts = 0
    update_display()


def ask_restart():
    again = messagebox.askyesno("Play Again?", "Do you want to play again?")
    if again:
        start_new_game()
    else:
        root.destroy()


guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack(pady=5)

# Start game
start_new_game()
root.mainloop()
