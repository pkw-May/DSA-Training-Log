N = int(input())
nums = list(map(lambda x: int(x), input().strip()))

result = 0
for i in range(0, N):
    result += nums[i]

print(result)

