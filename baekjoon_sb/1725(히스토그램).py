import sys

input = sys.stdin.readline

N = int(input())

censor = dict()
area = 1
for block in range(N):

    height = int(input())
    
    for c in list(filter(lambda x: x > height, censor.keys())):
        area = max(area, censor[c] * c)
        del censor[c]

    for h in range(1, height+1):

        if censor.get(h):
            censor[h] += 1

        else:
            censor[h] = 1

print(max([k*v for k, v in censor.items()] + [area]))
