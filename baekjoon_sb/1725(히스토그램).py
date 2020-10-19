import sys

#input = sys.stdin.readline

N = int(input())

best_area = 1
censor = None
cnt = 1
for block in range(N):

    height = int(input())
    if not censor:
        censor = height

    else:
        if censor <= height:
            cnt += 1
            best_area = max(best_area, censor * cnt)

        else:
            censor = height

    print("censor:" , censor)
print(best_area)


            


    