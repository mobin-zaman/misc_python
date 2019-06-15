from collections import deque, defaultdict


def bfs_path_finder(graph, source, destination):
    q = deque()
    q.append(source)

    level = dict()

    level[source] = 0

    parent = dict()

    while q:
        u = q.popleft()

        for edges in graph[u]:
            if edges not in level.keys():
                level[edges] = level[u]+1
                parent[edges] = u
                q.append(edges)

    return path_finder(parent, source, destination)
    

    # bfs done, now find the path


def path_finder(parent, source, destination):
    path = list()

    def path_recurse(dest):
        if parent[dest] == source:
            path.append(dest)
            path.append(source)
            return path

        else:
            path.append(dest)
            return path_recurse(parent[dest])

    return path_recurse(destination)


print("input 99 99 to terminate")
graph = defaultdict(list)

while (1):
    x, y = map(int, input().split())
    if(x == 99 and y == 99):
        break

    graph[x].append(y)

print('path',bfs_path_finder(graph, 1, 5))
