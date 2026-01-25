N = int(input())
seats = input()

# Please write your code here.
### 요구사항 분석
# 원래 자리는 그대로
# 가장 가까운 두 사람 간의 거리를 최대로 하고싶다.


### 로직 설정
# c1 : 0으로 시작, 1로 끝 -> 맨 앞에 1을 붙인다
    #0010000001000001 
    #0000001000001
# c2 : 1로 시작, 0으로 끝 -> 맨 뒤에 1을 붙인다
# c3 : 0으로 시작, 0으로 끝 -> 맨 앞과 맨 뒤에 1을 붙인다

# 가장 먼 두 사람 간의 거리를 구한다
# '1'와'x' 사이랑 그냥 '1'간의 사이 어떤 게 더 거리가 큰지 확인한다
# '1'와 'x'사이가 크다면 그 거리를 리턴하고,
# '1'간의 사이가 크다면 중간 위치과 1간의 거리를 리턴한다

seats = list(seats)

dist1,dist2 = -1,-1
if seats[0]=='0' and seats[1]=='0' and seats[N-1]=='0' and seats[N-2]=='0':
    seats[0]='x'
    seats[N-1]='x'

    for i in range(N):
        if seats[i]=='1':
            dist1 = i-0
            break
    for i in range(N-1,-1,-1):
        if seats[i]=='1':
            dist2 = (N-1)-i
            break

elif seats[0]=='0' and seats[1]=='0':
    seats[0]='x'
    for i in range(N):
        if seats[i]=='1':
            dist1 = i-0
            break

elif seats[N-1]=='0'and seats[N-2]=='0':
    seats[N-1]='x'
    for i in range(N-1,-1,-1):
        if seats[i]=='1':
            dist2 = (N-1)-i
            break

dist3 = 0
max_i,max_j = -1,-1
for i in range(N):
    if seats[i]=='1':
        for j in range(i+1,N):
            if seats[j]=='1':
                if j-i > dist3:
                    dist3 = j-i
                    max_i,max_j = i, j

                break

#print("".join(seats))
#print(max_i,max_j)
#print(dist1,dist2,dist3//2)
max_dist = max(dist1,dist2,dist3//2)

if max_dist==dist1 or max_dist==dist2:
    if dist1 > 0 and dist1 == min(dist1,dist2):
        answer = dist1
    else:
        answer = dist2
else:
    answer = dist3//2
print(answer)