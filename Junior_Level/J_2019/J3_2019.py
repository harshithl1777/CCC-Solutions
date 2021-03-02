# Name - Harshith Latchupatula
# Date - August 28, 2020
# Language - Python 3.8
# Contest Completed - Yes

def coldCompression():
    lines = int(input('Enter the number of lines - '))
    allOutputs = []
    for x in range(lines):
        outputLine = []
        strInput = input('Enter the string - ')
        prevStr = ''
        multiplier = 0
        posCount = 0
        for y in strInput:
            posCount = posCount + 1
            if multiplier == 0 and posCount != len(strInput):
                # no prev_not end of str
                prevStr = y
                multiplier = 1
            elif multiplier == 0 and posCount == len(strInput):
                # no prev_end of str
                multiplier = 1
                outputLine.append(str(multiplier) + " " + y)
            elif multiplier != 0 and prevStr == y and posCount != len(strInput):
                # prev exists_current char same_not end of str
                multiplier = multiplier + 1
                prevStr = y
            elif multiplier != 0 and prevStr == y and posCount == len(strInput):
                # prev exists_current char same_end of str
                multiplier = multiplier + 1
                outputLine.append(str(multiplier) + " " + prevStr)
            elif multiplier != 0 and prevStr != y and posCount != len(strInput):
                # prev exists_current char not same_not end of str
                outputLine.append(str(multiplier) + " " + prevStr)
                multiplier = 1
                prevStr = y
            elif multiplier != 0 and prevStr != y and posCount == len(strInput):
                # prev exists_current char not same_end of str
                outputLine.append(str(multiplier) + " " + prevStr)
                outputLine.append(str(1) + " " + y)
        allOutputs.append(outputLine)

    for j in allOutputs:
        master = ''
        count = 0
        for m in j:
            if count == 0:
                master = master + m
                count = count + 1
            elif count >= 1:
                master = master + ' ' + m
                count = count + 1

        print(master)

coldCompression()