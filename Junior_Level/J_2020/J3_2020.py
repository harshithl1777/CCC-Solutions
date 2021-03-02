# Name - Harshith Latchupatula
# Date - July 26, 2020
# Language - Python 3.8
# Contest Completed - Yes

def findFrame():
    numberOfDrops = int(input("Enter the number of drops: "))
    xArray = []
    yArray = []
    for i in range(numberOfDrops):
        coordinates = input("Enter the next coordinate: ")
        commaPosition = coordinates.find(",")
        strLength = len(coordinates)
        if commaPosition == 1 and strLength == 3:
            xCoordinate = int(coordinates[0])
            yCoordinate = int(coordinates[2])
            xArray.append(xCoordinate)
            yArray.append(yCoordinate)
        elif commaPosition == 1 and strLength == 4:
            xCoordinate = int(coordinates[0])
            yCoordinate = int(coordinates[2:4])
            xArray.append(xCoordinate)
            yArray.append(yCoordinate)
        elif commaPosition == 2 and strLength == 5:
            xCoordinate = int(coordinates[0:2])
            yCoordinate = int(coordinates[3:5])
            xArray.append(xCoordinate)
            yArray.append(yCoordinate)
        elif commaPosition == 2 and strLength == 4:
            xCoordinate = int(coordinates[0:2])
            yCoordinate = int(coordinates[3])
            xArray.append(xCoordinate)
            yArray.append(yCoordinate)
    sXPoint = min(xArray) - 1
    sYPoint = min(yArray) - 1
    lXPoint = max(xArray) + 1
    lYPoint = max(yArray) + 1
    print(str(sXPoint) + "," + str(sYPoint))
    print(str(lXPoint) + "," + str(lYPoint))

findFrame()

