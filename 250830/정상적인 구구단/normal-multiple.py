n = int(input())

for i in range(1,n+1): #1단부터 n단까지
    for j in range(1,n): #1부터 n-1까지는 줄바꿈없이 ,으로 끝내기
        print(f"{i} * {j} = {i*j}", end=", ")
    print(f"{i} * {n} = {i*n}")  #마지막 수는 줄바꿈 o
