n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

max_val = 0
# N개의 점 중 3개 고르기
for i in range(n):
    for j in range(n):
        for k in range(n):
            #3개의 점은 모두 다른 점이다
            if i==j or i==k or j==k:
                continue

            #삼각형을 만들 수 있는 필수조건: 
            #dot1,dot2,dot3를 골랐다고 쳤을 때, dot3 = (dot1의 x좌표, dot2의 y좌표)
            if not(x[k]==x[i] and y[k]==y[j]):
                continue

            #최대넓이의 2배 구하기
            max_x = max(x[i],x[j],x[k])
            min_x = min(x[i],x[j],x[k])
            max_y = max(y[i],y[j],y[k])
            min_y = min(y[i],y[j],y[k])
            area = (max_x-min_x) * (max_y-min_y)
            #print("x",max_x, "y",max_y)
            #최댓값인지 확인 
            max_val = max(area, max_val)

#삼각형을 만들 수 없다면 0 출력
print(max_val)