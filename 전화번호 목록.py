# 문자열을 정리해두면 접두사인 번호가 앞에 나오고 그 바로 뒤에 해당 번호를 접두사로 두는 번호가
# 나온다. 그렇기에 n번씩만 비교하면된다.

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
