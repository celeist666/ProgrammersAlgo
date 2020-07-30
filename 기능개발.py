import math

# 남은 일수를 체크하고 시작일보다 값이 높은 인덱스에
# 다다르면 그동안의 값을 리스트에 넣고 front값은 해당 인덱스로 갱신한ㄴ다
def solution(progresses, speeds):
    answer = []
    progresses = [math.ceil((100-a)/b) for a, b in zip(progresses, speeds)]
    front = 0
    for idx in range(len(progresses)):
        if progresses[front] < progresses[idx]:
            answer.append(idx-front)
            front = idx
    answer.append(len(progresses)-front)
    return answer
