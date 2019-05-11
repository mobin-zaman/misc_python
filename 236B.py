a, b, c = map(int, input().split())

max_number = 100 * 100 * 100
d=[0]*(max_number+1)
for i in range(1, (max_number+1)):
    j = i
    while j <= max_number:
        d[j] += 1
        j += i

count = 0
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            count += d[i * j * k]

print(count % 1073741824)
