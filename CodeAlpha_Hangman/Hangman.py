import random

def choose_word():
    words = [
    "python",
    "computer",
    "programming",
    "developer",
    "software",
    "hardware",
    "algorithm",
    "database",
    "network",
    "debugging",
    "compiler",
    "function",
    "variable",
    "iteration",
    "condition",
    "automation",
    "technology",
    "engineering",
    "application",
    "framework"
]

    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("\n🎮 WELCOME TO ADVANCED HANGMAN GAME 🎮")
    print("Guess the word, one letter at a time")
    print("You have 6 incorrect attempts\n")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed Letters:", ", ".join(guessed_letters))
        print("Remaining Attempts:", attempts)

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Invalid input! Enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good job! Letter found.")
        else:
            attempts -= 1
            print("❌ Wrong guess!")

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 CONGRATULATIONS! YOU WON 🎉")
            print("The word was:", word)
            break
    else:
        print("\n💀 GAME OVER 💀")
        print("The word was:", word)

if __name__ == "__main__":
    hangman()

