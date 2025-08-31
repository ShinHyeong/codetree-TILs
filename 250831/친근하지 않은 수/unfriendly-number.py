#n 입력받기
#1이상 n이하 돌면서
#친근 하면 넘기고 
#친근하지 않으면 개수 세고
#출력하기

n=int(input())
num=0
for i in range(1,n-1):
    if i%2==0 or i%3==0 or i%5==0:
        continue
    else:
        num+=1
print(num)