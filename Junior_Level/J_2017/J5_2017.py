# Name - Harshith Latchupatula
# Date - September 12, 2020
# Language - Python 3.8
# Contest Completed - Partially

def nailedIt():
    numWood = int(input('Enter the number of wood pieces: '))
    heightsStr = input('Enter the wood heights: ')
    wHeights = []
    count = 0
    numSoFar = ''
    for x in heightsStr:
        count = count + 1
        if count == 1:
            numSoFar = x
        elif count != 1 and count != len(heightsStr):
            if x.isdigit():
                numSoFar = numSoFar + x
            elif not x.isdigit():
                wHeights.append(int(numSoFar))
                numSoFar = ''
        elif count == len(heightsStr):
            numSoFar = numSoFar + x
            wHeights.append(int(numSoFar))
    wHeights.append(0)
    allSums = summer(wHeights)
    print(allSums)
    finalModer(allSums)

def summer(numsArr):
    prevDone = []
    sumHolder = []
    sums = []
    firstCount = 0
    secondCount = 0
    for y in numsArr:
        secondCount = 0
        firstCount = firstCount + 1
        for z in numsArr:
            secondCount = secondCount + 1
            if secondCount <= firstCount:
                pass
            else:
                theSum = y + z
                sums.append(theSum)
        prevDone.append(y)
    return sums

def finalModer(allSums):
    modes = []
    alreadyDone = []
    count2 = 0
    greaterThan = ''
    for a in allSums:
        if alreadyDone.count(a) == 0:
            mode = allSums.count(a)
            modes.append(mode)
            alreadyDone.append(a)
        else:
            pass
    print(modes)
    for b in modes:
        count2 = count2 + 1
        if count2 == 1:
            greaterThan = b
        elif count2 != 1:
            if b > greaterThan:
                greaterThan = b
            elif b < greaterThan:
                pass
            elif b == greaterThan:
                pass
    print(str(greaterThan) + ' ' + str(modes.count(greaterThan)))



nailedIt()