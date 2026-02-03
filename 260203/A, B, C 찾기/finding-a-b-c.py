arr = list(map(int, input().split()))

# Please write your code here.

# 최댓값 : A+B+C
# 최솟값 : A
# A<=B<=C
# A<=B<=A+B
# A+B <= B+C <= A+B+C
sorted_arr = sorted(arr)
sum_abc, a, b = sorted_arr[-1], sorted_arr[0], sorted_arr[1]
c = sum_abc - a - b
print(a,b,c)