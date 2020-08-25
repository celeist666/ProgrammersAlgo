# bin 함수와 .count를 이용한 풀이
def nextBigNumber(n):
    c = bin(n).count('1')
    for m in range(n+1,1000001):
        if bin(m).count('1') == c:
            return m
