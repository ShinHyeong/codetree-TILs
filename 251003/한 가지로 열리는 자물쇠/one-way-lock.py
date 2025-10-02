N = int(input())
a, b, c = map(int, input().split())

# Please write your code here.
cnt=0
for i in range(1,N+1): #첫번째 자리의 숫자 : 1~N
    for j in range(1,N+1): #두번째 자리의 숫자 : 1~N
        for k in range(1,N+1): #세번째 자리의 숫자 : 1~N
            if abs(a-i) <= 2 or abs(b-j)<=2 or abs(c-k)<=2: #한자리라도 주어진 조합과 거리가 2이내이면 열린다
                cnt+=1 #열리게 되는 횟수
print(cnt)