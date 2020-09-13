def solution(s):
    div = len(s) % 2
    return s[len(s)//2] if div else s[len(s)//2-1:len(s)//2+1]
    
  if __name__=="__main__":
    print("abcde", solution("abcde"), sep=": ")
    print("qwer", solution("qwer"), sep=": ")
    
