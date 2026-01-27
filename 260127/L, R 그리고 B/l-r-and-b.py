board = [list(input()) for _ in range(10)]

# Please write your code here.
## 요구사항 분석
# L에서 R을 피해 B로 가는 최단거리를 구하라
# 대각선 이동 불가능. 상하좌우로만 이동 가능.

## 로직 설정
# B의 위치, R의 위치, L의 위치를 구한다
# 맨하튼 거리를 사용한다

# R이 B와 L사이에 있고, B의 x좌표 == R의 x좌표 == L의 x좌표 
#또는 R이 B와 L사이에 있고, B의 y좌표 == R의 y좌표 == L의 y좌표
#위 상황일 경우 +2를 해준다

row_idx_b, colm_idx_b = -1,-1
row_idx_r, colm_idx_r = -1,-1
row_idx_l, colm_idx_l = -1,-1

for i in range(10):
    for j in range(10):
        if board[i][j]=="B":
            row_idx_b, colm_idx_b = i,j
        if board[i][j]=="R":
            row_idx_r, colm_idx_r = i,j
        if board[i][j]=="L":
            row_idx_l, colm_idx_l = i,j

dist = abs(row_idx_b-row_idx_l)+abs(colm_idx_b-colm_idx_l)-1

def colm_between_b_l():
    return colm_idx_b<colm_idx_r<colm_idx_l or colm_idx_l<colm_idx_r<colm_idx_b
def row_between_b_l():
    return row_idx_b<row_idx_r<row_idx_l or row_idx_l<row_idx_r<row_idx_b
    
if (colm_between_b_l() and row_idx_b==row_idx_r==row_idx_l) or (row_between_b_l() and colm_idx_b==colm_idx_r==colm_idx_l):
    dist+=2

print(dist)