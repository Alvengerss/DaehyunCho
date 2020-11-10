import sys
from collections import defaultdict

#input = sys.stdin.readline

N = int(input())

censor = defaultdict(lambda: 0)
areas = []
debug = []
for block in range(N):

    block = int(input())

    if censor.get(block):

        if censor[block] == 0:
            censor[block] += 1
        
    else:
        censor[block] = 1

    for c in censor:

        if c > block and censor[c]:

            areas.append(c * censor[c])
            debug.append([block, c, censor[c]])
            censor[c] = 0
        
# print(areas)
print(debug)