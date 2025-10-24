import random

# Predefined list of 5 words
word_list = ["apple", "zebra", "robot", "chair", "plant"]

# Scoreboard
wins = 0
losses = 0

while True:
    # Randomly choose a word from the list
    secret_word = random.choice(word_list)

    # Variables for the game state
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    # Create a display version of the word with underscores
    display_word = ["_" for _ in secret_word]

    # Game loop
    while incorrect_guesses < max_incorrect and "_" in display_word:
        print("\nCurrent word: " + " ".join(display_word))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        print("Guessed letters so far:", " ".join(guessed_letters))
        
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
            # Reveal the letter in display_word
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess
        else:
            print(f"❌ Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

    # End of game
    print()
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", secret_word)
        wins += 1
    else:
        print("😢 You're out of guesses. The word was:", secret_word)
        losses += 1

    # Show scoreboard
    print(f"\n📊 Scoreboard → Wins: {wins} | Losses: {losses}")

    # 🔁 Ask if player wants to replay
    play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
    if play_again != 'y':
        print(f"\n👋 Thanks for playing Hangman! Final Score → Wins: {wins} | Losses: {losses}")
        break
