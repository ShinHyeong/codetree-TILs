n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

#두 점 사이의 거리 제곱한 값의 최솟값 구하기 로직
#1. 두 점을 하나씩 다 잡아본다
#2. 거리 제곱 값이 최솟값인지 확인한다
#3. 최솟값을 출력한다

min_val = (1000**2)+(1000**2)
for i in range(n):
    for j in range(i+1, n):
        dist = (x[i]-x[j])**2 + (y[i]-y[j])**2
        min_val = min(dist, min_val)
print(min_val)