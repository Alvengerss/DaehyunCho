class Stack:

    def __init__(self):

        self.stack = []

    def push(self, X):

        self.stack.append(X)

    def pop(self):

        return self.stack.pop(-1) if self.stack else -1

    def size(self):

        return len(self.stack)

    def empty(self):

        return 0 if self.stack else 1

    def top(self):

        return self.stack[-1] if self.stack else -1

if __name__=="__main__":

    N = int(input())

    stack = Stack()
    ops = {
        'push': stack.push,
        'pop': stack.pop,
        'size': stack.size,
        'empty': stack.empty,
        'top': stack.top
    }

    for i in range(N):

        operation = list(map(str, input().split()))
        
        if operation[0] == 'push':
            stack.push(int(operation[1]))

        else: print(ops[operation[0]]())

