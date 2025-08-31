#a,b 정수 입력받기
#시작숫자:a 무한루프
    #종료조건:b초과 
    #종료조건x : 홀수인경우 *2 / 짝수인경우 +3
    #공백을 사이에두고 출력

a,b=tuple(map(int,input().split()))
while True:
    if a>b:
        break
    print(a,end=" ")
    if a%2==0:
        a = a+3
    else:
        a = a*2
    
    