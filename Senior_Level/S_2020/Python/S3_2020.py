needle = input()
hay = input()

def findComb():
    strHold = ''
    combs = []
    count = -1
    for x in hay:
        count = count + 1
        if (count <= len(hay)-len(needle)):
            strHold = hay[count:count+(len(needle))]
            if(combs.count(strHold) == 0):
                combs.append(strHold)
            else:
                pass
        else:
            break
    checkPerm(combs)

def checkPerm(combList):
    foundNum = 0
    for b in combList:
        neeArr = []
        possible = False
        for a in needle:
            neeArr.append(a)
        for c in b:
            if (neeArr.count(c) > 0):
                neeArr.pop(neeArr.index(c))
                possible = True
            elif (neeArr.count(c) == 0):
                pass
                possible = False
                break
        if possible:
            foundNum = foundNum + 1
    print(foundNum)


findComb()