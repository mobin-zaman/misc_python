n = int(input())
a = 0
while 4*a <= n:
    r = n - 4 * a
    if r % 7 == 0:
        print('4'*a, end='')
        print('7'*(int(r/7)))
        exit()
    a += 1

print(-1)
