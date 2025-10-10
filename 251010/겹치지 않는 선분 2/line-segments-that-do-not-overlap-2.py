n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
x1 = [line[0] for line in lines]
x2 = [line[1] for line in lines]

#하나의 선분을 고르고
#나머지 선분의 위치를 하나씩 확인하면서 겹치는지 확인한다
#겹친다면 그 수를 카운팅한다
#(전체 선분 갯수 - 겹치는 선분 갯수) 출력

cnt=0 #겹치는 선분의 갯수
for i in range(n): #하나의 선분을 고르고
    for j in range(n):
        if i==j: #나머지 선분에 대해서만 확인한다
            continue
        #겹치는가 : 겹치는 특징에 해당된다면 카운팅한다
        if (x1[i]<=x1[j] and x2[j]<=x2[i]) or (x1[j]<=x1[i] and x2[i]<=x2[j]):
            cnt+=1

print(n-cnt)