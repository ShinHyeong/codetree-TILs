n = int(input())
adjacent = list(map(int, input().split()))

# Please write your code here.

# 합계배열 S에서 0번쨰 원소인 S[0]=A[0]+A[1] => A[1]=S[0]-A[0]
# S[1]=A[1]+A[2] => A[2]=S[1]-A[1]
# A[0]만 구하면 나머지도 순차적으로 구해진다

for a_0 in range(1,n+1): #A[0] 후보를 정한다
    ori = [a_0]
    for i in range(n-1): #A[1]~A[n-1]까지 추가한다
        ori.append(adjacent[i]-ori[i])

    #한 번씩만 등장하는지 검토한다
    overlap = False
    for v1 in range(n):
        for v2 in range(v1+1,n):
            if ori[v1] == ori[v2]:
                overlap = True
                break

    if overlap==True:
        continue
    else:
        break

for o in ori:
    print(o, end=" ")



# A
# n=2 ; [1,2] -> 3
# n=3 : [1,2,3] -> 3+5 [1,3,2] -> 4+5 [2,1,3] -> 3+4 ...
# n=4 : [1,2,3,4] -> 
# 1~N이하 숫자 나열 -> 그 리스트의 순서만 바꿔서 -> 2번쨰 줄 입력과 일치하는지 확인



# 인접한 원소의 합 : 순서대로 구한 n-1 -> 초기수열 복원
# 1이상 N 이하의 숫자들이 단 한번씩만 등장하는 길이가 N인 수열 A