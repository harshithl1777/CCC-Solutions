# Name - Harshith Latchupatula
# Date - September 13, 2020
# Language - Python 3.8
# Contest Completed - Yes

def palindrome():
    text = input('Enter: ')
    posCount = 0
    combs = []
    for a in text:
        posCount = posCount + 1
        includeCount = 0
        totalExc = ''
        for b in text:
            includeCount = includeCount + 1
            if includeCount < posCount:
                pass
            elif includeCount >= posCount:
                totalExc = totalExc + b
                combs.append(totalExc)
    allPalins = palinCompiler(combs)
    findLongest(allPalins)

def palinCompiler(array):
    newPalins = []
    for c in array:
        strHolder = ''
        for d in c:
            strHolder = d + strHolder
        if strHolder == c:
            newPalins.append(strHolder)
        elif strHolder != c:
            pass
    return newPalins

def findLongest(array2):
    toBeat = ''
    for x in array2:
        if toBeat == '':
            toBeat = len(x)
        elif toBeat != '':
            if toBeat >= len(x):
                pass
            elif toBeat < len(x):
                toBeat = len(x)
    print(toBeat)

palindrome()