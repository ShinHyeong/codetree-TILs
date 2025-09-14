N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.
infected = [0] * (N+1) # 감염자 여부 (0:음성/1:양성)
infected_cnt = [0] * (N+1) #감염시킬수 있는 횟수

# 최초 감염자 양성처리
infected[P] = 1
infected_cnt[P] = K

# T번에 걸친 악수 정보(t,x,y)를 바탕으로
#     handshakes[i][0] : t초 시점에 악수
#    handshakes[i][1] : x개발자
#    handshakes[i][2] : y개발자

#일단 시간순으로 오름차순으로 튜플나열
handshakes.sort(key=lambda h : h[0])

#악수 시뮬레이션
#양성인 개발자가 악수하면 그와 악수한 해당 개발자 양성(1) 처리
#단, 최대 k번의 악수 동안만 전염병을 옮길 수 있음 -> 카운팅
#print("handshakes:", handshakes)
#print("infected:", infected)
#print("cnt:", infected_cnt)

for h in handshakes:
    #print("h:", h)

    if infected[h[1]]==1: #1) x개발자만 감염된 경우
        if infected_cnt[h[1]]>0: #감염시킬 수 있다면
            infected[h[2]], infected_cnt[h[2]] = 1,2 #감염시키기
            infected_cnt[h[1]]-=1 #감염횟수차감
    elif infected[h[2]]==1: #2) y개발자만 감염된 경우
        if infected_cnt[h[2]]>0: #감염시킬 수 있다면
            infected[h[1]], infected_cnt[h[1]] = 1, 2 #감염시키기
            infected_cnt[h[2]]-=1 #감염횟수차감
    elif infected[h[1]]==1 and infected[h[2]]==1: #3) 둘다 감염된 경우
        if infected_cnt[h[1]]>0: #감염시킬 수 있다면
            infected_cnt[h[1]]-=1 #감염횟수차감
        if infected_cnt[h[2]]>0: #감염시킬 수 있다면
            infected_cnt[h[2]]-=1 #감염횟수차감

    #print("infected:", infected)
    #print("cnt:", infected_cnt)

# 모든 악수 진행한 후 최종적으로 누가 전염병에 걸리게 되었는지 (1번 개발자부터 출력)
for i in infected[1:]:
    print(i,end='')