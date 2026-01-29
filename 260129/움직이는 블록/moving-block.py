n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.

## 요구사항 분석 ##
# 특정 위치 블록을 다른 위치로 옮긴다
# 이를 반복하여, 모든 위치에 놓인 블럭 개수가 동일해지게 만든다
# 움직여야할 최소 블럭 수를 구하자

## 로직 설정 ##
# 일단 가장 많은 블록 위치를 확인한다
# 맨 앞 위치에 가장 많은 블록위치가 2번째로 블록 개수가 될때까지 옮긴다
# 
sorted_blocks = sorted(blocks)
max_idx, max_idx2 = -1,-1
max_val, max_val2 = sorted_blocks[0], sorted_blocks[1]
for i in range(n):
    if blocks[i]==max_val:
        max_idx = i
    if blocks[i]==max_val2:
        max_idx2 = i

