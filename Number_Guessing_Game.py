import random

random_number = random.randint(1, 100)
correct_guess = False

try:
    user_input = input("Guess a number between 1 and 100: ")
    number = int(user_input)

    if number == random_number:
        correct_guess = True
        print("You guessed correctly!")

    elif number > random_number:
        print("You guessed too high.")

    elif number < random_number:
        print("You guessed too low.")

except:
    print("Please enter a valid number.")
  
