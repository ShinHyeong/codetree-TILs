a,b=map(int,input().split())

#3,6,9 중 하나가 들어 있는지
def is_there_3_6_9(n):
    # 계속 10으로 나눠주며
    # 일의 자리를 조사합니다.
    while( n > 0):
        if n%10==3 or n%10==6 or n%10==9:
            return True
        n//=10
    
    return False

#그 숫자가 3의 배수인지
def is_3(n):
    return n%3==0

cnt=0
for i in range(a,b+1):
    if is_there_3_6_9(i) or is_3(i):
        cnt+=1
print(cnt)