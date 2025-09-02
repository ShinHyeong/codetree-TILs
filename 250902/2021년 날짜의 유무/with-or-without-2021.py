M, D = map(int, input().split())

# Please write your code here.

##y/m/d 날짜가 존재하는지 확인하는 함수 작성
#m: 1,3,5,7,8,10,12-> d: 1~31
#m: 4,6,9,11 -> d: 1~30
def is_valid_date(M,D):
    if 1<=M<=7:
        if M==2:
            return 1<=D<=28 #Feb D.: 1~28

        if M%2!=0: #odd M. : 1,3,5,7
            return 1<=D<=31
        else: #even M. : 2,4,6
            return 1<=D<=30
    else: #8<=M<=12
        if M%2!=0: #odd M. : 9,11
            return 1<=D<=30
        else: #even M : 8,10,12
            return 1<=D<=31

if is_valid_date(M,D):
    print("Yes")
else:
    print("No")