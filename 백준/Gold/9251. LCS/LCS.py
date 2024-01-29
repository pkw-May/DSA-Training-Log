X = '0' + input().strip()
Y = '0' + input().strip()

dp = [[0] * (len(Y)) for _ in range(len(X))]

for i in range(1, len(X)):
    for j in range(1, len(Y)):
        if X[i] == Y[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])


print(dp[-1][-1])
