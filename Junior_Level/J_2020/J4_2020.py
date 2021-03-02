# Name - Harshith Latchupatula
# Date - July 26, 2020
# Language - Python 3.8
# Contest Completed - Yes

def cyclicShiftCheck():
    testPiece = input("Enter the text: ")
    refString = input("Enter the string: ")
    stringLen = len(refString)
    cyclicArray = []
    count = 1
    arrayCount = 0
    for i in range(stringLen):
        lastC = refString[stringLen - 1]
        startPart = refString[0:stringLen-1]
        refString = lastC + startPart
        cyclicArray.append(refString)
    while count <= stringLen:
        whatToCheckFor = cyclicArray[arrayCount]
        inString = testPiece.find(whatToCheckFor)
        if inString != -1:
            print("yes")
            break
        else:
            count = count + 1
            arrayCount = arrayCount + 1
    print("no")

cyclicShiftCheck()
