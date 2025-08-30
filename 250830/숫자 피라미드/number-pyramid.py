n = int(input())

##1단~n단까지 출력
for i in range(1, n+1): #1단~
    for _ in range(i): # i를 각 숫자만큼 출력 (줄바꿈없이 스페이스로 끝)
        print(f"{i}", end=" ")
    print() #줄바꿈