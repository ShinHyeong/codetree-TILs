k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# Please write your code here.

# 경기마다 랭킹을 기록한다
ranking = [[0]*(n) for _ in range(k)]
for i in range(k):
    for rank in range(n):
        num = arr[i][rank]
        ranking[i][num-1] = rank

always_wins = [[True]*(n) for _ in range(n)] #항상 이기는지 기록하는 리스트
for i in range(len(ranking)): #경기마다
    for winner in range(n):
        for loser in range(n): #각 개발자에 대해 분석한다
            if winner==loser: #자기자신에 대해선 카운팅하면 안되므로 False
                always_wins[winner][loser] = False
            if ranking[i][winner]>ranking[i][loser]: #한번이라도 지면 False
                always_wins[winner][loser] = False

#True의 갯수를 산다
cnt=0
for winner in range(len(always_wins)):
    for loser in range(len(always_wins[0])):
        if always_wins[winner][loser]:
            cnt+=1
print(cnt)