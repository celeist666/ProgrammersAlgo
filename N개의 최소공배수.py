from fractions import gcd

def nlcm(num):
    answer = num[0]
    for n in num: 
        answer = n * answer / gcd(n, answer)

    return answer
