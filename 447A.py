p, n = map(int, input().split())
hash_table = [-1] * p

flag = True
for i in range(n):

    x = int(input())

    hx = x % p

    if hash_table[hx] == -1:
        hash_table[hx] = x

    else:
        print(i+1)
        flag = False
        break

if(flag):
    print(-1)
