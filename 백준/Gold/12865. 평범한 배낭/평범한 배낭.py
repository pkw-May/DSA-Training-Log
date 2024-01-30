N, MaxWeight = map(int, input().split())
things = [[0,0]] + [list(map(int, input().split())) for _ in range(N)]

dp = [[0]* (MaxWeight+1) for _ in range(N+1)]

for index in range(1, N + 1):
    for weight in range(1, MaxWeight+1):
        if things[index][0] <= weight:
            dp[index][weight] = max(things[index][1] + dp[index-1][weight-things[index][0]], dp[index-1][weight])
        else: 
            dp[index][weight] = dp[index-1][weight]


print(dp[-1][-1])
