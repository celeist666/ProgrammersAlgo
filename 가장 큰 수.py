def solution1(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[len(stack) -1]]:
            temp = stack.pop()
            answer[temp] = i - temp
        stack.append(i)
    while len(stack):
        temp = stack.pop()
        answer[temp] = len(prices) - temp - 1

    return answer
