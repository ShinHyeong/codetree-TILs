n = int(input())
adjacent = list(map(int, input().split()))

# Please write your code here.

# 합계배열 S에서 0번쨰 원소인 S[0]=A[0]+A[1] => A[1]=S[0]-A[0]
# S[1]=A[1]+A[2] => A[2]=S[1]-A[1]
# A[0]만 구하면 나머지도 순차적으로 구해진다

def is_valid(tmp): #한 번씩만 등장하는지 검토한다
    exist = [False] * (n+1) #idx: 0~n
    for t in tmp:
        if t>n or t<1: #원소는 1과 n사이에 있어야한다.
            return False
        if exist[t]==True:
            return False
        exist[t] = True
    return True


for a_0 in range(1,n+1): #A[0] 후보를 정한다
    ori = [a_0]
    for i in range(n-1): #A[1]~A[n-1]까지 추가한다
        ori.append(adjacent[i]-ori[i])
    
    if is_valid(ori): #후보 original이 완성되면 조건에 유효한지 확인하고 완전탐색을 멈춘다
        break
        
for o in ori: #조건에 맞는 original을 출력한다
    print(o, end=" ")
        