import collections

# 자료들의 개수를 세어 dictionary 형태로 반환하는 Counter함수 사용
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
