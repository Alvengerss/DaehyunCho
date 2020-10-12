import sys

#input = sys.stdin.readline

def stack(lst, x):
    
    if x == '(':
        return lst + [x]
    
    if lst == [] and x == ')':
        return -1
    
    else:
        return lst[:-1]
    
N = int(input())
for i in range(N):
    
    seq = input()
    ans = []
    for x in seq:
        ans = stack(ans, x)
        if ans == -1: break
    
    if ans == []:
        print("YES")
        
    else:
        print("NO")