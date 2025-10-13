N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
#같은 번호이고 거리 K안에 있다면 [폭발] 처리
#폭발된 폭탄이 가장 큰 번호인지 확인
#가장 큰 번호 출력
#[0,1,2,3,4,5] -> 1 4
max_num = 0 #가장 큰 번호 : 폭탄이 가질 수 있는 번호의 최솟값으로 초기화

for target in range(len(num)):
    for i in range(target+1, len(num)):
        if num[target]==num[i] and (i-target)<=3:
            max_num = max(num[target], max_num)

print(max_num)