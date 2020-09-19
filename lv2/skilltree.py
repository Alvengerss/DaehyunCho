def solution(skill, skill_trees):
    
    answer = 0
    candidates = list(map(lambda i: skill[:i+1], range(len(skill))))

    for tree in skill_trees:
        check_list = ''.join(list(filter(lambda x: x in skill, tree)))
        if check_list in candidates: answer += 1
        elif check_list == '': answer += 1
    
    return answer
    
if __name__=="__main__":

    skill, skill_trees = "CBD", ["BACDE", "CBADF", "AECB", "BDA"]
    print(f'skill: {skill} | skill_trees: {skill_trees} | sol: solution(skill, skill_trees)} | ans: 2')
    
    skill, skill_trees = "CBD", ["BACDE", "CBADF", "AECB", "BDA", "AQWER"]
    print(f'skill: {skill} | skill_trees: {skill_trees} | sol: solution(skill, skill_trees)} | ans: 2')
