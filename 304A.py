from math import sqrt

n = int(input())

count = 0
for i in range(1, n):
    for j in range(i+1, n):
        x =  sqrt((i**2)+(j**2))
        if x > n:
            break
        if int(x) == x:
            count += 1

print(count)
