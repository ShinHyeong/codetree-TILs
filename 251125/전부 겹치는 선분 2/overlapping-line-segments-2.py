n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

# Please write your code here.

#[접근방법]
#하나의 선분을 제외하고
#시작점에서의 가장 큰 값 (max_x1)
#끝점에서의 가장 작은 값(min_x2)을 구한다
# 모든 선분이 다 겹치는 조건인지 확인한다 (max_x1 <= min_x2)
MIN_X,MAX_X = 1,100

all_overlap = False
for e in range(n): #제외할 선분 하나를 뽑는다

    max_x1,min_x2 = MIN_X, MAX_X
    for i in range(n): #그 선분을 제외한 max_x1, min_x2을 구한다
        if i==e:
            continue
        max_x1 = max(x1[i],max_x1)
        min_x2 = min(x2[i],min_x2)

    if max_x1 <= min_x2:
        all_overlap = True
        break

print("Yes" if all_overlap else "No")