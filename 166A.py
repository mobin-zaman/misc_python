n, k = map(int, input().split())
team_list = list()
team_map = dict()

for i in range(n):
    team = tuple(map(int, input().split()))

    if team in team_map:
        team_map[team] += 1

    else:
        team_map[team] = 1

    team_list.append(team)

team_list.sort(key=lambda x: (-x[0], x[1]))
print(team_map[team_list[k-1]])

