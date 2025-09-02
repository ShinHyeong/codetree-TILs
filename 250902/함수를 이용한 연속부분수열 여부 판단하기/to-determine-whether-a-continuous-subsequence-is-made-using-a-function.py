n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
#b의 첫번째 원소를 a에서 어느위치에 있는지 확인
def firstElementIndexInListA(a, b):
    for i in range(n1):
        if a[i]==b[0]:
            return i
    return -1

#b의 첫번째 원소를 a에서 어느위치에 있는지 확인
#b의 처음~끝까지 돌면서 a도 그 인덱스부터 같이 비교하면서 돌았는데 한번도 어긋남없이 같다면 연속부분수열임
def is_subSeq(a,b):
    if a.index(b[0])>=0: 
        firstElementIndexInListA = a.index(b[0])
    else:
        return False 

    for i in range(n2):
        if b[i]!=a[firstElementIndexInListA+i]:
            return False
    return True

#yes, no출력
if is_subSeq(a,b):
    print("Yes")
else:
    print("No")