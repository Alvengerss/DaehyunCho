def solution(s):        
    answer = ''
    for word in s.split():
        print(word)
        answer += ''.join(_.upper() if not i % 2 else _.lower() for i, _ in enumerate(word)) + ' '
    
    return answer[:-1]
    
if __name__=="__main__":

  s = "try hello world"
  print("s: {s} | sol: {solution(s)} | ans: "TrY HeLlO WoRlD")
