N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key = lambda x: (x[1], x[0]))

endPoint = 0
cnt = 0

for start, end in meetings:
    if start >= endPoint:
        endPoint = end
        cnt += 1

print(cnt)