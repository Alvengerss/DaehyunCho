def solution(citations):
    
    for ref in range(len(citations), 0, -1):
        if ref <= len(list(filter(lambda x: x >= ref, citations))): return ref
        
    return 0
    
    
if __name__=="__main__":
    
    citations = [3, 0, 6, 1, 5]
    print(f'citations: {citations} | sol: {solution(citations)} | ans: 3')
    
    citations = [5, 5, 5, 5]
    print(f'citations: {citations} | sol: {solution(citations)} | ans: 4')
    
    citations = [31, 66]
    print(f'citations: {citations} | sol: {solution(citations)} | ans: 2')
    
    citations = [0, 1, 3, 5, 5, 5, 5, 5, 6]
    print(f'citations: {citations} | sol: {solution(citations)} | ans: 5')
