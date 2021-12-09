# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

print("VIEN ANGELO BERNALES | BSCOE 1-1 \n")

import random

GuessNumber = "True"
User = int(input("GUESS A NUMBER (0-100): "))
randNum = random.randint(0,100)

while GuessNumber == "True":
    if User > randNum:
        print("GREATER THAN")
        User = int(input("TRY AGAIN: "))
        
    if User < randNum:
        print("LOWER THAN")
        User = int(input("TRY AGAIN: "))

    elif User == randNum:
        print("CORRECT!")

