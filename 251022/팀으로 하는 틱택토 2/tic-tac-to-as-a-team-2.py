inp = [input() for _ in range(3)]

# Please write your code here.
board = [list(map(int, i)) for i in inp]

def is_win(cnt_p1, cnt_p2):
    return (cnt_p1==2 and cnt_p2==1) or (cnt_p1==1 and cnt_p2==2)

# 가로 / 세로 / 대각선으로 같은수2개 다른수1개 조합이 몇개?
PLAYER_MIN_NUM, PLAYER_MAX_NUM = 1, 9

ans = 0

#승리한 플레이어 조합(팀)을 만든다 (player1 != player2)
for player1 in range(PLAYER_MIN_NUM, PLAYER_MAX_NUM+1):
    for player2 in range(player1+1, PLAYER_MAX_NUM+1):
        
        #그 팀이 승리하는 경우 중 하나라도 해당하면 카운팅하고 종료

        win = False #현재 승리한 상태인지

        #가로로 빙고가 만들어지는지 검사
        for i in range(3):
            cnt_p1, cnt_p2 = 0,0
            for j in range(3):
                if board[i][j]==player1:
                    cnt_p1+=1
                if board[i][j]==player2:
                    cnt_p2+=1
            if is_win(cnt_p1, cnt_p2):
                win = True

        #세로로 빙고가 만들어지는지 검사
        for j in range(3):
            cnt_p1, cnt_p2 = 0,0
            for i in range(3):
                if board[i][j]==player1:
                    cnt_p1+=1
                if board[i][j]==player2:
                    cnt_p2+=1
            if is_win(cnt_p1, cnt_p2):
                win = True

        #좌측 상단 -> 우측 하단 방향의 대각선으로 빙고가 만들어지는지 검사
        cnt_p1, cnt_p2 = 0,0
        for k in range(3):
            if board[k][k]==player1:
                cnt_p1+=1
            if board[k][k]==player2:
                cnt_p2+=1
        if is_win(cnt_p1, cnt_p2):
            win = True

        #우측 하단 -> 좌측 상단 방향의 대각선으로 빙고가 만들어지는지 검사
        cnt_p1, cnt_p2 = 0,0
        for k in range(3):
            if board[k][3-k-1]==player1:
                cnt_p1+=1
            if board[k][3-k-1]==player2:
                cnt_p2+=1
        if is_win(cnt_p1, cnt_p2):
            win = True

        if win:
            ans +=1

print(ans)