# 해당 행의 이전 행의 원소들 중 같은 열에 있지 않은 원소를 각각 행에 더해주는 식으로 쭉쭉 내려가면 된다.
def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])
