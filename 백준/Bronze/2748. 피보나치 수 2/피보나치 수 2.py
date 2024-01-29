n = int(input())

dp = [0] * (n+1)


def fibo(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        dp[x] = 1
        return dp[x]
    elif dp[x] != 0:
        return dp[x]
    else:
        dp[x] = fibo(x-2) + fibo(x-1)
        return dp[x]


print(fibo(n))