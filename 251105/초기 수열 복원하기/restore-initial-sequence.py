n = int(input())
adjacent = list(map(int, input().split()))

# Please write your code here.

# 합계배열 S에서 0번쨰 원소인 S[0]=A[0]+A[1] => A[1]=S[0]-A[0]
# S[1]=A[1]+A[2] => A[2]=S[1]-A[1]
# A[0]만 구하면 나머지도 순차적으로 구해진다

def is_onlyone_appear(tmp): #한 번씩만 등장하는지 검토한다
    for idx1 in range(n):
        for idx2 in range(idx1+1,n):
            if tmp[idx1]==tmp[idx2]:
                return False
    return True

def is_between_1n(tmp):
    for t in tmp:
        if t>n or t<1:
            return False
    return True

for a_0 in range(1,n+1): #A[0] 후보를 정한다
    ori = [a_0]
    for i in range(n-1): #A[1]~A[n-1]까지 추가한다
        ori.append(adjacent[i]-ori[i])
    
    if is_onlyone_appear(ori) and is_between_1n(ori):
        break
        
for o in ori:
    print(o, end=" ")
        