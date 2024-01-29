N, K = map(int, input().split())
coins = list(map(int, (input() for _ in range(N))))
coins.reverse()

count = 0 

for coin in coins:
    if K >= coin:
        count += K // coin
        K = K % coin

    elif K <= 0:
        break

print(count)