N, M = map(int, input().split())
graph = [input().split()[0] for _ in range(N)]

def horizon(line):
    isH = False

    for i in range(M):
        if line[i] == '-':
            if not isH:
                global cnt
                cnt += 1
            isH = True
        else:
            isH = False

def vertical(index):
    isV = False

    for nth in range(N):
        if graph[nth][index] == '|':
            if not isV:
                global cnt
                cnt += 1
            isV = True
        else:
            isV = False

cnt = 0

for n in range(N):
    horizon(graph[n])

for m in range(M):
    vertical(m)

print(cnt)