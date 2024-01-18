x = input()
origin = x
cnt = 0

def addCycle(x):
    y = str(x[-1])

    if len(str(x)) < 2:
        x = '0' + str(x)
    
    x = str(int(x[0]) + int(x[1]))

    x = y + str(x[-1])

    if int(origin) != int(x):
        global cnt
        cnt += 1
        addCycle(x)
    
    else:
        cnt += 1
        print(cnt)
    
addCycle(x)