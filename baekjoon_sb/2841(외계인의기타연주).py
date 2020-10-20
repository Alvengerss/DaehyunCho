import sys

input = sys.stdin.readline

N, P = map(int, input().split())

stack = dict()
mvmnts = 0
for _ in range(N):

    line, flat = map(int, input().split())

    # if there is a finger on that line
    if stack.get(line):

        # already pressed
        if stack[line][-1] == flat:

            pass

        # press
        elif stack[line][-1] < flat:

            stack[line].append(flat)
            mvmnts += 1

        # when both fails(last flat lower than the current one)
        else:

            # we pop out lower flats
            # possibility to get empty
            while stack[line]:

                if stack[line][-1] > flat:

                    # release
                    stack[line].pop(-1)
                    mvmnts += 1

                else:

                    if stack[line][-1] == flat:
                        break

                    elif stack[line][-1] < flat:

                        # press
                        stack[line].append(flat)
                        mvmnts += 1
                        break

            # if flat empty
            if not stack[line]:
                stack[line].append(flat)
                mvmnts += 1

    # initial press on that line
    else:
        # press
        stack[line] = [flat]
        mvmnts += 1

print(mvmnts)