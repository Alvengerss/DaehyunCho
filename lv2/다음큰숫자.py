def to_binary(n):

    conv = ''
    while True:
        conv += str(int(n%2))
        n = int(n / 2)
        if n < 1: return conv[::-1]
        
        
def solution(n):
    
    ref = to_binary(n).count('1')
    
    while True:
        n += 1
        if to_binary(n).count('1') == ref: return n
        
        
if __name__=="__main__":

    n = 78
    print(f'n: {n} | sol: {solution(n)} | ans: 83')
    
    n = 15
    print(f'n: {n} | sol: {solution(n)} | ans: 23')
