board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
def in_range(x,y):
    return (0<=x and x<len(board)) and (0<=y and y<len(board))

#가로로 5번 연속됨 확인
#한번이라도 아니라면 False
#모두 다 통과했다면 True
def isHSeq(i,j):
    for k in range(5):
        if not in_range(i,j+k) or board[i][j+k]!=board[i][j]:
            return False
    return True

#세로로 5번 연속됨 확인
#한번이라도 아니라면 False
#모두 다 통과했다면 True
def isVSeq(i,j):
    for k in range(5):
        if not in_range(i+k,j) or board[i+k][j]!=board[i][j]:
            return False
    return True

#하향 대각선 방향으로 5번 연속됨 확인
#한번이라도 아니라면 False
#모두 다 통과했다면 True
def isDiagDownSeq(i,j):
    for k in range(5):
        if not in_range(i+k,j+k) or board[i+k][j+k]!=board[i][j]:
            return False
    return True

#상향 대각선 방향으로 5번 연속됨 확인
#한번이라도 아니라면 False
#모두 다 통과했다면 True
def isDiagUpSeq(i,j):
    for k in range(5):
        if not in_range(i-k,j+k) or board[i-k][j+k]!=board[i][j]:
            return False
    return True

# 이겼는지 검사하는 함수 : 해당인덱스의 숫자 포함 연속(가로or세로or대각선)으로 같은 숫자 5개 나오는지 검사
def is_win(i,j):
    return isHSeq(i,j) or isVSeq(i,j) or isDiagDownSeq(i,j) or isDiagUpSeq(i,j)

#바둑판을 돌며 
#연속으로 같은 숫자가 5개이상인지 확인한다 
    #승자를 결정하고
    #종료한다
def get_winner():
    winner=0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]>0 and is_win(i,j): #승부가 결정되었다면
                winner = board[i][j]
                return winner
    return winner

#출력1: 누가이겼는지 출력 - 아직 승부가 결정되지 않으면 0 출력
winner = get_winner()
print(winner)

#출력2 : 만약 검/흰이 이겼다면 그 연속된 5개의 바둑알 중 가운데 위치한 바둑알의 가로줄번호,세로줄번호 공백두고 출력
if winner > 0:
    k=2
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]>0 and is_win(i,j):
                if isHSeq(i,j): #board[i][j+k]
                    print(i+1, j+k+1)
                elif isVSeq(i,j): #board[i+k][j]
                    print(i+k+1, j+1)
                elif isDiagDownSeq(i,j): #board[i+k][j+k]
                    print(i+k+1, j+k+1) 
                elif isDiagUpSeq(i,j): #board[i-k][j+k]
                    print(i-k+1, j+k+1)