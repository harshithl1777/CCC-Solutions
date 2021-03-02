# Name - Harshith Latchupatula
# Date - September 13, 2020
# Language - Python 3.8
# Contest Completed - Yes

def magicSquares():
    square = []
    for x in range(4):
        rowStr = input('Enter: ')
        count = 0
        prevNum = ''
        rowHolder = []
        for y in rowStr:
            count = count + 1
            if count == 1:
                prevNum = y
            elif count != 1 and count != len(rowStr) and y.isdigit():
                prevNum = prevNum + y
            elif count != 1 and count != len(rowStr) and not y.isdigit():
                rowHolder.append(int(prevNum))
                prevNum = ''
            elif count == len(rowStr):
                prevNum = prevNum + y
                rowHolder.append(int(prevNum))
        square.append(rowHolder)
    print(checker(square))

def checker(array):
    rowSum = ''
    for a in array:
        totalThusFar = 0
        for b in a:
            totalThusFar = totalThusFar + b
        if rowSum == '':
            rowSum = totalThusFar
        else:
            if rowSum == totalThusFar:
                pass
            elif rowSum != totalThusFar:
                return 'not magic'
    col = -1
    colSums = []
    for z in range(4):
        col = col + 1
        sumSoFar = 0
        for c in array:
            sumSoFar = sumSoFar + c[col]
        colSums.append(sumSoFar)
    prevSum = ''
    for e in colSums:
        if prevSum == '':
            prevSum = e
        elif prevSum != '':
            if e == prevSum:
                pass
            elif e != prevSum:
                return 'not magic'
    return 'magic'







magicSquares()


