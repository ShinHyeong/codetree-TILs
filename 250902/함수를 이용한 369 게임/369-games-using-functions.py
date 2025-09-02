a, b = map(int, input().split())

# Please write your code here.
# [조건 1 : 3의 배수인지] 검사하는 함수
def multiple_3(x):
    return x%3==0

# [조건 2 : 숫자에 3,6,9 있어야함] 검사하는 함수
def contains_369(x):
    #계속 10으로 나눠주며 
    #일의자리 조사함
    while x>0:
        if (x%10==3 or x%10==6 or x%10==9): #일의자리 조사
            return True
        x //= 10
    
    return False

# a~b까지 돌면서
# 조건 1 : 3의 배수인지
# 조건 2 : 숫자에 3,6,9 있어야함
# 조건 1 또는 조건 2를 만족해야 함
cnt=0
for x in range(a,b+1):
    if multiple_3(x) or contains_369(x):
        cnt+=1
print(cnt)