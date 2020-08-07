# 앞에서부터 비교해서 다음 수가 더 크면 해당 자리의 수를 지운다.
# 다음 숫자가 더 크면 스택에서 빼주는 식
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop() 
        stack.append(num)
    if k != 0: # 뺄만큼 뺐는데도 감소시켜야하는 횟수가 남아있을경우 뒤를 자른다.
        stack = stack[:-k]
    return ''.join(stack)
