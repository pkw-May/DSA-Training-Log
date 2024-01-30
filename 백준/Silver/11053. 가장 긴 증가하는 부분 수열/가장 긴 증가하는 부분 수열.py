N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N

# 본인은 고정해놓은 상태로, 앞선 모든 원소에 대하여 
for i in range(1, N):
    for j in range(0, i):
        if arr[i] > arr[j]:
            # 너까지 도달하는 데 수열이 쌓인게 더 크면, 너를 포함해서 횟수를 더하고
            # 너를 포함해봤자 내가 더 긴 수열을 만든다면, 그냥 가만히 있고
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))