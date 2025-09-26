board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
def in_range(x,y):
    """
    주어진 좌표가 19x19 바둑판 범위 내에 있는지 확인
    Returns:
        bool: 범위 내에 있으면 True
    """
    return (0<=x and x<len(board)) and (0<=y and y<len(board))


def find_winner():
    """
    오목 게임의 승자를 찾는 함수
    모든 위치에서 8개의 방향으로 5개 연속된 같은 색 돌 탐색
    Returns:
	    tuple: (승자, 중앙x좌표, 중앙y좌표) or (None, None, None)
	    - 승자 : 1(흑) 또는 2(백)
    """
    
    #8개의 방향 : 시계방향으로 동쪽부터 시작
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
		
		#바둑판의 모든 위치 순회
    for i in range(len(board)):
        for j in range(len(board[0])):
		        #빈칸은 건너뛰기
            if board[i][j]==0:
                continue
            
            #현재위치(i,j)를 기점으로 8개의 방향으로 탐색
            for dx,dy in DIRECTIONS:
		            #5개 연속 발견시 승자, 중앙 돌 위치 리턴
		            #중앙 돌 위치 = 시작점에서 2칸 이동한 위치
		            #+1은 1-indexed로 변환한 것 (문제 요구사항)
                if isSeq5(i,j,dx,dy): 
                    return board[i][j], i+2*dx+1, j+2*dy+1
    
    #승자가 없는 경우
    return None,None,None

def isSeq5(start_x, start_y, dx, dy):
    """
    특정방향으로 5개 연속인지 확인
    Args:
	    start_x, start_y : 시작 위치의 좌표
	    dx, dy: 탐색중인 방향 벡터
    Returns:
	    bool: 5개 연속이면 True
    """
    #시작 위치의 돌 색상
    color = board[start_x][start_y]
    
    #시작점 포함 5개의 위치 확인
    for k in range(5):
        nx,ny = start_x+k*dx,start_y+k*dy
        #격자범위를 벗어나거나 다른색이면 연속이 아님
        if not in_range(nx,ny) or board[nx][ny]!=color: 
            return False
    
    return True

# ===== 메인 실행 부분 =====
# 승자 탐색
winner, x, y = find_winner()
# 결과 출력
if winner:
    print(winner) #1:흑돌 승 / 2:백돌 승
    print(x,y) #5개 연속 돌의 중앙 위치
else:
    print(0) #승부 미결정
						