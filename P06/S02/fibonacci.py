list1 = []
fibo = []
for x in range (0,11):

    if x >= 2:
         n = fibo[x-1] + fibo[x-2]
         fibo.append(n)
    else :
        list1.append(x)
        fibo.append(x)

print (fibo)


