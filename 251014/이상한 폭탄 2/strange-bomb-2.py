N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
#같은 번호이고 거리 K안에 있다면 [폭발] 처리
#폭발된 폭탄이 가장 큰 번호인지 확인
#가장 큰 번호 출력

max_num = -1 

for target in range(len(num)):
    for i in range(target+1, len(num)):
        if num[target]==num[i] and i-target<=K:
            max_num = max(num[target], max_num)

print(max_num)