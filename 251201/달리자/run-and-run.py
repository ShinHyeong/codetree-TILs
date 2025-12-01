n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

# 오른쪽 집으로 갈 수밖에 없다
# 그러면 크기가 줄어든 i부터 크기가 늘어난 i로 옮겨준다
dst = 0
for i in range(n):
    if A[i]>B[i]: #크기가 줄어든 i부터
        for j in range(i+1, n):
            if A[j]<B[j]:
                dst += (A[i]-B[i])*(j-i) #크기가 늘어난 i로 옮겨준다
                break

print(dst)