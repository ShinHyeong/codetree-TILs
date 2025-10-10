n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

#제외할 점 하나씩 정해보고
#제외한 후 만든 직사각형의 넓이가 최솟값인지 확인한다
#최솟값 출력

# 직사각형의 가로 : max_x - min_x / ex. 5-1 
# 직사각형의 세로 : max_y - min_y / ex. 4-1
# 직사각형의 넓이 : 가로 x 세로
min_val = 40000*40000
for e in range(len(points)): #제외할 점을 하나 정한다
    max_x, max_y, min_x, min_y = 1,1,40000,40000

    for i in range(len(points)): #제외한 후 만든 직사각형의 가로,세로를 구한다
        if i==e:
            continue
        max_x = max(x[i], max_x)
        max_y = max(y[i], max_y)
        min_x = min(x[i], min_x)
        min_y = min(y[i], min_y)

    area = (max_x - min_x)*(max_y - min_y)  #제외한 후 만든 직사각형의 넓이를 구한다
   
    min_val = min(area, min_val) #최솟값인지 확인한다

print(min_val)