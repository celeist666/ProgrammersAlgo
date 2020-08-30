# 앞에서 구한 값을 계속 사용해서 중복 계산을 피한다.

def solution(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a
