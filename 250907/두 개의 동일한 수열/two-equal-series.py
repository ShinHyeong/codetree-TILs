n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
# 순서와 상관없이 원소의 구성이 같은지 확인
# 1. 두 리스트를 오름차순으로 정렬
A.sort()
B.sort()

# 2. 리스트 처음부터 끝까지 돌면서 원소 같은지 확인
def is_same(A,B):
    for i in range(n):
        if A[i]!=B[i]:
            return False
    return True

# 3. yes/no 출력
if is_same(A,B):
    print("Yes")
else:
    print("No")