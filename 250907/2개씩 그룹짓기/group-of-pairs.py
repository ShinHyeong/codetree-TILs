n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
# 각 그룹의 원소 합 중 최댓값이 최소가 되도록
# n=2, 주어진 원소: 3 5 5 2
# 그룹핑1 : [5,5],[3,2] -> 각 그룹의 합 : 10, 5 -> 최댓값: 10 
# 그룹핑2 : [3,5],[5,2] -> 각 그룹의 합 : 8, 7 -> 최댓값: 8 이며 이보다 최댓값 더 작게 못만듦

# 오름차순으로 정렬한 후 : 2 3 5 5
nums.sort()

# 처음+끝으로 그룹핑 arr[0]+arr[3] / arr[1]+arr[2]
sum_vals = []
for i in range(n):
    sum_vals.append(nums[i]+nums[2*n-1-i])
# 각 그룹의 합 구하고
# 가장 작은거 출력
print(max(sum_vals))