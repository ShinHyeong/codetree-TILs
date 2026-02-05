arr = list(map(int, input().split()))

# Please write your code here.
# 최솟값: A, 2번째로 작은값: B, 최댓값: A+B+C+D
# 3번째로 작은값: C. 왜냐하면 A+B가 C이상이기 때문.
sorted_arr = sorted(arr)
a,b,c,abcd = sorted_arr[0], sorted_arr[1], sorted_arr[2], sorted_arr[-1]
d = abcd-a-b-c
print(a,b,c,d)