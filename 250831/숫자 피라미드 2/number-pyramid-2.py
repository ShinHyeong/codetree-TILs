#정수N받기
# 외부 : 1~n 줄
# 내부 : 각 줄마다 행번호만큼 숫자 개수를 출력
#내부원소는 1씩 증가 

n=int(input())
start=1
for i in range(1,n+1):
    for _ in range(1,i+1):
        print(start, end=" ")
        start+=1
    print()