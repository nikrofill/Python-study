sum1 = 0
for n in range(10,100,1):
    sum1 += n // 10 + n % 10
    print(n)
    print(sum1*3)
    sum1 = 0