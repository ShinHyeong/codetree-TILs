n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
# x리스트와 y리스트에 있는 요소 3개 뽑아서
# 모든 좌표를 지나는지 확인하기

# 모든 포인트들에 대하여
# 평행 직선을 3개 골라 그린다
# 모든 세 개의 직선을 지나지 않는 경우 평행 직선 후보 아웃
# 평행 직선이 하나라도 있으면  1 출력 아니면 0 출력
MAX_X, MAX_Y = 10,10
def yyy_ok():
    for line1_y in range(MAX_Y+1):
        for line2_y in range(line1_y+1, MAX_Y+1):
            for line3_y in range(line2_y+1, MAX_Y+1):

                isnot_crossing_all_lines = False
                for i in range(n): #i번째 포인트에 대하여
                    if (y[i]!=line1_y)and(y[i]!=line2_y)and(y[i]!=line3_y):
                        isnot_crossing_all_lines = True
                        break

                if isnot_crossing_all_lines==False:
                    return True
    return False  

def yyx_ok():
    for line1_y in range(MAX_Y+1):
        for line2_y in range(MAX_Y+1):
            for line3_x in range(MAX_X+1):
                
                if line1_y==line2_y:
                    continue

                isnot_crossing_all_lines = False
                for i in range(n): #i번째 포인트에 대하여
                    if (y[i]!=line1_y)and(y[i]!=line2_y)and(x[i]!=line3_x):
                        isnot_crossing_all_lines = True
                        break

                if isnot_crossing_all_lines==False:
                    return True
    return False  

def yxx_ok():
    for line1_y in range(MAX_Y+1):
        for line2_x in range(MAX_X+1):
            for line3_x in range(MAX_X+1):
                
                if line2_x==line3_x:
                    continue

                isnot_crossing_all_lines = False
                for i in range(n): #i번째 포인트에 대하여
                    if (y[i]!=line1_y)and(x[i]!=line2_x)and(x[i]!=line3_x):
                        isnot_crossing_all_lines = True
                        break

                if isnot_crossing_all_lines==False:
                    return True
    return False  

def xxx_ok():
    for line1_x in range(MAX_X+1):
        for line2_x in range(line1_x+1, MAX_X+1):
            for line3_x in range(line2_x+1, MAX_X+1):

                isnot_crossing_all_lines = False
                
                for i in range(n): #i번째 포인트에 대하여
                    if (x[i]!=line1_x)and(x[i]!=line2_x)and(x[i]!=line3_x):
                        isnot_crossing_all_lines = True
                        break

                if isnot_crossing_all_lines==False:
                    return True
    return False  

if yyy_ok() or yyx_ok() or yxx_ok() or xxx_ok():
    print(1)
else:
    print(0)