# Name - Harshith Latchupatula
# Date - August 29, 2020
# Language - Python 3.8
# Contest Completed - Yes

def flipper():
    square = [[1, 2], [3, 4]]
    order = input('Enter the flip order: ')
    for x in order:
        if x == 'H':
            square = horizantal(square)
        elif x == 'V':
            square = vertical(square)
    printer(square)


def horizantal(matrix1):
    matrix1[0].reverse()
    matrix1[1].reverse()
    return matrix1

def vertical(matrix2):
    matrix2.reverse()
    return matrix2


def printer(matrix3):
    for y in matrix3:
        print(str(y[0]) + " " + str(y[1]))


flipper()
