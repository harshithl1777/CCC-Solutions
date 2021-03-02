# Name - Harshith Latchupatula
# Date - September 8, 2020
# Language - Python 3.8
# Contest Completed - Yes

def shiftySum():
    num = int(input('Enter the number: '))
    shifts = int(input('Enter the number: '))
    shiftSum = num
    for x in range(shifts):
        singleNum = str(num)
        ending = ''
        for y in range(x+1):
            ending = ending + '0'
        singleNum = singleNum + ending
        shiftSum = shiftSum + int(singleNum)
    print(shiftSum)


shiftySum()