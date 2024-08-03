import random

def choose_word():
    words = ["fish","egg","crab","soup","sruzz","bar","gayu"]
    return random.choice(words)

def display_word(word,guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman!")
    while attempts > 0:
        print("\nAttempts left:", attempts)
        display = display_word(word_to_guess, guessed_letters)
        print(display)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        if display == word_to_guess:
            print("Congratulations! You've guessed the word:",word_to_guess)
            break
        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct!")
        else:
            if attempts == 6:
                print(" O ")
            if attempts == 5:
                print(" O ")
                print(" | ")
            if attempts == 4:
                print(" O ")
                print("/| ")
            if attempts == 3:
                print(" O ")
                print("/|\ ")
            if attempts == 2:
                print(" O ")
                print("/|\ ")
                print("/")
            if attempts == 1:
                print(" O ")
                print("/|\ ")
                print("/ \ ")
            attempts -= 1
    if attempts == 0:
        print("\nGame over! The word was:", word_to_guess)
hangman()
