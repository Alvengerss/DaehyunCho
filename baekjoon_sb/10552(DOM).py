import sys

input = sys.stdin.readline

N, M, src = map(int, input().split())

graphs = dict()
for pensioner in range(N):

    good, hate = map(int, input().split())
    if hate in graphs:
        pass

    else:
        graphs[hate] = good

visited = []
cnt = 0
while True:

    if not graphs.get(src):
        # print(len(visited))
        print(cnt)
        break

    dst = graphs[src]
    if dst not in visited:
        cnt += 1
        visited.append(dst)

    else:
        print(-1)
        break

    src = dst