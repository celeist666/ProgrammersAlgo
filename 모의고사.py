from itertools import cycle

# 반복가능한 객체를 패턴으로삼아 무한히 다음 숫자를 반환해주는 cycle함수

def solution(answers):
    winner = []
    pattern_supo_1 = [1 ,2, 3, 4, 5]
    pattern_supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score_supo = [0, 0, 0]

    for supo_1, supo_2, supo_3, answer in zip(cycle(pattern_supo_1), cycle(pattern_supo_2), cycle(pattern_supo_3), answers):
        if supo_1 == answer: score_supo[0] += 1
        if supo_2 == answer: score_supo[1] += 1
        if supo_3 == answer: score_supo[2] += 1

    for i, score in enumerate(score_supo):
        if score == max(score_supo):
            winner.append(i+1)

    return winner
