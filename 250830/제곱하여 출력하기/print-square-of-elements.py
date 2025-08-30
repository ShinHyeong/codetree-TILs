n=int(input())
arr = list(map(int,input().split()))
for ele in [x**2 for x in arr]:
    print(ele, end=" ")