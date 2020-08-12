# for else를 이용하며 in을 사용해 있으면 선행스킬의 처음을 pop해 비교하여 풀이한다.

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
