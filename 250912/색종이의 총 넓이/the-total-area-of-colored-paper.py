n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
#만약 이차원 평면의 좌표값들 중 음수가 있을 수 있으므로 offset 설정 : 모든 좌표중에서 가장 작은 좌표값
offset = 0
for k in range(n):
    if x[k]<0 or y[k]<0:
        if min(x[k],y[k]) < offset:
            offset = (-1) * min(x[k],y[k])

#offset만큼 더해서 모든 좌표값을 양수로 만들고 시작
for k in range(n):
    x[k] += offset
    y[k] += offset
    
#모든 원소가 0인 이차원 배열 생성
checked = [ [0 for _ in range(1+100*2)] for _ in range(1+100*2) ]

#가로세로 길이 8, 넓이 64인 n개의 사각형 색칠
for k in range(n):
    for i in range(x[k],x[k]+8):
        for j in range(y[k],y[k]+8): 
            checked[i][j]+=1

cnt=0
for i in range(len(checked)):
    for j in range(len(checked[0])):
        if checked[i][j]>0:
            cnt+=1
print(cnt)