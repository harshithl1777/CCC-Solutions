# Name - Harshith Latchupatula
# Date - September 8, 2020
# Language - Python 3.8
# Contest Completed - Yes

def quadSelection():
    xC = int(input('Enter the x coordinate: '))
    yC = int(input('Enter the y coordinate: '))

    if xC > 0 and yC > 0:
        print('1')
    elif xC < 0 and yC > 0:
        print('2')
    elif xC < 0 and yC < 0:
        print('3')
    elif xC > 0 and yC < 0:
        print('4')


quadSelection()
