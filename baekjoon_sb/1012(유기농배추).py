T = int(input())

def adjacent(pos, N, M):

    x, y = pos
    left = (x-1, y) if x-1 >= 0 else None
    right = (x+1, y) if x+1 < M else None

    up = (x, y-1) if y-1 >= 0 else None
    down = (x, y+1) if y+1 < N else None

    return list(filter(lambda x: x, (left, right, up, down)))

for case in range(T):

    N, M, nums = map(int, input().split())
    grid = dict()
    for cabbage in range(nums):

        grid[tuple(map(int, input().split()))] = []

    src = grid[0]
    dsts = list(filter(lambda x: x in grid, adjacent(grid[0], N, M)))
    print(dsts)




if __name__=="__main__":

    a = {(2, 3): 1}
    b = {v: k for k, v in a.items()}
    print(b)

        
    

    