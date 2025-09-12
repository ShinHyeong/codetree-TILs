n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

# 흰색과 검은색으로 각각 2번이상 칠해지면 회색 -> 각 타일당 흰색과 검은색 몇번 칠해졌는지 정보 저장하기
# 게다가 더이상 바뀌지 않음 -> 색 확인하고 만약 회색이면 조건문 넣기
# 각 타일 정보를 객체로 설정
class Tile:
    def __init__(self, color, cnt_w, cnt_b):
        self.curr = color #현재 칠해진 색(흰/검/회)
        self.cnt_w = cnt_w #흰색이 몇번 칠해졌는지
        self.cnt_b = cnt_b #검은색이 몇번 칠해졌는지

# 타일들 초기화 : 타일 한칸을 수직선 상 각 지점이라고 치면, 가장 작은 수를 나타내는 지점은 -100*1000 / 가장 큰 수를 나타내는 지점은 +100*1000
tiles = [Tile("", 0, 0) for _ in range(1+100*1000*2)] 

# 현재 타일 위치 0으로 설정
curr_idx = len(tiles)//2


# 현재색깔==회색 인지 확인
def is_grey(t):
    return t.curr=="g"

# 회색으로 칠해야할 조건에 해당인지 체크 : 흰색과 검은색으로 각각 2번이상 칠해지면 회색
def to_color_grey(t):
    return t.cnt_w>=2 and t.cnt_b>=2

#각 명령어 돌면서 한 칸씩 색칠
# 규칙1 - 왼쪽으로 이동 : 현재위치타일 포함해서 총 x칸의 타일을 흰색으로 연속해서 색칠
# 규칙2 - 오른쪽으로 이동 : 현재위치타일 포함해서 총 x칸의 타일을 검은색으로 연속해서 색칠
# 규칙3 - 각 명령이후엔 마지막으로 칠한 타일 위치에 있음
for i in range(n):
    #print("색칠 전", curr_idx, tiles[curr_idx].curr)
    if dir[i]=="L": #왼쪽 이동
        #현재위치타일 포함해서 총 x칸의 타일을 한칸씩 검사하면서 색칠
        for _ in range(x[i]):
            # 1) 현재색깔이 회색인지 체크 후 만약 그렇다면 색칠 안 하고 (회색은 더이상 바뀌지 않음)
            if not is_grey(tiles[curr_idx]):
                #현재색깔이 회색이 아니라면 현재위치타일 포함해서 총 x칸의 타일을 흰색으로 연속해서 색칠                
                tiles[curr_idx].curr = "w"
                tiles[curr_idx].cnt_w += 1
                # 만약 흰색으로 색칠했는데 회색으로 칠해야할 조건에 해당한다면 현재색깔=회색 처리 / 아니라면 현재색깔=흰색 처리
                tiles[curr_idx].curr="g" if to_color_grey(tiles[curr_idx]) else "w"
            
            #print("색칠 후", curr_idx, tiles[curr_idx].curr)
            # 2) 다음칸으로 위치 옮기기
            curr_idx -= 1
        #각 명령이후엔 마지막으로 칠한 타일 위치에 있음
        curr_idx += 1

    else: #오른쪽 이동
        #현재위치타일 포함해서 총 x칸의 타일을 한칸씩 검사하면서 색칠
        for _ in range(x[i]):
            # 1) 현재색깔이 회색인지 체크 후 만약 그렇다면 색칠 안 하고 (회색은 더이상 바뀌지 않음)
            if not is_grey(tiles[curr_idx]):
                #현재색깔이 회색이 아니라면 현재위치타일 포함해서 총 x칸의 타일을 검은색으로 연속해서 색칠                
                tiles[curr_idx].curr = "b"
                tiles[curr_idx].cnt_b += 1
                # 만약 흰색으로 색칠했는데 회색으로 칠해야할 조건에 해당한다면 현재색깔=회색 처리 / 아니라면 현재색깔=검은색 처리
                tiles[curr_idx].curr="g" if to_color_grey(tiles[curr_idx]) else "b"
            
            #print("색칠 후", curr_idx, tiles[curr_idx].curr)
            # 2) 다음칸으로 위치 옮기기
            curr_idx += 1
        #각 명령이후엔 마지막으로 칠한 타일 위치에 있음
        curr_idx -= 1


# 현재 타일 색이 무슨 색인지 확인 한 후 각 색깔별 타일 갯수 세기
w, b, g = 0,0,0
for t in tiles:
    if t.curr == "w":
        w+=1
    if t.curr == "b":
        b+=1
    if t.curr == "g":
        g+=1

# 공백을 사이에 두고 흰/검/회 타일수 출력
print(w,b,g)