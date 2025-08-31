#무한루프
    #하나씩 입력받기  
    #if 종료조건 ; ==25 -> Good 출력, 종료
    #else 종료x : <25 -> higher출력 / >25 -> lower출력 
    
while True:
    n = int(input())
    
    if n==25:
        print("Good")
        break
    
    if n<25:
        print("Higher")
    elif n>25:
        print("Lower")