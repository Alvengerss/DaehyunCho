def solution(numbers):
    answer = set()
    for i, num in enumerate(numbers):
        answer = answer.union(list(map(lambda x: x+num, numbers[i+1:])))
    return sorted(list(answer))
    
if __name__=="__main__":
  numbers = [2, 1, 3, 4, 1]
  print(f'Given: {numbers} | Sol:{solution(numbers)} | Ans: [2, 3, 4, 5, 6, 7]')
  
  numbers = [5, 0, 2, 7]
  print(f'Given: {numbers} | Sol:{solution(numbers)} | Ans: [2, 5, 7, 9, 12]')
