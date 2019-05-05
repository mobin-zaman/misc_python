#
#
# def elephent_func(n):
#     if (n == 0):
#         return None
#     else:
#         elephent_func(n - 1)
#         array[n], array[n - 1] = array[n - 1], array[n]


n = int(input())
print(n,end=' ')
for i in range(1,n):
    print(i, end=' ')

