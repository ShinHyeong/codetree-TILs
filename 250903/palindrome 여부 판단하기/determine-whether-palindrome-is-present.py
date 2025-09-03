A = input()

# Please write your code here.
# palindrome 인지 판단하는 함수 : 문자열을 뒤집어도 동일한 문자열이어야함
def is_palindrome(_str):
    return _str == _str[::-1]

# yes, no 출력
if is_palindrome(A):
    print("Yes")
else:
    print("No")