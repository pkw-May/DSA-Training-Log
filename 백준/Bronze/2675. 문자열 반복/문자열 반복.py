n = int(input())

for _ in range(n):
    cnt, word = input().split()
    
    result = ''
    
    for x in word:
        result += x*int(cnt)
        
    print(result)