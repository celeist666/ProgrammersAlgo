# 최대공배수 만큼의 같은 패턴이 생기고 각 패턴마다 하나씩 겹치기에 w+h-gcd 만큼의 종이를 못 사용하게 된다.

import math
def solution(w,h): 
    return w*h - (w+h-math.gcd(w,h))
