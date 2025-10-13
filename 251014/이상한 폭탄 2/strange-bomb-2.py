N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
#같은 번호이고 거리 K안에 있다면 [폭발] 처리
#폭발된 폭탄이 가장 큰 번호인지 확인
#가장 큰 번호 출력

max_num = 0 #가장 큰 번호 : 폭탄이 가질 수 있는 번호의 최솟값으로 초기화

for target in range(len(num)):
    for i in range(target+1, len(num)):
        if num[target]==num[i] and target<=(K-1):
            max_num = max(num[target], max_num)

print(max_num)

#[7,3,4,2,3,4,8,4,6,7]
#[7,4,2,4,8,4,6,7] #3폭발
#[7,2,8,6,7] #4폭발
#