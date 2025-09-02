n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
# b수열이 a[n]부터의 수열과 완전 일치하는지 확인
def is_same(n):
    for i in range(n2):
        if b[i]!=a[n+i]:
            return False
    return True

#가능한 모든 위치에서 해당 수열을 확인해야함
# A = [1, 2, 1, 2, 3]
# B = [2, 3]
# 다음과 같이 A에서 B[0]과 같은 값이 여러 번 나타나는 경우를 방지해야함
def is_subSeq(a,b):
    for i in range(n1-n2+1):
        if is_same(i):
            return True
    return False

#yes, no출력
if is_subSeq(a,b):
    print("Yes")
else:
    print("No")