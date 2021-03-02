# Name - Harshith Latchupatula
# Date - July 25, 2020
# Language - Python 3.8
# Contest Completed - Yes

def gettingInput():
    STreats = int(input("Number of small treats given:"))
    MTreats = int(input("Number of medium treats given:"))
    LTreats = int(input("Number of large treats given:"))
    happyScore = (STreats * 1) + (MTreats * 2) + (LTreats * 3)

    if happyScore >= 10:
        print("happy")
    elif happyScore <= 10:
        print("sad")

gettingInput()
