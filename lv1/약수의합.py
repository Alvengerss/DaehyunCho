def solution(n):
    return sum(filter(lambda x: not n % x, [_ for _ in range(1, n+1)]))

if __name__=="__main__":
    print(f'Input: {12} | MyAns: {solution(12)} | Ans: {28}')
    print(f'Input: {5} | MyAns: {solution(5)} | Ans: {6}')
