# 자기보다 작은 홀수로 나누어 떨어지는 값의 갯수가 문제의 답
def solution(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])
