def solution(n):
    return sum(filter(lambda x: not n % x, [_ for _ in range(1, n+1)]))
