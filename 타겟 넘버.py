# 재귀를 이용해 각각의 자식에 numbers의 첫 요소를 target에서 빼거나 더한 값을 넣어준다.

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
