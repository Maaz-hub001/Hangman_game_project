import random

def play_hangman():
    # 1. Predefined list of 5 secret words
    words = ["python", "programming", "hangman", "developer", "antigravity"]
    
    # Randomly select a word from the list
    secret_word = random.choice(words)
    
    # Keep track of the guessed letters
    guessed_letters = set()
    
    # Limit incorrect guesses to 6
    max_incorrect_guesses = 6
    incorrect_guesses = 0
    
    print("=========================================")
    print("       Welcome to Hangman Game!          ")
    print("=========================================")
    print(f"I have chosen a secret word. You have {max_incorrect_guesses} incorrect guesses allowed.")
    print("Let's start!\n")
    
    while incorrect_guesses < max_incorrect_guesses:
        # Display the current state of the word
        # (e.g., 'p _ _ h _ _' if 'python' is the word and 'p' & 'h' are guessed)
        displayed_word = []
        for letter in secret_word:
            if letter in guessed_letters:
                displayed_word.append(letter)
            else:
                displayed_word.append("_")
        
        current_state = " ".join(displayed_word)
        print(f"Word: {current_state}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        if guessed_letters:
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        # Win condition check: if no underscores are left in the displayed word
        if "_" not in displayed_word:
            print("\n🎉 Congratulations! You guessed the word correctly!")
            print(f"The secret word was indeed: '{secret_word}'")
            break
            
        # Get player's guess
        try:
            guess = input("Guess a letter: ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nGame aborted. Goodbye!")
            return
        
        # Input Validation
        if not guess:
            print("❌ Input cannot be empty. Please enter a letter.\n")
            continue
        if len(guess) != 1:
            print("❌ Please enter only a single letter.\n")
            continue
        if not guess.isalpha():
            print("❌ Please enter a valid alphabetical letter.\n")
            continue
        if guess in guessed_letters:
            print(f"❌ You have already guessed '{guess}'. Try a different letter.\n")
            continue
            
        # Add to the set of guessed letters
        guessed_letters.add(guess)
        
        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f"⭐ Correct! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"❌ Sorry, '{guess}' is not in the word.\n")
            
    else:
        # Lose condition check (if the loop completes without break)
        print("=========================================")
        print("💀 GAME OVER! bye bye!")
        print(f"You've run out of incorrect guesses.")
        print(f"The secret word was: '{secret_word}'")
        print("=========================================")

if __name__ == "__main__":
    play_hangman()
