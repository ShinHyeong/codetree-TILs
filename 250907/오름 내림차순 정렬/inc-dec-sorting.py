n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort() #오름차순 정렬
for ele in nums:
    print(ele, end=' ') #출력

print()

nums.sort(reverse=True) #내림차순 정렬
for ele in nums:
    print(ele, end=' ') #출력