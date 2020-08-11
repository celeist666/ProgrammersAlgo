# red부분의 제곱근값 이하이므로 이를 완전 탐색해서 red의 가로세로를 알아낸다.
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
