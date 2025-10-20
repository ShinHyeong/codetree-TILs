n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
# 평행 직선을 3개 골라 그린다
# 모든 포인트들에 대하여
# 모든 세 개의 직선을 지나지 않는 경우 평행 직선 후보 아웃

MAX_X, MAX_Y = 10,10
def isCrossing3Row(line1_coord,line2_coord,line3_coord):
    #y축과 평행한 3개의 직선을 모두 지나는지
    is_crossing_all_lines = True

    for x,y in points: #모든 포인트에 대하여
        if x==line1_coord or x==line2_coord or x==line3_coord:
            continue #점 하나가 하나의 직선이라도 지나면 통과

        #모든 직선을 지나지 않으면
        is_crossing_all_lines = False
    
    return is_crossing_all_lines

def isCrossing2Row1Column(line1_coord,line2_coord,line3_coord):
    #y축과 평행한 2개의 직선, x축과 평행한 1개의 직선을 모두 지나는지
    is_crossing_all_lines = True

    for x,y in points: #모든 포인트에 대하여
        if x==line1_coord or x==line2_coord or y==line3_coord:
            continue #점 하나가 하나의 직선이라도 지나면 통과

        #모든 직선을 지나지 않으면
        is_crossing_all_lines = False
    
    return is_crossing_all_lines

def isCrossing1Row2Column(line1_coord,line2_coord,line3_coord):
    #y축과 평행한 1개의 직선, x축과 평행한 2개의 직선을 모두 지나는지
    is_crossing_all_lines = True

    for x,y in points: #모든 포인트에 대하여
        if x==line1_coord or y==line2_coord or y==line3_coord:
            continue #점 하나가 하나의 직선이라도 지나면 통과

        #모든 직선을 지나지 않으면
        is_crossing_all_lines = False
    
    return is_crossing_all_lines

def isCrossing3Column(line1_coord,line2_coord,line3_coord):
    #x축과 평행한 3개의 직선을 모두 지나는지
    is_crossing_all_lines = True

    for x,y in points: #모든 포인트에 대하여
        if y==line1_coord or y==line2_coord or y==line3_coord:
            continue #점 하나가 하나의 직선이라도 지나면 통과

        #모든 직선을 지나지 않으면
        is_crossing_all_lines = False
    
    return is_crossing_all_lines


ans = 0
for line1_coord in range(MAX_X+1):
    for line2_coord in range(MAX_X+1):
        for line3_coord in range(MAX_X+1):

            if isCrossing3Row(line1_coord,line2_coord,line3_coord):
                ans = 1
            if isCrossing2Row1Column(line1_coord,line2_coord,line3_coord):
                ans = 1
            if isCrossing1Row2Column(line1_coord,line2_coord,line3_coord):
                ans = 1
            if isCrossing3Column(line1_coord,line2_coord,line3_coord):
                ans = 1

print(ans)