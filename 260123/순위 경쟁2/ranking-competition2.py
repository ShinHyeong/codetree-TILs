n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.

##요구사항 분석
# 게임점수가 바뀔때마다 명예전당에 1등만 올려줌
# 명예전당 조합 바뀐 횟수 출력

##예제 분석
# A B 명예전당 바뀐횟수
# 0 0 (A,B) 
# -1 0 (B) : +1
# -1 1 (B)
# 0 1 (B)
# 1 1 (A,B) : +1
# 1 3 (B) : +1
# 1 4 (B)
# 5 4 (A) : +1
# 총 바뀐 횟수 : 4

##로직 설정
#시뮬레이션 돌려서 일일이 세도 될것 같다 (N=100)
score_a, score_b, cnt = 0,0,0
curr_winner = "ab"
for i in range(n):
    prev_winner = curr_winner

    if c[i]=="A":
        score_a += s[i]
    else:
        score_b+=s[i]
    
    if score_a > score_b:
        curr_winner = "a" 
    elif score_b > score_a:
        curr_winner = "b"
    else:
        curr_winner = "ab"
    
    if curr_winner != prev_winner:
        cnt+=1
print(cnt)