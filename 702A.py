n = int(input())
l = input()
array = list(map(int, l.split(' ')))

max_count = 1
j = 0
count = 1

for i in range(n-1):
    if array[i] < array[i+1]:
        count += 1
        if (count > max_count):
            max_count = count
    else:
        count = 1
        continue


print(max_count)
