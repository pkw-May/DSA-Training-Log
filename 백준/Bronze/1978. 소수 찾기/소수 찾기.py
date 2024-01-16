n = int(input())
nums = list(map(int, input().split()))
count = 0

for num in nums:
    if num > 1 :
        cnt = 0
        for i in range(2, num+1):
            if num % i == 0:
                cnt += 1
            
        if cnt == 1:
            count += 1

print(count)

