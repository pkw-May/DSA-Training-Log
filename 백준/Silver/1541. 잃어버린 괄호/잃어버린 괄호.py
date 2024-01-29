posList = input().split('-')
nums = []

for pos in posList:
    temp = 0
    for num in pos.split('+'):
        temp += int(num)
    nums.append(temp)

result = nums[0]
for i in range(1, len(nums)):
    result -= nums[i]

print(result)