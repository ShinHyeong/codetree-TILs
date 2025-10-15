n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

# Please write your code here.
max_val = 0
for target in range(3): #조약돌을 넣을 종이컵 num
    cups = [False]*3
    cups[target] = True #조약돌을 넣는다
    score = 0

    #n번에 걸쳐 행동을 반복한다
    for i in range(n):
        a_idx, b_idx, c_idx = a[i]-1,b[i]-1,c[i]-1
        #a번 종이컵과 b번 종이컵을 교환한다
        tmp = cups[a_idx]
        cups[a_idx] = cups[b_idx]
        cups[b_idx] = tmp
        #c번 종이컵에 조약돌이 있는지 확인한다
        if cups[c_idx]:
            score+=1
    
    #점수가 최댓값인지 확인한다
    max_val = max(score, max_val)

print(max_val)