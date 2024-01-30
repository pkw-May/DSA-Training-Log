N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N
biggest = arr[0]

for i in range(1, N):
    if (arr[i] > arr[i-1]) & (arr[i] > biggest):
        biggest = arr[i]
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]

print(dp[-1])
