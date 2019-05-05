from math import sqrt


def move(z, x, y):
    if z == 'E':
        return x + 1, y
    elif z == 'S':
        return x, y - 1
    elif z == 'W':
        return x - 1, y
    elif z == 'N':
        return x, y + 1


distance = lambda x, y, a, b: sqrt(((x - a) ** 2) + ((y - b) ** 2))

t, sx, sy, ex, ey = map(int, input().split())
base_distance = distance(sx, sy, ex, ey)

wind_direction = input()

count = 0

"""no need of distance at all :/"""
for d in wind_direction:
    count += 1
    test_x, test_y = move(d, sx, sy)
    new_distance = distance(test_x, test_y, ex, ey)
    if new_distance < base_distance:
        sx, sy = test_x, test_y
        base_distance = new_distance
        if (sx == ex and sy == ey):
            print(count)
            exit()

print(-1)
