def solution(numbers, hand):
    
    keypad = {i+1: (i//3, i%3) for i in range(0, 9)}
    keypad[0] = (3, 1)
    keypad['*'] = (3, 0)
    keypad['#'] = (3, 2)

    def distance(x, y):
        return sum(abs(p1-p2) for p1, p2 in zip(keypad[x], keypad[y]))
    
    answer = ''
    left_num, right_num = [1, 4, 7], [3, 6, 9]
    left_pos, right_pos = '*', '#'
    for num in numbers:
        if num in left_num:
            left_pos = num
            answer += 'L'
            
        elif num in right_num:
            right_pos = num
            answer += 'R'
            
        else:
            if distance(left_pos, num) < distance(right_pos, num):
                left_pos = num
                answer += 'L'
                
            elif distance(left_pos, num) > distance(right_pos, num):
                right_pos = num
                answer += 'R'
                
            else:
                if hand == 'right':
                    right_pos = num
                    answer += 'R'
                elif hand == 'left':
                    left_pos = num
                    answer += 'L'
    
    return answer
    
if __name__=="__main__":
    numbers, hand = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"
    print(f'numbers: {numbers} | hand: {hand} | sol: {solution(numbers, hand)} | ans: "LRLLLRLLRRL"')
    
    numbers, hand = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"
    print(f'numbers: {numbers} | hand: {hand} | sol: {solution(numbers, hand)} | ans: "LRLLRRLLLRR"')
    
    numbers, hand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"
    print(f'numbers: {numbers} | hand: {hand} | sol: {solution(numbers, hand)} | ans: "LLRLLRLLRL"')
