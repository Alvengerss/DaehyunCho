N = int(input())
formula = input()

operators = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y, 
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y}

operands = dict()
stack = []

for op in formula:

    if op in operators:
        y, x = stack.pop(), stack.pop()
        stack.append(operators[op](x, y))

    else:
        if op not in operands:
            operands[op] = int(input())
        stack.append(operands[op])

print(stack[0])