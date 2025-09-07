n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
# 주어진 문자열로 시작하는지 확인 : arr[0]==t[0], arr[1]==t[1], ... arr[len(t)-1]=t[len(t)-1]
def is_same(arr, pattern):
    for i in range(len(pattern)):
        if arr[i]!=pattern[i]:
            return False
    return True

# 주어진 문자열로 시작하는 단어만 선택
# 1. 리스트 처음~끝 돌면서
# 2. 주어진 문자열로 시작하는지 확인 : arr[0]==t[0], arr[1]==t[1], ... arr[len(t)-1]=t[len(t)-1]
same_starts = []
for s in str:
    arr = list(s)
    if is_same(arr, t):
        same_starts.append(s)

# 사전순으로 정렬
same_starts.sort()

# k번째 문자열 출력
print(same_starts[k-1])