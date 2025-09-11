n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.

# 튜플 (x, dir)로 이동 정보 다시 담기
movements = []
for i in range(n):
    movements.append((x[i], dir[i]))
# 지나간 구간의 최소 시나리오 : 위치 0에서 -10씩 100번의 명령
# 지나간 구간의 최대 시나리오 : 위치 0에서 +10씩 100번의 명령
# ex.-2 -1 0 1 2 -> 총 5칸 가운데인덱스 : 2 = 5//2
checked = [0] * (10*100 + 10*100 +1)
checked_mid_idx = (10*100 + 10*100 +1)//2

# mid_index에서 시작해서 구간(=시작점) 표시 -> x1부터 x2-1까지 +1 처리
curr_idx = checked_mid_idx
for m in movements:
    if m[1]=="L": #왼쪽으로 이동한다면
        #curr_idx에서 -x만큼 이동 -> curr_idx-x부터 curr_idx-1까지 +1처리
        for i in range(curr_idx-m[0], curr_idx):
            checked[i] += 1
        # curr_idx(현재지점) 업데이트
        curr_idx = curr_idx - m[0]

    else: #오른쪽으로 이동한다면
        #curr_idx에서 +x만큼 이동 -> curr_idx부터 curr_idx+x-1까지 +1처리
        for i in range(curr_idx, curr_idx+m[0]):
            checked[i] += 1
        # curr_idx(현재지점) 업데이트
        curr_idx = curr_idx + m[0]

# 2번이상 지나간 영역의 크기 출력 : 2번이상 영역 구하고 그 개수 출력
cnt=0
for c in checked:
    if c>=2:
        cnt+=1
print(cnt)