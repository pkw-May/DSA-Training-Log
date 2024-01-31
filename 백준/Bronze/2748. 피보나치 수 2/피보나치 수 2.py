n = int(input())

fibTable = [0, 1]

for i in range(2, n+1):
    fibTable.append(fibTable[i-2] + fibTable[i-1])

print(fibTable[n])