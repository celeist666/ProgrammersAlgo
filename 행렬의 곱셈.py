# zip이 행과 열을 변환해주는 역할

def soltuion(A, B):  
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
