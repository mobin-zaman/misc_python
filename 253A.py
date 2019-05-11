import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n, m = map(int, input().split())
maximum, minimum = (max(n, m), min(n, m))
ans_string = ''

if n > m:
    max_character = "B"
    min_character = "G"

else:
    max_character = "G"
    min_character = "B"

for i in range(maximum):
    ans_string += max_character
    if minimum:
        ans_string += min_character
        minimum -= 1

print(ans_string)
