# Name - Harshith Latchupatula
# Date - August 30, 2020
# Language - Python 3.8
# Contest Completed - Yes

def occupyParking():
    checkCount = -1
    totalSimilar = 0
    spots = int(input('Enter the number of spots: '))
    ySpots = input('Enter the spots from yesterday: ')
    tSpots = input('Enter the spots from today: ')

    for a in ySpots:
        checkCount = checkCount + 1
        if a == 'C':
            if a == tSpots[checkCount]:
                totalSimilar = totalSimilar + 1
            else:
                pass
        else:
            pass
    print(totalSimilar)

occupyParking()
