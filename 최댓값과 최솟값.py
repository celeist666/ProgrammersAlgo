# 너무 쉬워서 생략

def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
