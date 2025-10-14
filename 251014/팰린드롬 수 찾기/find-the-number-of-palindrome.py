X, Y = map(int, input().split())

# Please write your code here.
#자릿수 리턴하는 함수
def get_num(num):
    digits=[]
    while num>=10:
        digits.append(num%10)
        num//=10
    digits.append(num%10)
    return digits[::-1]

#거꾸로 읽어도 같은수인지 판단
def is_palindrome(num):
    digits = get_num(num)
    if digits == digits[::-1]:
        return True
    return False

cnt=0
for num in range(X,Y+1):
    if is_palindrome(num):
        cnt+=1
print(cnt)