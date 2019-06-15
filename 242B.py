n = int(input())

x_list=[]
y_list=[]
dictionary = {}

for i in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
    dictionary[(x, y)] = i + 1

x_list.sort()
y_list.sort(reverse=True)

if (x_list[0],y_list[0]) in dictionary.keys():
    print(dictionary[x_list[0],y_list[0]])
else:
    print(-1)


