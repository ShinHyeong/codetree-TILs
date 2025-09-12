n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
#만약 이차원 평면의 좌표값들 중 음수가 있을 수 있으므로 offset 설정 : 모든 좌표중에서 가장 작은 좌표값
offset = 0
for k in range(n):
    if x1[k]<0 or x2[k]<0 or y1[k]<0 or y2[k]<0:
        if min(x1[k],x2[k],y1[k],y2[k]) < offset:
            offset = (-1) * min(x1[k],x2[k],y1[k],y2[k])

#offset만큼 더해서 모든 좌표값을 양수로 만들고 시작
for k in range(n):
    x1[k] += offset
    x2[k] += offset
    y1[k] += offset
    y2[k] += offset

#모든 원소가 0인 이차원 배열 생성
checked = [ [0 for _ in range(1+100*2)] for _ in range(1+100*2) ]

#이차원 평면 -> 이차원 배열로 바꿔서 직사각형 색칠
for k in range(n):
    for i in range(x1[k], x2[k]): #x1 ~ x2-1 만큼 색칠
        for j in range(y1[k], y2[k]): #y1 ~ y2-1 만큼 색칠
            checked[i][j] += 1

cnt=0 #한 칸의 색칠 여부 : 색칠되어있으면 0보다 큼

#몇 칸 색칠되었는지 세고, 출력
for i in range(len(checked)):
    for j in range(len(checked[0])):
        if checked[i][j]>0:
            cnt+=1
print(cnt)