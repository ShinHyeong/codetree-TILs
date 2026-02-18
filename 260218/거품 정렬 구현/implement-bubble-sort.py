n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n-1):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
            tmp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = tmp

for ele in arr:
    print(ele, end=" ")