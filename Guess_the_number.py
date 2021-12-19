import random

number = random.randrange(1, 2)
try:
    guess = int(input("Guess the number :"))

    while guess != number:
        if guess > number:
            print("To big !")
            guess = int(input("Guess the number :"))
        else:
            print("To small !")
            guess = int(input("Guess the number :"))
except ValueError:
    print("It's not a number!")
    guess = int(input("Guess the number :"))


if guess == number:
    print("You win")
