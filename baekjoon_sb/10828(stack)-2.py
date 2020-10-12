import sys

input = sys.stdin.readline

push = lambda lst, x: lst.append(x)
pop = lambda lst: lst.pop(-1) if lst else -1
size = lambda lst: len(lst)
empty = lambda lst: 0 if lst else 1
top = lambda lst: lst[-1] if lst else -1

if __name__=="__main__":

    N = int(input())

    ops = {
        'pop': pop,
        'size': size,
        'empty': empty,
        'top': top
    }

    stack = []
    for i in range(N):
        
        operation = list(map(str, input().split()))
        
        if operation[0] == 'push':
            push(stack, operation[1])

        else: print(ops[operation[0]](stack))
