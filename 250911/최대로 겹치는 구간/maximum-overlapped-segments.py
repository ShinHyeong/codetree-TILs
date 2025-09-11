n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 선분 정보 리스트 하나씩 돌면서 음수있는지 확인
# 음수 있다면 Offset 설정
offset = 0
for s in segments:
    if s[1] < 0:
        offset = -s[1]
    if s[0] < 0:
        offset = -s[0]
        
# 다 돌았으면 Offset 더해줘서 선분 정보 리스트 업데이트
updated_segments = []
for s in segments:
    updated_segments.append((s[0]+offset,s[1]+offset))

# x1과 x2는 최소 -100에서 최대 100까지 가능 -> 100+1+100칸
checked = [0] * (100+1+100)

# n개의 선분 표시 : 겹치는 구간(=시작점) 찾기니까 x1부터 x2-1까지에 +1 처리
for s in updated_segments:
    for i in range(s[0], s[1]):
        checked[i] += 1

#가장 많이 겹치는 구간에는 몇개의 선분이 겹치는지 출력
print(max(checked))