board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
def in_range(x,y):
    return (0<=x and x<len(board)) and (0<=y and y<len(board))


def find_winner():
    """
    오목 게임의 승자를 찾는 함수
    Returns:
            tuple: (승자, 중앙x좌표, 중앙y좌표) or (None, None, None)
    """
    DIRECTIONS = [
        # (0,0)(0,1)(0,2)
        # (1,0)(1,1)(1,2)
        # (2,0)(2,1)(2,2)
        (0,1), #동
        (1,1), #남동
        (1,0), #남
        (1,-1), #남서
        (0,-1), #서
        (-1,-1), #북서
        (-1,0), #북
        (-1,1)  #북동
    ]
		
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                continue
                
            for dx,dy in DIRECTIONS: #각 방향별로
                if isSeq5(i,j,dx,dy): #5개 연속인지 확인
                    return board[i][j], i+2*dx+1, j+2*dy+1
    
    return None,None,None

def isSeq5(i,j,dx,dy):
    """
    특정방향으로 5개 연속인지 확인
    """
    color = board[i][j]
    
    for k in range(5):
        nx,ny = i+k*dx,j+k*dy
        if not in_range(nx,ny) or board[nx][ny]!=color: #격자범위를 벗어나거나 color와 다르면
            return False
    
    return True

winner, x, y = find_winner()
if winner:
    print(winner)
    print(x,y)
else:
    print(0)
						