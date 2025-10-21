inp = [input() for _ in range(3)]

# Please write your code here.
def is_same2diff1(d1,d2,d3):
    return (d1==d2 and d1!=d3) or (d1==d3 and d1!=d2) or (d2==d3 and d2!=d1)

# 가로 / 세로 / 대각선으로 같은수2개 다른수1개 조합이 몇개?
ans=0

#가로로 검사
for i in range(3):
    if is_same2diff1(inp[i][0],inp[i][1],inp[i][2]):
        ans+=1

#세로로 검사
for j in range(3):
    if is_same2diff1(inp[0][j],inp[1][j],inp[2][j]):
        ans+=1

#대각선으로 검사
if is_same2diff1(inp[0][0],inp[1][1],inp[2][2]):
    ans+=1

if is_same2diff1(inp[0][2], inp[1][1], inp[2][0]):
    ans+=1

print(ans)