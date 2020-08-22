# 문제를 각각 2x2 정사각형 비교로 축소시켜 푼다.
# 각 칸에 칸으로부터 왼쪽, 왼쪽위, 위 중의 최소값의 +1을 더해 전체 값의 max를 찾는다. 

def solution(board):
    width = len(board[0])
    height = len(board)
    for x in range(1,height):
        for y in range(1,width):
                if board[x][y] == 1:
                        board[x][y] = min(board[x-1][y-1], board[x-1][y], board[x][y-1]) + 1
    return max([item for row in board for item in row])**2
