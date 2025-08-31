#영문자 입력받기
s = input()
#5개의 문자열 초기화
arr = ["apple","banana","grape","blueberry","orange"]

cnt=0

#문자열 돌면서
#3번째나 네번째 문자와 일치하는지 확인
#그 문자열 출력하고
#cnt에 더하기
for x in arr:
    if s in x[2] or s in x[3]:
        print(x)
        cnt+=1

#마지막에 cnt 출력
print(cnt)