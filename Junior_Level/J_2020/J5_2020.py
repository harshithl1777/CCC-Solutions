# Name - Harshith Latchupatula
# Date - August 27, 2020
# Language - Python 3.8
# Contest Completed - Yes
allRows = []
R = int(input('Enter the first input - '))
C = int(input('Enter the second input - '))

def storeMatrix():
    for x in range(R):
        rowHolder = []
        rowInput = input('Enter the row: ')
        rowLen = len(rowInput)
        print(rowLen)
        count = 0
        for y in range(rowLen):
            num = ''
            if count + 1 <= rowLen:
                if (rowInput[count]).isdigit():
                    num = str(rowInput[count])
                    if count + 2 <= rowLen:
                        if(rowInput[count+1]).isdigit():
                            num = num + str(rowInput[count+1])
                            if count + 3 <= rowLen:
                                if(rowInput[count+2]).isdigit():
                                    num = num + str(rowInput[count+2])
                                    if count + 4 <= rowLen:
                                        if (rowInput[count+3]).isdigit():
                                            num = num + str(rowInput[count+3])
                                            rowHolder.append(int(num))
                                            count = count + 4
                                        else:
                                            rowHolder.append(int(num))
                                            count = count + 4
                                    else:
                                        rowHolder.append(int(num))
                                        break
                                else:
                                    rowHolder.append(int(num))
                                    count = count + 3
                            else:
                                rowHolder.append(int(num))
                                break
                        else:
                            rowHolder.append(int(num))
                            count = count + 2
                    else:
                        rowHolder.append(int(num))
                        break
                else:
                    count = count + 1
            else:
                break
        allRows.append(rowHolder)
    end = R * C
    repeatCheck(end)

def repeatCheck(num):
    for a in allRows:
        countR = -1
        countR = countR + 1
        for b in a:
            countC = -1
            countC = countC + 1
            if b == num:
                if countR == 0 and countC == 0:
                    print("yes")
                    raise SystemExit
                else:
                    nowToCheck = (countR+1) * (countC+1)
                    repeatCheck(nowToCheck)
    print("no")

storeMatrix()

