num = input()

hexList = {"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}

if(num[0]=="0"):
    if (num[1]=="x"):
        #16진수
        result = 0
        i = 0

        for n in num[:1:-1]:
            if(n.isalpha()):       
                n = hexList[n]
            result += int(n)*(16**i)
            i += 1

        num = result

    else:
        #8진수
        result = 0
        i = 0

        for n in num[:0:-1]:
            result += int(n)*(8**i)
            i += 1

        num = result


print(int(num))
