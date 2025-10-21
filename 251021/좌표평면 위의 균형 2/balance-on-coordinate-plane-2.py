n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# x축과 y축에 평행한 직선 각각 1개씩 긋기
# 4군데의 점 각각 세기
# 4군데 중 가장 많은 점의 수(M)이 최솟값인지 확인하기
# M 출력

x_list, y_list = [p[0] for p in points], [p[1] for p in points]
MAX_N = 100
min_val = MAX_N

for line_x in range(0,max(y_list),2): #x축과 평행한 직선 1개 선택
    for line_y in range(0,max(x_list),2): #y축과 평행한 직선 1개 선택

        cntInArea1, cntInArea2, cntInArea3, cntInArea4 = 0,0,0,0
        
        for x,y in points:   
            if x>line_y and y>line_x:
                cntInArea1 += 1
            if x<line_y and y>line_x:
                cntInArea2 += 1
            if x<line_y and y<line_x:
                cntInArea3 += 1
            if x>line_y and y<line_x:
                cntInArea4 += 1
        
        M = max(cntInArea1,cntInArea2, cntInArea3, cntInArea4)
        min_val = min(min_val, M)        

print(min_val)
    