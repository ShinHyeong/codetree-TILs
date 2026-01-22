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

## 문제 분석
# (1,2,3)
# (가위,주먹,보) -> (1,3) (2,1) (3,2)
# (가위,보,주먹) -> (1,2) (2,3) (3,1)
# (주먹,가위,보) -> (1,2) (2,3) (3,1)
# (주먹,보,가위) -> (1,3) (2,1) (3,2)
# (보,가위,주먹) -> (1,3) (2,1) (3,2)
# (보,주먹,가위) -> (1,2) (2,3) (3,1)
# 이렇게 첫번째 개발자가 이기는 경우는 (1,3) (2,1) (3,2) 또는 (1,2) (2,3) (3,1) 만 나옴

## 로직
# (1,3) (2,1) (3,2) 경우 세기 (=case1_cnt)
# (1,2) (2,3) (3,1) 경우 세기 (=case2_cnt)
# 둘중 최댓값 고르기

case1_cnt = 0
for i in range(N):
    if (a[i]==1 and b[i]==3) or (a[i]==2 and b[i]==1) or (a[i]==3 and b[i]==2):
        case1_cnt+=1

case2_cnt = 0
for i in range(N):
    if (a[i]==1 and b[i]==2) or (a[i]==2 and b[i]==3) or (a[i]==3 and b[i]==1):
        case2_cnt+=1

print(max(case1_cnt,case2_cnt))