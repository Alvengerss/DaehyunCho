N = int(input())

flags = []
for line in range(N):

    sentence = input()
    stack = []

    if len(sentence) % 2 == 0:

        for x in sentence:

            if not stack: stack.append(x)

            else:
                if stack[-1] == x:
                    stack.pop(-1)

                else: stack.append(x)

        flags.append(not stack)

    else: pass

print(sum(flags))
