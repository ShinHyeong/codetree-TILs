n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.

## 요구사항 분석 ##
# 특정 위치 블록을 다른 위치로 옮긴다
# 이를 반복하여, 모든 위치에 놓인 블럭 개수가 동일해지게 만든다
# 움직여야할 최소 블럭 수를 구하자

## 예제분석 ##
# 다 더하면 2+10+7+1=20
# 균일하게 분배하면 5
# 5보다 작은 값은 (2,1) 5보다 큰 값은 (10,7)이다
# 어차피 큰 값을 작은 값으로 이동해야하므로 5+2 = 7이다

## 로직설정 ##
# 다 더하고 목표값을 구한다
sum_val = sum(blocks)
target = sum_val//n
# 목표값보다 큰 값이면 목표값과의 차이를 더해서 그 합을 리턴한다
movement = 0
for ele in blocks:
    if ele > target:
        movement += ele-target
print(movement)