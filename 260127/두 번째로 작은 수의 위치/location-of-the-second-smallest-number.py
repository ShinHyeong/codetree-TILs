n = int(input())
a = [0] + list(map(int, input().split()))

# Please write your code here.

##요구사항 분석
# 첫번째 원소의 위치는 1로 생각하라
# 2번째로 작은 수가 없거나 여러개 있으면 -1을 출력하라
# 2번째로 작은 수의 위치를 출력하라

##로직 설정
# 첫번째로 작은 수를 찾는다
# 첫번째보다 +1 큰 수를 찾는다 -> +2 큰수를 찾는다 ... 반복 (최대 99*n 번 수행)
    # 여러개 있으면 -1 출력
# 위치 출력
    # 없으면 -1 출력

ans = -1
min_val = min(a[1:])

for i in range(1,100):
    cnt = 0

    for j in range(1, n+1):
        if a[j] == min_val + i:
            ans = j
            cnt += 1

        if cnt > 1:
            ans = -1
            break

    if cnt >= 1:
        break

print(ans)