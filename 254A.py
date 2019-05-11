import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
n = int(input())

pair = {}

inp = input().split()
i = 0
for ip in inp:
    i += 1
    if ip not in pair:
        pair[ip] = list()
    pair[ip].append(i)

if any(len(p) % 2 != 0 for p in pair.values()):
    print(-1)
else:
    for p in pair.values():
        i = 0
        while i < len(p) - 1:
            print(p[i], p[i + 1])
            i+=2
