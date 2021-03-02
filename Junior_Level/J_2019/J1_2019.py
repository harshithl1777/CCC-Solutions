# Name - Harshith Latchupatula
# Date - August 27, 2020
# Language - Python 3.8
# Contest Completed - Yes

def determineWinner():
    a3 = int(input('Enter input - '))
    a2 = int(input('Enter input - '))
    a1 = int(input('Enter input - '))
    b3 = int(input('Enter input - '))
    b2 = int(input('Enter input - '))
    b1 = int(input('Enter input - '))

    a = (a3*3) + (a2*2) + a1
    b = (b3*3) + (b2*2) + b1
    if a > b:
        print('A')
    elif b > a:
        print('B')
    elif b == a:
        print('T')

determineWinner()