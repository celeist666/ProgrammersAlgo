# 역순으로 뒤집어서 각 수에 순번을 매기고 그 순번과 값의 min값들 중에 max값이 H-index이다
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
