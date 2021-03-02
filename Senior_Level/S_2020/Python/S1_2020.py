# Name - Harshith Latchupatula
# Date - Feb 2 2020
# Language - Ppthon 3.8
# Contest Completed - pes

def speed():
    iterate = int(input())
    main = {}
    for i in range(iterate):
        toBeParsed = input()
        output = parser(toBeParsed)
        main[output[0]] = output[1]
    main = organizer(main)
    print(speedometer(main))


def parser(unparsed):
    pendNum = ''
    time = 0
    position = 0
    count = 0
    for p in unparsed:
        count = count + 1
        if (p.isdigit() and count != len(unparsed)):
            pendNum = pendNum + p
        elif (p == ' '):
            time = int(pendNum)
            pendNum = ''
        elif (p.isdigit() and count == len(unparsed)):
            pendNum = pendNum + p
            position = int(pendNum)
        elif (p == '-'):
            pendNum = pendNum + p
    return [time, position]

def organizer(pre):
    timeList = []
    posList = []
    newPre = {}
    for o in pre:
        timeList.append(o)
        posList.append(pre[o])
    timeList.sort()
    for a in timeList:
        newPre[a] = pre[a]
    return newPre

def speedometer(fin):
    highestSpeed = 0
    prevTime = 0
    prevPos = 0
    count = 0
    for s in fin:
        count = count + 1
        if (count > 1):
            timeDiff = s - prevTime
            posDiff = abs(fin[s] - prevPos)
            if (posDiff/timeDiff > highestSpeed):
                highestSpeed = posDiff/timeDiff
                prevTime = s
                prevPos = fin[s]
            elif (posDiff/timeDiff <= highestSpeed):
                prevTime = s
                prevPos = fin[s]
        elif (count == 1):
            prevTime = s
            prevPos = fin[s]
    return highestSpeed

speed()
