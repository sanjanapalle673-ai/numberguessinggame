# Number Guessing Game
# Internship Task

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Variable to count attempts
attempts = 0

print("===================================")
print(" Welcome to the Number Guessing Game ")
print("===================================")
print("I have chosen a number between 1 and 100.")
print("Try to guess it!")

# Keep asking until the correct number is guessed
while True:
    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("\nCongratulations!")
        print("You guessed the correct number.")
        print("Total attempts:", attempts)
        break