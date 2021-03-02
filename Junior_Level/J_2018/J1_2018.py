# Name - Harshith Latchupatula
# Date - August 30, 2020
# Language - Python 3.8
# Contest Completed - Yes

def telemarketer():
    num = ''
    for x in range(4):
        digit = str(input('Enter the digit: '))
        num = num + digit
    if (num[0] == '8' or num[0] == '9') and (num[1] == num[2]) and (num[3] == '8' or num[3] == '9'):
        print('ignore')
    else:
        print('answer')

telemarketer()