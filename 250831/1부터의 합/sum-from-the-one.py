#정수n 입력받기
#1~100까지 1씩 증가하며 돌면서
#합이 n이상이 되는 즉시
#더했던 수 출력 -> 종료

n=int(input())
sum_val = 0
for i in range(1,100+1):
    sum_val += i
    if sum_val >=n:
        print(i)
        break