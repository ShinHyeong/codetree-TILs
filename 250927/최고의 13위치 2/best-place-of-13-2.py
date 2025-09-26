n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def in_range(x,y):
    """
    주어진 좌표가 nxn 격자 범위내에 있는지
    """
    return (0<=x and x<n) and (0<=y and y<n)

def in_range_1x3(start_x, start_y):
    """
    1x3 크기의 격자가 nxn 격자 범위내에 있는지
    Args:
        start_x,start_y : 1x3 크기의 격자의 첫번째 칸
    """
    for k in range(3):
        if not in_range(start_x,start_y+k):
            return False
    return True

def is_overlap(start_x1, start_y1, start_x2, start_y2):
    """
    1x3 크기의 격자 2개가 겹치는지 확인한다
    두 개의 격자는 nxn 격자 범위내에 있어야 한다
    Args:
        start_x1,start_y1 : 첫번째 1x3 크기의 격자의 첫번째 칸
        start_x2,start_y2 : 두번째 1x3 크기의 격자의 첫번째 칸
    Returns:
        bools: 겹치면 True를 리턴한다
    """
    for i in range(3):
        y1 = start_y1 + i
        for j in range(3):
            y2 = start_y2 + j
            if start_x1==start_x2 and y1==y2:
                return True

    return False #안겹치는 경우


#=====메인실행부분=====
max_val = 0

#1x3 크기의 격자 2개를 서로 겹치지 않게 잡는다
for start_x1 in range(n):
    for start_y1 in range(n):
        for start_x2 in range(n):
            for start_y2 in range(n):
#                print(start_x1, start_y1, start_x2, start_y2)
#                print(is_overlap(start_x1, start_y1, start_x2, start_y2))
                if not is_overlap(start_x1, start_y1, start_x2, start_y2):
                    sum_val=0
#                    print(f"(x1,y1):({start_x1},{start_y1}), (x2,y2):({start_x2},{start_y2})")
                    #두 격자 모두 nxn 격자를 벗어나지 않는다면
                    #해당 범위 안애 있는 동전의 개수를 센다
                    if in_range_1x3(start_x1,start_y1) and in_range_1x3(start_x2, start_y2):
                        for k in range(3):
    #                        print(f"arr[{start_x1}][{start_y1+k}]:{arr[start_x1][start_y1+k]}")
    #                        print(f"arr[{start_x2}][{start_y2+k}]:{arr[start_x2][start_y2+k]}")
                            sum_val+=arr[start_x1][start_y1+k]+arr[start_x2][start_y2+k]
                    
                    #최대 동전의 수 업데이트
                    max_val = max(sum_val, max_val)

print(max_val) #최대 동전의 수 출력