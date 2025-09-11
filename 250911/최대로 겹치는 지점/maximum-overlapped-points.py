n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# offset 설정하기
offset = 0
for s in segments:
    if s[1]<0:
        offset = -s[1]
    if s[0]<0:
        offset = -s[0]

# 음수 지점을 포함하는 선분이 있을 수 있으니 양수 지점으로 업데이트
updated_segments = []
for s in segments:
    updated_segments.append((s[0]+offset,s[1]+offset))

# 업데이트한 선분 정보 리스트 하나씩 돌면서
# 겹치는 지점 구하기 -> x1부터 x2까지 +1 처리
checked = [0] * 100
for s in updated_segments:
    for i in range(s[0], s[1]+1):
        checked[i]+=1

# 최대로 겹치는 지점에서 몇개의 선분이 겹치는지 출력
print(max(checked))