n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

max_val = 0
# N개의 점 중 3개 고르기
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            #최대넓이의 2배 구하기 : 최대x x 최대y
            area = max(x[i],x[j],x[k]) * max(y[i],y[j],y[k])
            
            #최댓값인지 확인 
            max_val = max(area, max_val)

print(max_val)