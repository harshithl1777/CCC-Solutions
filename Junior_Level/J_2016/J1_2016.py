# Name - Harshith Latchupatula
# Date - September 13, 2020
# Language - Python 3.8
# Contest Completed - Yes

def tourneySelection():
    wins = 0
    for x in range(6):
        result = input('Enter: ')
        if result == 'W':
            wins = wins + 1
        elif result == 'L':
            pass
    if wins == 1 or wins == 2:
        print('3')
    elif wins == 3 or wins == 4:
        print('2')
    elif wins == 5 or wins == 6:
        print('1')
    elif wins == 0:
        print('-1')

tourneySelection()
