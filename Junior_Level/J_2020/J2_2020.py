# Name - Harshith Latchupatula
# Date - July 25, 2020
# Language - Python 3.8
# Contest Completed - Yes

def infectionCheck():
    # Getting Inputs
    benchMark = int(input("Enter the first number"))
    firstInfected = int(input("Enter the second number"))
    dailyInfections = int(input("Enter the third number"))

    # Calculating day when infections passes benchmark
    totalInfections = 0
    todayInfections = firstInfected
    infectArray = []
    while totalInfections <= benchMark:
        todayInfections = todayInfections * dailyInfections
        infectArray.append(todayInfections)
        totalInfections = totalInfections + todayInfections
    print(len(infectArray) - 1)

infectionCheck()


