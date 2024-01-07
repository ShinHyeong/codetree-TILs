n1,n2 = map(int,input().split()) #a의 원소수, b의 원소수
a = list(map(int,input().split()))
b = list(map(int,input().split()))

#b수열이 완전히 일치하는지 확인해보자
def is_same(n):
    for i in range(n2):
        if a[i+n] != b[i]:
            return False
    return True

#b가 a의 연속부분수열인지 확인해보자
def is_subseq():
    for i in range(n1-n2+1):
        if is_same(i):
            return True
    return False

if is_subseq():
    print("Yes")
else:
    print("No")