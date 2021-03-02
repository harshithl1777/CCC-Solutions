# Name - Harshith Latchupatula
# Date - September 3, 2020
# Language - Python 3.8
# Contest Completed - Yes

poses = [0]
dists = []

def thereYet():
    distInput = input('Enter the distances: ')
    count = -1
    prevNumTr = ''
    posHold = ''
    for x in distInput:
        count = count + 1
        if x.isdigit():
            prevNumTr = True
            if prevNumTr:
                if (count + 1) == len(distInput):
                    posHold = posHold + str(x)
                    sendIn(int(posHold))
                else:
                    posHold = posHold + str(x)
                    prevNumTr = True
            elif not prevNumTr:
                posHold = x
                prevNumTr = True
        else:
            sendIn(int(posHold))
            prevNumTr = False
            posHold = ''
    makePos()

def sendIn(inte):
    dists.append(int(inte))

def makePos():
    count2 = -1
    sums = 0
    for z in dists:
        count2 = count2 + 1
        if count2 == 0:
            sums = sums + z
            poses.append(z)
        elif count2 != 0:
            poses.append(sums + z)
            sums = sums + z
    printer()

def printer():
    for a in poses:
        printLine = ''
        count3 = 0
        for b in poses:
            count3 = count3 + 1
            finDist = b - a
            if finDist < 0:
                finDist = finDist * (-1)
            else:
                pass
            if count3 == 1:
                printLine = printLine + str(finDist)
            else:
                printLine = printLine + ' ' + str(finDist)
        print(printLine)

thereYet()

