def getData():
    rows = int(input())
    col = int(input())
    itNum = int(input())
    choices = []
    for a in range(itNum):
        strHold = input()
        singleChoiceArr = strHold.split()
        choices.append(singleChoiceArr[0]+singleChoiceArr[1])
    matrix = creator(rows, col)
    painted = computer(matrix, choices, rows, col)
    counter(painted)

def creator(rw, cl):
    mat = []
    for b in range(rw):
        rowHold = []
        for c in range(cl):
            rowHold.append('B')
        mat.append(rowHold)
    return mat

def computer(tab, moves, r, c):
    for d in moves:
        action = d[0]
        val = int(d[1:]) - 1
        if (action == 'R'):
            count = -1
            for e in tab[val]:
                count = count + 1
                if (e == 'B'):
                    tab[val][count] = 'G'
                elif (e == 'G'):
                    tab[val][count] = 'B'
        elif (action == 'C'):
            countC = -1
            val = int(d[1:]) - 1
            for f in tab:
                countC = countC + 1
                if f[val] == 'B':
                    tab[countC][val] = 'G'
                elif f[val] == 'G':
                    tab[countC][val] = 'B'
    return tab

def counter(pTable):
    totalG = 0
    for g in pTable:
        totalG = totalG + g.count('G')
    print(totalG)


getData()
