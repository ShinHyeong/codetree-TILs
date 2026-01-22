N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]
a, b = zip(*moves)
a, b = list(a), list(b)

# Please write your code here.
##예제 분석
# 총 5판
# 1 2 -> 가위 주먹 (패)
# 2 2 -> 주먹 주먹 (무승부)
# 1 3 -> 가위 보 (승)
# 1 1 -> 가위 가위 (무승부)
# 3 2 -> 보 주먹 (승)
# 총 2판 승리

# 3*2*1=6
# (1,2,3)
# (가위,주먹,보) 
# (가위,보,주먹)
# (주먹,가위,보)
# ...

#로직
#6가지 경우에 대해서 승리하는 횟수를 구한다
case_list = [("s","r","p"),("s","p","r"),
                ("r","s","p"),("r","p","s"),
                ("p","s","r"),("p","r","s")]
max_win_cnt = 0
for case in case_list:
    for i in range(N):
        if a[i]==1:
            a[i]=case[0]
        elif a[i]==2:
            a[i]=case[1]
        else:
            a[i]=case[2]
        if b[i]==1:
            b[i]=case[0]
        elif b[i]==2:
            b[i]=case[1]
        else:
            b[i]=case[2]

    win_cnt = 0
    for i in range(N):
        if (a[i]=="s" and b[i]=="p") or (a[i]=="r" and b[i]=="s") or (a[i]=="p" and b[i]=="r"):
            win_cnt += 1
    max_win_cnt = max(win_cnt, max_win_cnt)

print(max_win_cnt)