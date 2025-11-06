N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.

# 폭탄번호별로 터진횟수를 저장함
MAX_NUM = max(num)
explode_cnt = [0] * (MAX_NUM+1)

# 주어진 폭탄이 터졌는지 안터졌는지 상태를 저장함
explode = [False] * N

for i in range(N):
    for j in range(i+1,N):
        if i-j>K: #거리조건 만족하는지 확인
            break #거리가 k를 초과하는 다음 j도 싹다 넘겨야 함
        
        if num[i]!=num[j]: #거리조건 만족하는데 폭탄번호가 다르면
            continue #거리 만족하는 다음 j 케이스로 이동
        
        #이제 거리조건과 폭탄번호조건 만족함
        #이미 터진 폭탄인지 상태를 확인하고
            #안 터졌으면 터졌다는 상태를 기록한다
            #터진횟수를 카운팅한다

        n1,n2 = num[i],num[j] #조건을 만족하는 폭탄번호
        if explode[i]==False:
            explode[i]=True
            explode_cnt[n1]+=1
        
        if explode[j]==False:
            explode[j]=True
            explode_cnt[n2]+=1


# 가장 많이 터진 횟수를 구하고
#그 횟수에 해당하는 폭탄번호 최댓값 구하기
max_explode_cnt = 1
max_bomb_num = 0
for n,cnt in enumerate(explode_cnt):
    if cnt>=max_explode_cnt:
        max_explode_cnt = cnt
        max_bomb_num = n
print(max_bomb_num)