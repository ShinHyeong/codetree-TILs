Y, M, D = map(int, input().split())

# Please write your code here.
#윤년(2월이 29일까지 있는 조건) 확인 함수 작성
def is_leapYear(Y):
    if Y%4==0: #4의 배수 -> 윤년 o
        if Y%100==0:
            if Y%400==0: #(4의 배수+100의 배수+400의 배수) -> 윤년 o
                return True
            else: #(4의 배수+100의 배수)o (400의 배수)x -> 윤년 x
                return False
        else: #4의 배수 o +100의 배수 x -> 윤년  
            return True
    else: #4의 배수 x -> 윤년 x
        return False


#계절에 따라 판별시키는 함수 작성
def season(M):
    if 3<=M<=5:
        return "Spring"
    if 6<=M<=8:
        return "Summer"
    if 9<=M<=11:
        return "Fall"
    if M==12 or 1<=M<=2:
        return "Winter"

##(2월 제외)y/m/d 날짜가 존재하는지 확인하는 함수 작성
#m: 1,3,5,7,8,10,12-> d: 1~31
#m: 4,6,9,11 -> d: 1~30
def is_valid_date(M,D):
    if 1<=M<=7:
        if M%2!=0: #odd M. : 1,3,5,7
            return 1<=D<=31
        else: #even M. : 2,4,6
            return 1<=D<=30
    else: #8<=M<=12
        if M%2!=0: #odd M. : 9,11
            return 1<=D<=30
        else: #even M : 8,10,12
            return 1<=D<=31

## (2월 제외)y/m/d 날짜가 존재하는지 확인
if is_valid_date(M,D):
##1. 존재한다면 : 월에 따라 계절 판별 후 출력
    if M==2:  #1) 2월의 경우 한번더 검토 -> y가 윤년인지 검사
        if is_leapYear(Y): #윤년이라면 D:1~29인지 검사 -> 맞으면 계절 출력
            #print("is leap year")
            if 1<=D<=29:
                print(season(M))
            else:
                print(-1)
        else: #윤년이 아니라면 D:1~28인지 검사 -> 맞으면 계절 출력
            #print("not leap year")
            if 1<=D<=28:
                print(season(M))
            else:
                print(-1)
#2) 2월이 아닌경우 계절 출력
    else:
        #print("not Feb, but valid date")
        print(season(M))

##2. 해당날짜 자체가 존재하지 않는다면 : -1 출력
else:
    #print("invalid date")
    print(-1)
