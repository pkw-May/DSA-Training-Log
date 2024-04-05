import math

def main():
    N = int(input())

    if N==1:
        return

    for num in range(2, int(math.sqrt(N)) + 1):
        while(N%num==0):
            print(num)
            N //= num
    
    if N>1:
        print(N)
        
main()