for _ in range(int(input())):
    N = input()
    coinTypes = list(map(int, input().split()))
    totalValue = int(input())

    dp = [0] * (totalValue + 1)
    dp[0] = 1

    for coin in coinTypes:
        for value in range(1, totalValue+1):
            if value >= coin:

                dp[value] += dp[value-coin]

    print(dp[totalValue], end="\n")
