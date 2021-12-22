import random

'''
1. Ask the question "Guess the number:" and retrieve the number from the keyboard.
2. Check if the entered text is really a number and in the event of an error display the message "It's not a number!", 
Then go back to pt. 1
3. If the number entered by the user is less than the random number, display the message "To small!", 
Then return to pt. 1.
4. If the number given by the user is greater than the randomly selected number, display the message "To big!", 
Then go back to pt. 1.
5. If the number entered by the user is equal to the random number, 
display the message "You win!" And exit the program. 
'''

number = random.randrange(1, 100)
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
    print("You win!")
