# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

print("VIEN ANGELO BERNALES | BSCOE1-1 \n")

import random

print("WELCOME PLAYER!")
Start = "y"

while Start == "y":
    firstNum = int(input("ENTER YOUR FIRST NUMBER: "))
    secondNum = int(input("ENTER YOUR SECOND NUMBER: "))
    thirdNum = int(input("ENTER YOUR THIRD NUMBER: "))
    randNum1 = random.randint(0,9)
    randNum2 = random.randint(0,9)
    randNum3 = random.randint(0,9)

    if (firstNum and secondNum and thirdNum) in (randNum1 and randNum2 and randNum3):
        print(f"CONGRATS! YOU ARE A WINNER!")
    
    else:
        print(f"You loss :<")
        print(f"The winning numbers are: {randNum1}, {randNum2}, {randNum3}.")
        Start = input("Try again? y/n: ")

if Start == "n":
    print("THANK YOU, BETTER LUCK NEXT TIME!")