X = '0'+input()
Y = '0'+input()

dp = [[0]*len(X) for _ in range(len(Y))]

for i in range(1, len(Y)):
    for j in range(1, len(X)):
        if X[j] == Y[i]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])