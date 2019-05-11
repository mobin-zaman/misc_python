n = int(input())
w = input().split()

share = {}

for weight in w:
    if weight == "200":
        share[200] += 1

    else:
        share[100] += 1

if share[200]==(2*share[100]):
    print("YES")
else:





