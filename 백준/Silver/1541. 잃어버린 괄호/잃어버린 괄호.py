exp = input()
numsToSub = []
result = 0

for nums in exp.split('-'):
    temp = 0

    for posNum in nums.split('+'):
        temp += int(posNum)

    numsToSub.append(temp)

result = numsToSub[0]

for num in numsToSub[1:]:
    result -= num

print(result)