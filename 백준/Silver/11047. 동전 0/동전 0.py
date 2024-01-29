N, K = map(int, input().split())
coins = sorted(map(int, (input() for _ in range(N))), reverse=True)

count = 0 

for coin in coins:
    if K >= coin:
        count += K // coin
        K = K % coin

    elif K <= 0:
        break

print(count)