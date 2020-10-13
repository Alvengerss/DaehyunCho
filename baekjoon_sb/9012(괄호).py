import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    
    seq = input()
    ans = 0
    for x in seq:
        ans = ans + 1 if x == '(' else ans - 1
        if ans < 0: break
        
    print(f'{"YES" if ans == 0 else "NO"}')