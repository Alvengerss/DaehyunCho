def solution(scoville, K):
    
    if min(scoville) >= K: return 0
    
    cnt = 0
    while min(scoville) < K:
        
        if len(scoville) > 1:

            least = min(scoville)
            scoville.remove(least)
            next_least = min(scoville)
            scoville.remove(next_least)
        
        scoville.append(least + 2*next_least)
        cnt += 1
        
        if len(scoville) == 1 and scoville[0] < K: return -1

    return cnt
    
if __name__=="__main__":

    scoville, K = [1, 2, 3, 9, 10, 12], 7
    print(f'scoville: {scoville} | K: {K} | sol: {solution(scoville, K)} | ans: 7')
