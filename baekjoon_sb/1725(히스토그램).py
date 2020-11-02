import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

censor = defaultdict(lambda: 0)
areas = set()
before = 0
for block in range(N):

    height = int(input())
    censor[height] = 0
    
    for c in censor.keys():

        if c > height and censor[c]:
            print(censor[c] * c)
            areas.add(censor[c] * c)
            censor[before] += 2
            censor[c] = 0

        elif c < height:
            censor[c] += 1

    before = height
    print(censor)

areas = areas.union(set(censor[c] * c for c in censor.keys()))
print(areas)
