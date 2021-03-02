# Name - Harshith Latchupatula
# Date - September 15, 2020
# Language - Python 3.8
# Contest Completed - Yes

def arrivalTime():
    startTimeStr = input('Enter: ')
    if int(startTimeStr[0]) == 0:
        startTime = startTimeStr[1] + startTimeStr[3] + startTimeStr[4]
    elif int(startTimeStr[0]) > 0:
        startTime = int(startTimeStr[0] + startTimeStr[1] + startTimeStr[3] + startTimeStr[4])
    findTime(int(startTime))

def findTime(startTime):
    if 1000 <= startTime <= 1300 or 1900 <= startTime <= 2340 or 000 <= startTime <= 500:
        endTime = startTime + 200
        if endTime == 2420:
            print('00:20')
        elif endTime == 2440:
            print('00:40')
        elif endTime > 2400:
            endTime = endTime - 2400
            printer(endTime)
        elif endTime == 2400:
            print('00:00')
        else:
            printer(endTime)
    elif 520 <= startTime <= 940:
        times = {520: 740, 540: 820, 600: 900, 620: 940, 640: 1010, 700: 1030, 720: 1040, 740: 1050, 800: 1100, 820: 1110, 840: 1120, 900: 1130, 920: 1140, 940: 1150}
        endTime = times[startTime]
        printer(endTime)
    elif 1320 <= startTime <= 640:
        times2 = {1320: 1540, 1340: 1620, 1400: 1700, 1420: 1740, 1440: 1820, 1500: 1900, 1520: 1910, 1540: 1920, 1600: 1930, 1620: 1940, 1640: 1950, 1700: 2000, 1720: 2010, 1740: 2020, 1800: 2030, 1820: 2040, 1840: 2050}
        endTime = times2[startTime]
        printer(endTime)

def printer(time):
    time2 = str(time)
    if len(time2) == 3:
        output = '0' + time2[0] + ':' + time2[1] + time2[2]
    elif len(time2) == 4:
        output = time2[0] + time2[1] + ':' + time2[2] + time2[3]
    print(output)

arrivalTime()