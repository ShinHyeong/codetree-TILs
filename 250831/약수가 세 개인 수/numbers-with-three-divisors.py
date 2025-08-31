start, end = map(int, input().split())

# Please write your code here.
#start~end 크기의 정수를 하나씩 돌면서
#약수가 3개인지 검사 : 1부터 n까지 하나씩 나눠보고 나머지가 0인 개수세기 (divisor_cnt)
#cnt+=1
#cnt 출력

cnt=0

for x in range(start,end+1):
    divisor_cnt=0
    for divisor in range(1,x+1):
        if x%divisor==0:
            divisor_cnt+=1
    if divisor_cnt==0:
        cnt+=1
print(cnt)