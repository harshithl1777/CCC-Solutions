# Name - Harshith Latchupatula
# Date - September 11, 2020
# Language - Python 3.8
# Contest Completed - Yes

def favTimes():
    mins = int(input('Enter the number of minutes: '))
    halves = int(mins/720)
    rem = mins - (halves * 720)
    numOfFavorites = halves * 31
    hours = [1200, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]
    time = 1200
    state = 'AM'
    timePassed = 0
    count = 0
    for x in range(rem):
        if timePassed < 59:
            timePassed = timePassed + 1
            time = time + 1
            result = seqChecker(str(time))
            if result:
                numOfFavorites = numOfFavorites + 1
            elif not result:
                pass
        elif timePassed == 59:
            timePassed = 0
            count = count + 1
            time = hours[count]
    print(numOfFavorites)

def seqChecker(time):
    count = 0
    prevNum = 0
    rise = ''
    length = len(time)
    for y in time:
        count = count + 1
        if count == 1:
            prevNum = int(y)
        elif count == 2:
            rise = int(y) - prevNum
            prevNum = int(y)
        elif count > 2:
            if (int(y)-prevNum) == int(rise):
                if count == length:
                    final = True
                else:
                    prevNum = int(y)
            elif (int(y)-prevNum) != int(rise):
                final = False
                break
    if final:
        return True
    else:
        return False

favTimes()



