pos = list(map(int, input().split()))

# Please write your code here.

# 이미 연속된 값인지 확인한다 -> 만약 그렇다면 print(0)
#1번째 값이 2번쨰 값과 3번째 값 사이에 들어가면 연속된 값이 되는지 확인한다
#  -> 만약 그렇다면 print(1)
#3번째 값이 1번쨰 값과 2번째 값 사이에 들어가면 연속된 값이 되는지 확인한다
#  -> 만약 그렇다면 print(1)
#둘다 연속된 값이 안나오면 print(2)

pos.sort()
v1, v2, v3 = pos[0], pos[1], pos[2]

if abs(v2-v1)==1 and abs(v3-v2)==1:
    print(0)
elif abs(v3-v2)==2 or abs(v2-v1)==2:
    print(1)
else:
    print(2)