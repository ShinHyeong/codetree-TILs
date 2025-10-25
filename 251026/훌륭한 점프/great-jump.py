n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

#적혀있는 수의 최댓값이 max_val 라고 할 때 모두 건널 수 있는지
def is_possible(max_val):
    #1번 돌부터 건너야 하므로 1번 돌을 건널 수 없다면 False
    if arr[0] > max_val:
        return False

    #건널 수 있는 돌 리스트를 구한다.
    rocks = []
    for i, digit in enumerate(arr):
        if digit <= max_val:
            rocks.append((i,digit))
    
    #돌들 사이의 거리가 k이내라면 모두 건널 수 있다
    for i in range(len(rocks)-1):
        if rocks[i+1][0] - rocks[i][0] > k:
            return False

    return True

MAX_DIGIT = 100
answer = MAX_DIGIT
for max_val in range(min(arr), max(arr)+1):
    if is_possible(max_val):
        answer = min(answer, max_val)
print(answer)