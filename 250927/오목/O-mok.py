board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
def in_range(x,y):
    return (0<=x and x<len(board)) and (0<=y and y<len(board))

# (0,0)(0,1)(0,2)
# (1,0)(1,1)(1,2)
# (2,0)(2,1)(2,2)
# 동: (1,1)->(1,2) i,j+1
# 동남: (1,1)->(2,2) i+1,j+1
# 남: (1,1)->(2,1) i+1,j
# 남서: (1,1)->(2,0) i+1,j-1
# 서: (1,1)->(1,0) i,j-1
# 서북: (1,1)->(0,0) i-1,j-1
# 북: (1,1)->(0,1) i-1,j
# 북동: (1,1)->(0,2) i-1,j+1
dxs, dys = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]

#모든 좌표에서 다 확인해보자
for i in range(len(board)):
		for j in range(len(board[0]):
				if board[i][j] == 0:
						continue
				
				for dx,dy in zip(dxs,dys):
				    # 각 반복에서:
					  # 1번째: dx=0,  dy=1   (→ 방향) 
				    # 2번째: dx=1,  dy=-1  (↙ 방향)
				    # 3번째: dx=1,  dy=0   (↓ 방향)
				    # 4번째: dx=1,  dy=1   (↘ 방향)
				    # 5번째: dx=-1, dy=-1  (↖ 방향)
				    # 6번째: dx=-1, dy=0   (↑ 방향)
				    # 7번째: dx=-1, dy=1   (↗ 방향)
				    # 8번째: dx=0,  dy=-1  (← 방향)
				    
				    #방향 하나 정해졌으면
				    #5번 연속인지 검사한다
				    isSeq=True
						curr_x, curr_y = i, j
						for _ in range(5): 
								nx,ny = curr_x+dx,curr_y+dy
								if not in_range(nx,ny) or board[nx][ny]==board[i][j]: #범위밖 or 연속x라면 검사종료
										isSeq=False
										break
								curr_x,curr_y = nx,ny #계속검사
						
						# 연속x -> 다음 방향으로 검사한다
						# 연속o -> 루프종료
						if isSeq==True:
								print(board[i][j]) #승자출력
								print(i+2*dx+1, j+2*dy+1) #가운데 x,y출력
								sys.exit()

print(0)