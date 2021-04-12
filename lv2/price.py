def solution(prices):
    
    answer = []
    
    for i in range(len(prices) - 1):
        
        cnt = 0
        left, right = i, i + 1
        
        while True:
            
            # price go down
            
            if prices[left] > prices[right]:
                cnt += 1
                break
                
            # if price didn't go down
            else:

                # add +1 to flag
                cnt += 1
                
                # move right pointer
                right += 1
                if right == len(prices):
                    break

        answer.append(cnt)
            
    answer.append(0)
    return answer
  
if __name__=="__main__":
  
  prices = [1, 2, 3, 2, 3]
  print(solution(prices))
