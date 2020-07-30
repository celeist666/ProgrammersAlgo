def solution(n):
    answer = ''
    while n > 0:
        n -= 1 # 숫자가 0부터 시작할 수 있게 하려고
        answer = '124'[n%3] + answer
        n //= 3
    return answer

# 3진법을 사용한다. 하지만 3진법을 쓰면 0,1,2가 나오기에 각 값을 매핑해준다.
