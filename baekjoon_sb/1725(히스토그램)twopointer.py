import sys

input = sys.stdin.readline

N = int(input())
blocks = [int(input()) for _ in range(N)]

def histo(blocks):

    area = 0
    left, right = 0, len(blocks) - 1
    left_max, right_max = blocks[left], blocks[right]
    
    while left < right:

        left_max, right_max = max(blocks[left], left_max), max(blocks[right], right_max)

        if left_max <= right_max:

            area = max(area, (right - left + 1) * left_max)
            left += 1
            
        elif left_max > right_max:

            area = max(area, (right - left + 1) * right_max)
            right -= 1
            
    return area

print(histo(blocks))