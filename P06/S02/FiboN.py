def fibon(y) :
    list1 = []
    fibo = []
    for x in range (0,20):
        if x >= 2:
            n = fibo[x-1] + fibo[x-2]
            fibo.append(n)
        else :
            list1.append(x)
            fibo.append(x)
    number = fibo[y]
    return number

print(fibon(5))
print(fibon(10))
print(fibon(15))