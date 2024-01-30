N, K = map(int, input().split())
things = [[0,0]] + [list(map(int, input().split())) for _ in range(N)]

dp = [[0]* (K+1) for _ in range(N+1)]

for i in range(1, N + 1):
    for w in range(1, K+1):
        if things[i][0] <= w:
            dp[i][w] = max(things[i][1] + dp[i-1][w-things[i][0]], dp[i-1][w])
        else: 
            dp[i][w] = dp[i-1][w]


print(dp[-1][-1])
