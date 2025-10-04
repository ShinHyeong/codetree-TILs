N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
def dist(d1, d2):
    return min(abs(d1-d2), N-max(d1,d2)+min(d1,d2))

#1부터 N까지의 숫자를 이용해 총 3자리 만들기
#1번째 조합에 대해 각자리 숫자와의 거리를 구하고
    #모든 자리 숫자에 대해 거리가 2 이내면 True로 설정한다
#2번째 조합에 대해 각자리 숫자와의 거리를 구하고
    #모든 자리 숫자에 대해 거리가 2 이내면 True로 설정한다
#둘중 하나의 조합이 True이면 카운팅한다
cnt=0
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            isOpen1 = False
            isOpen2 = False
            if dist(a1,i)<=2 and dist(b1,j)<=2 and dist(c1,k)<=2:
                isOpen1 = True
            if dist(a2,i)<=2 and dist(b2,j)<=2 and dist(c2,k)<=2:
                isOpen2 = True
            if isOpen1 or isOpen2:
                cnt+=1
print(cnt)