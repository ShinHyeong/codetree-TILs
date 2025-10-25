n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

#적혀있는 수의 최댓값이 max_val 라고 할 때 모두 건널 수 있는지
def is_possible(max_val):
    #1번 돌부터 n번 돌까지 max_val을 넘지 않으면서 돌들 사이의 거리가 k이내여야 한다
    #1번 돌부터 건너야 하므로 1번 돌을 건널 수 없다면 False
    if arr[0] > max_val:
        return False

    curr_idx = 0
    for i in range(1, n):
        if arr[i] <= max_val: 
            if i-curr_idx > k: #만약 돌들 사이의 거리가 k이내가 아니라면 계속 건널 수 없다 
                return False
            curr_idx = i #계속 건넌다
    
    return True

# 모두 건널 수 있는 최댓값의 범위를 정한다. 최댓값을 발견하는 즉시 출력후 종료한다 (그 값이 최솟값이기 때문)
for max_val in range(min(arr),max(arr)+1): 
    if is_possible(max_val):
        print(max_val)
        break