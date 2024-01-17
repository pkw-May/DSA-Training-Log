treeCnt, aimLen = map(int, input().split())
treeHeights = list(map(int, input().split()))

shortCutter = 0
longCutter = max(treeHeights)

while shortCutter <= longCutter:
    midCutter = (shortCutter + longCutter) // 2

    expectedLen = 0
    for tree in treeHeights:
        if tree >= midCutter:
            expectedLen += tree - midCutter
    
    if expectedLen >= aimLen:
        shortCutter = midCutter + 1

    else:
        longCutter = midCutter - 1
    
print(longCutter)