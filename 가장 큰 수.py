# 1000이하니까 3자리라고 치고 스트링을 3배로 늘린 뒤 이를 sorting하면 사전순으로 정렬되기에
# 원하는 순서대로 정렬이 된다. 

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
