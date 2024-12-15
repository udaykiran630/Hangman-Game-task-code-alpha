import random

def choose_word():
    # List of words to choose from
    word_list = ['python', 'hangman', 'programming', 'computer', 'developer', 'function', 'variable']
    return random.choice(word_list)

def display_word(word, guessed_letters):
    # Display the word with guessed letters and underscores for unguessed letters
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    # Welcome message and game setup
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts_left = 6  # Number of attempts before losing
    guessed_word = False

    while attempts_left > 0 and not guessed_word:
        print("\nCurrent word:", display_word(word, guessed_letters))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts_left}")
        
        guess = input("Guess a letter: ").lower()
        
        # Check if the input is a valid letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        # If the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        # Check if the guess is in the word
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            attempts_left -= 1
            print(f"Oops! {guess} is not in the word.")
        
        # Check if the word is fully guessed
        if all(letter in guessed_letters for letter in word):
            guessed_word = True

    if guessed_word:
        print(f"\nCongratulations! You guessed the word '{word}'!")
    else:
        print(f"\nGame over! The word was '{word}'.")

# Start the game
hangman()