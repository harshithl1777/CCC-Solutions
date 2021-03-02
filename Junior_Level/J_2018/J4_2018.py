# Name - Harshith Latchupatula
# Date - September 5, 2020
# Language - Python 3.8
# Contest Completed - Yes

lines = int(input())
rows = []
nums = []
def sunflowers():
    for a in range(lines):
        hold = input()
        rows.append(hold)
    for b in rows:
        rowHold = []
        count = 0
        prevNumTr = ''
        prevNumHold = ''
        for c in b:
            count = count + 1
            if count != len(b):
                if c.isdigit() and count == 1:
                    prevNumHold = str(c)
                    prevNumTr = True
                elif c.isdigit() and count != 1:
                    prevNumHold = prevNumHold + str(c)
                    prevNumTr = True
                elif not c.isdigit():
                    rowHold.append(int(prevNumHold))
                    prevNumTr = False
                    prevNumHold = ''
            elif count == len(b):
                prevNumHold = prevNumHold + str(c)
                rowHold.append(int(prevNumHold))
        nums.append(rowHold)
    result1, finalSq = clockwise(nums)
    if result1:
        for i in finalSq:
            posCount = 0
            printer = ''
            for j in i:
                posCount = posCount + 1
                if posCount != lines:
                    printer = printer + str(j) + ' '
                elif posCount == lines:
                    printer = printer + str(j)
            print(printer)
    elif not result1:
        result2, finalSq = counterclock(nums)
        for i in finalSq:
            posCount = 0
            printer = ''
            for j in i:
                posCount = posCount + 1
                if posCount != lines:
                    printer = printer + str(j) + ' '
                elif posCount == lines:
                    printer = printer + str(j)

def clockwise(entry):
    master = []
    for g in range(lines):
        singleR = []
        for h in entry:
            oneNum = h[g]
            singleR.insert(0, oneNum)
        master.append(singleR)
    check = checker(master)
    if check == True:
        return True, master
    elif check == False:
        clockwise(master)


def counterclock(enter):
    master = []
    for g in range(lines):
        singleR = []
        for h in enter:
            oneNum = h[(lines - 1) - g]
            singleR.append(oneNum)
        master.append(singleR)
    check = checker(master)
    if check == True:
        return True, master
    elif check == False:
        counterclock(master)

def checker(entry):
    for m in range(lines):
        checkRow = []
        for n in entry:
            oneNum = n[(lines - 1) - m]
            checkRow.append(oneNum)
        prevNumb = ''
        counter = 0
        for o in checkRow:
            counter = counter + 1
            if counter == 1:
                prevNumb = o
            elif counter != 1:
                if o > prevNumb:
                    pass
                    prevNumb = o
                elif o < prevNumb:
                    return False
    for p in range(lines):
        for q in entry:
            prevNumb = ''
            counter = 0
            for r in q:
                counter = counter + 1
                if counter == 1:
                    prevNumb = o
                elif counter != 1:
                    if o > prevNumb:
                        pass
                        prevNumb = o
                    elif o < prevNumb:
                        return False
    return True

sunflowers()