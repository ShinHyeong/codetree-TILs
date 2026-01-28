n = int(input())
c, s = [], []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.
## 요구사항 분석
# 명예의 전당 변경횟수 출력

## 예제 분석
# A B C winner cnt
# 0 0 0
# -1 0 0 (B,C) +1
# -1 1 0 (B) +1
# -1 1 1 (B,C) +1
# 0 1 1 (B,C)
# 0 1 3 (C) +1
# 0 1 4 (C)
# 4 1 4 (A,C) +1
# 답 = 5

## 로직 설정
# 를 저장하고 바뀌면 cnt+1
cnt = 0
winner = "ABC"
curr = [0,0,0]
for i in range(n):
    if c[i]=="A":
        curr[0] += s[i]
    elif c[i]=="B":
        curr[1] += s[i]
    else: #c[i]=="C"
        curr[2] += s[i]

    curr_winner = ""
    max_val = max(curr)
    for j in range(3):
        if curr[j]==max_val:
            if j==0:
                curr_winner += "A"
            elif j==1:
                curr_winner += "B"
            else:
                curr_winner += "C"

    if winner != curr_winner: #명예의전당 리스트 변경여부 확인
        winner = curr_winner #명예의전당 리스트 업데이트 
        cnt += 1

print(cnt)