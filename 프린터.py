# l을 증감하면서 답이 되는 값의 위치를 계속 추적하고 pop할 때마다
# 인쇄횟수를 증가시키고 이때 위치가 0이면 종료시킨다.

def solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans
