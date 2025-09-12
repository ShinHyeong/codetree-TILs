n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
# 하나의 타일 (0:회색 / -1:흰색 / +1:검은색)
tiles = [0] * (1+100*1000*2)
curr_idx = len(tiles)//2

# 각 명령어 마다
for i in range(n):

    if dir[i]=="L": #왼쪽으로 이동
        # 한칸씩 이동하며 x[i]만큼 흰색으로 뒤집기
        for _ in range(x[i]): 
            tiles[curr_idx] = -1
            curr_idx -=1 #왼쪽으로 한칸씩 이동
        #각 명령이 끝난 후엔 마지막으로 뒤집은 타일 위치에 있어야함
        curr_idx += 1

    else: #오른쪽으로 이동
        # 한칸씩 이동하며 x[i]만큼 검은색으로 뒤집기
        for _ in range(x[i]): 
            tiles[curr_idx] = +1
            curr_idx +=1 #오른쪽으로 한칸씩 이동
        #각 명령이 끝난 후엔 마지막으로 뒤집은 타일 위치에 있어야함
        curr_idx -= 1

#흰색, 검은색 타일 수 각각 세고, 출력
cnt_w,cnt_b=0,0
for t in tiles:
    if t<0:
        cnt_w+=1
    if t>0:
        cnt_b+=1
print(cnt_w,cnt_b)