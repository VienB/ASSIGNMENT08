# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

print("VIEN ANGELO BERNALES | BSCOE 1-1 \n")

import random

User = int(input("ENTER YOUR GUESS NUMBER: "))
randNum = random.randint(0, 100)

while randNum != User:
    if User < randNum:
        print("\nGREATER THAN")
        User = int(input("TRY AGAIN:"))

    elif User > randNum:
        print("\nLESS THAN")
        User = int(input("TRY AGAIN:"))

if User == randNum:
        print("\nYOU ARE CORRECT!")
        exit


