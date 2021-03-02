# Name - Harshith Latchupatula
# Date - August 27, 2020
# Language - Python 3.8
# Contest Completed - Yes

def timeToDecompress():
    toPrint = []
    lines = int(input('Enter number of lines - '))
    for x in range(lines):
        strHolder = ''
        string = input('Enter the input - ')
        num = 0
        char = ''
        lastANum = ''
        for y in string:
            if y.isdigit():
                num = int(y)
                lastANum = True
            elif y.isdigit() and lastANum == True:
                num = int(str(num) + str(y))
            elif y == '':
                pass
            else:
                char = y
                for z in range(num):
                    strHolder = strHolder + char
        toPrint.append(strHolder)
    for a in toPrint:
        print(a.replace(' ', ''))


timeToDecompress()
