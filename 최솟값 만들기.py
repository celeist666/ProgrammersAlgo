# 정렬과 역정렬한 A,B를 곱해서 리턴한다.

def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
