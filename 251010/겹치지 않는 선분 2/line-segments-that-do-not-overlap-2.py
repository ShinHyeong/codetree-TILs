n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
x1 = [line[0] for line in lines]
x2 = [line[1] for line in lines]

#하나의 선분을 고르고
#나머지 선분의 위치를 하나씩 확인하면서 겹치는 선분인지 확인한다
#겹치지 않는 선분이라면 카운팅한다

answer = 0 #겹치지 않는 선분의 갯수
for i in range(n): #하나의 선분을 고르고
    overlap = False
    for j in range(n):
        #자기자신은 확인하지 않는다
        if i==j:
            continue

        #겹치는가 : 겹치는 특징에 해당된다면 세지 않는다
        if (x1[i]<=x1[j] and x2[j]<=x2[i]) or (x1[j]<=x1[i] and x2[i]<=x2[j]):
            overlap = True
            break

    if overlap == False: #선분 i는 겹치지 않는 선분이구나
        answer +=1

print(answer)