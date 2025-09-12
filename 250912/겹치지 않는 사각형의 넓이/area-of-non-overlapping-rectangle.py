x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
#만약 이차원 평면의 좌표값들 중 음수가 있을 수 있으므로 offset 설정 : 모든 좌표중에서 가장 작은 좌표값
offset = 0
for k in range(3):
    if x1[k]<0 or x2[k]<0 or y1[k]<0 or y2[k]<0:
        if min(x1[k],x2[k],y1[k],y2[k]) < -offset:
            offset = (-1) * min(x1[k],x2[k],y1[k],y2[k])

#offset만큼 더해서 모든 좌표값을 양수로 만들고 시작
for k in range(3):
    x1[k] += offset
    x2[k] += offset
    y1[k] += offset
    y2[k] += offset

#모든 원소가 0인 이차원 배열 생성
checked = [ [0 for _ in range(1+1000*2)] for _ in range(1+1000*2) ]

#2차원 좌표평면 -> 2차원 배열로 옮겨서 직사각형 칠하기
#k번째 직사각형->k으로 채우기
for k in range(3):
    for i in range(x1[k],x2[k]):
        for j in range(y1[k],y2[k]):
            checked[i][j] = k+1
            
#1 또는 2로 채워진 칸의 갯수 출력
cnt=0
for i in range(len(checked)):
    for j in range(len(checked[0])):
        if checked[i][j]==1 or checked[i][j]==2:
            cnt+=1
print(cnt)