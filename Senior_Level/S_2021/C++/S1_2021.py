def getData():
    iterNum = int(input())
    fenceH = input().split()
    widths = input().split()
    totalArea = 0
    for x in range(iterNum):
        areaHold = (int(widths[x])*(int(fenceH[x]) + int(fenceH[x+1]))) / 2
        totalArea = totalArea + areaHold
    print(totalArea)

getData()