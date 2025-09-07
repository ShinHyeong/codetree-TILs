n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
#오름차순 정렬
nums.sort()
#k번째 숫자 출력
print(nums[k-1])