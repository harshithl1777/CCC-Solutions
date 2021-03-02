def voronoi():
    villNum = int(input())
    villages =[]
    for x in range(villNum):
        villHold = int(input())
        villages.append(villHold)
    villages.sort()
    count = -1
    lens = []
    for y in villages:
        count = count + 1
        if (count == 0 or count+1 == len(villages)):
            pass
        else:
            lenHold = ((y - villages[count-1]) / 2) + ((villages[count+1] - y) / 2)
            lens.append(lenHold)
    lens.sort()
    print(lens[0])
            

voronoi()