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

print("WELCOME PLAYER! \n")
Start = "y"

FNumber = int(random.randint(0,9))
SNumber = int(random.randint(0,9))
TNumber = int(random.randint(0,9))

def Lottery(Start):
    while Start == "y":
        FirstNum = int(input("ENTER YOUR FIRST NUMBER: "))
        SecondNum = int(input("ENTER YOUR SECOND NUMBER: "))
        ThirdNum = int(input("ENTER YOUR THIRD NUMBER: "))
        
        if FirstNum == FNumber and SecondNum == SNumber and ThirdNum == TNumber:
            print("Winner")
            print(f"THE WINNING NUMBERS ARE {FNumber}, {SNumber}, AND {TNumber}. ")
            Start = "n"
            Start = input("Try again? y/n: ")
            
        else:
            print(f"You lose.")
            print(f"THE WINNING NUMBERS ARE {FNumber}, {SNumber}, AND {TNumber}. ")
            Start = "n"
            Start = input("Try again? y/n: ")
            
    if Start == "n":
        print("THANK YOU, BETTER LUCK NEXT TIME!")

Lottery(Start)