n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# (15 2) (7 9) (10 5) -> 13 2 5 -> 2
# (15 7) (2 9) (10 5) -> 8 7 5 -> 5
# 최소 차이가 최대가 되려면
# 2 5 7 9 10 15

sorted_arr = sorted(arr)
min_val = 10**9
for i in range(n):
    min_val = min(min_val, abs(sorted_arr[i]-sorted_arr[i+n]))
print(min_val)