x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
#만약 이차원 평면의 좌표값들 중 음수가 있을 수 있으므로 offset 설정 : 모든 좌표중에서 가장 작은 좌표값
offset = 0
for k in range(2):
    if x1[k]<0 or x2[k]<0 or y1[k]<0 or y2[k]<0:
        if min(x1[k],x2[k],y1[k],y2[k]) < offset:
            offset = (-1) * min(x1[k],x2[k],y1[k],y2[k])

#offset만큼 더해서 모든 좌표값을 양수로 만들고 시작
for k in range(2):
    x1[k] += offset
    x2[k] += offset
    y1[k] += offset
    y2[k] += offset
 
#모든 원소가 0인 이차원 배열 생성
checked = [ [0 for _ in range(1+1000*2)] for _ in range(1+1000*2) ]

# 1번째 직사각형 -> +1 처리 , 2번째 직사각형 -> 0 처리
for i in range(x1[0],x2[0]):
    for j in range(y1[0],y2[0]):
        checked[i][j]=1

for i in range(x1[1],x2[1]):
    for j in range(y1[1],y2[1]):
        checked[i][j]=0

# 1번째 직사각형의 잔해물 덮기위한 최소 직사각형 넓이 
# 1) 덮이고 난 후 1번째 직사각형(0이 아닌 값)의 가장 큰 x값(=x2)과 작은 x값(=x1) 구하기
# 2) 덮이고 난 후 1번째 직사각형(0이 아닌 값)의 가장 큰 y값과 작은 y값 구하기
min_x, min_y = 2000, 2000
max_x, max_y = 0, 0
for i in range(len(checked)):
    for j in range(len(checked[0])):
        if checked[i][j]==1:
            min_x = min(i, min_x)
            max_x = max(i, max_x)
            min_y = min(j, min_y)
            max_y = max(j, max_y)

# 2) 이를 참고하여 넓이 구하기
cnt=0
for i in range(min_x,max_x+1):
    for j in range(min_y,max_y+1):
        cnt+=1
print(cnt)