def solution(s, n):
    def push(x):
        x = ord(x)
        if x == 32:
            return chr(x)
        
        elif 65 <= x <= 90:
            return chr(65 + (x+n-65) % 26)
        
        elif 97 <= x <= 122:
            return chr(97 + (x+n-97) % 26)
        
    answer = ''.join(map(push, s))
    return answer
    
if __name__=="__main__":

    s, n = "AB", 1
    print(f's: {s} | n: {n} | solution: {solution(s, n)} | ans: "BC"')
    
    s, n = "z", 1
    print(f's: {s} | n: {n} | solution: {solution(s, n)} | ans: "a"')
    
    s, n = "a B z", 1
    print(f's: {s} | n: {n} | solution: {solution(s, n)} | ans: "e F d"')
