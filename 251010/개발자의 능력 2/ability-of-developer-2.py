ability = list(map(int, input().split()))

# Please write your code here.
# 2명씩 3팀으로 배정하기
# 총합이 가장 큰 팀 가장 작은 팀의 차 구하기
# 그 차가 최솟값인지 확인
# 차의 최솟값 출력
# 0 1 2 3 4 5
min_val = 1000000
for x1 in range(len(ability)):
    for x2 in range(x1+1, len(ability)):
        for x3 in range(len(ability)):
            for x4 in range(x3+1, len(ability)):
                if x1==x3:
                    continue

                sum1 = ability[x1]+ability[x2]
                sum2 = ability[x3]+ability[x4]
                sum3 = sum(ability) - sum1 - sum2

                diff = max(sum1,sum2,sum3) - min(sum1,sum2,sum3)

                min_val = min(diff,min_val)

print(min_val)