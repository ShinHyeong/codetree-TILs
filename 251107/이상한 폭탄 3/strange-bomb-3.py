N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.

#가장 많이 터진 폭탄의 "번호"를 물어봄 -> 번호 단위로 완전탐색

unique_num = []
for i in range(N):
    if num[i] not in unique_num:
        unique_num.append(num[i])

bomb_list = []
for n in unique_num:

    #해당 번호의 폭탄 터졌는지 확인
    is_bomb = [False]*N
    for i in range(N):
        for j in range(i+1,N):
            if num[i]==n and num[j]==n and j-i<=K:
                is_bomb[i], is_bomb[j] = True,True

    #그 번호의 터진 폭탄 갯수 세기
    bomb_cnt = 0
    for b in is_bomb:
        if b==True:
            bomb_cnt +=1
    
    #저장 (폭탄번호, 터진횟수)
    bomb_list.append((n, bomb_cnt))

#가장 많이 터진 횟수 구하기
max_bomb_cnt = 0
for n,bomb_cnt in bomb_list:
    max_bomb_cnt = max(max_bomb_cnt, bomb_cnt)

#그 횟수에 해당하는 폭탄번호 최댓값 구하기
max_bomb_num = 0
for n,bomb_cnt in bomb_list:
    if bomb_cnt == max_bomb_cnt:
        max_bomb_num = max(n, max_bomb_num)

#아무 폭탄도 터지지 않을 경우 0 출력
print(max_bomb_num if max_bomb_cnt!=0 else 0)