import random

# Generate a random number between 1 and 100
correct_number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number (between 1 and 100): "))

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        if guess == correct_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < correct_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
