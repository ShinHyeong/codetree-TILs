n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
# 1. 좌표평면 -> 2차원 배열로 변경
# 1) 음수 -> 양수 처리
#만약 이차원 평면의 좌표값들 중 음수가 있을 수 있으므로 offset 설정 : 모든 좌표중에서 가장 작은 좌표값
offset = 0
for k in range(n):
    if x1[k]<0 or x2[k]<0 or y1[k]<0 or y2[k]<0:
        if min(x1[k],x2[k],y1[k],y2[k]) < -offset:
            offset = (-1) * min(x1[k],x2[k],y1[k],y2[k])

#offset만큼 더해서 모든 좌표값을 양수로 만들고 시작
for k in range(n):
    x1[k] += offset
    x2[k] += offset
    y1[k] += offset
    y2[k] += offset
    
# 2) 0으로 채워진 2차원 배열 생성
checked = [[0 for _ in range(1+100*2)] for _ in range(1+100*2)]

# 2. n개의 직사각형 색칠하기
# 처음에 주어지는 직사각형 : 빨간색
# 빨->파->빨->파-> ... 번갈아가며 주어짐 : 즉, 0,2,4,... 짝수번째 시도는 빨간색 / 1,3,5,... 홀수번째 시도는 파란색
# 겹치는 위치가 있다면 가장 마지막에 덮힌 색으로 취급
# 빨간색 -> 1로 처리 / 파란색 -> 2로 처리
for k in range(n): #k번째 직사각형 색칠
    if k%2==0: #빨간색(=1)로 색칠
        color = 1
    else:
        color = 2

    for i in range(x1[k],x2[k]):
        for j in range(y1[k],y2[k]):
            checked[i][j]=color

# 3. 파란색의 총 넓이 출력
cnt=0
for i in range(len(checked)):
    for j in range(len(checked[0])):
        if checked[i][j]==2:
            cnt+=1
print(cnt)