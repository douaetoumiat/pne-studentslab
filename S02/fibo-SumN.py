def fibosum(y):
    list1 = []
    fibo = []
    sum = 0
    for x in range (0,20):
        if x >= 2:
            n = fibo[x-1] + fibo[x-2]
            fibo.append(n)
        else :
            list1.append(x)
            fibo.append(x)
    for c in range (0,y+1):
        sum += fibo[c]
    return sum
print(fibosum(5))
print(fibosum(10))