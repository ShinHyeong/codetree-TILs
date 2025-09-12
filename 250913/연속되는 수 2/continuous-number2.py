n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

# 연속해서 동일한 숫자가 나오는 횟수 저장하는 리스트
consecutive_counts = []

# 다른숫자가 나왔는지 구분하는 법 : i==0 이거나 직전원소가 다른경우(a[i]!=a[i-1]
cnt=1 #i==0 인 경우부터 시작이니까

for i in range(1,n):
    print("i=",i)
    if arr[i]!=arr[i-1]:#다른숫자가 나왔다
        consecutive_counts.append(cnt) #직전숫자 연속해서 나온 횟수를 리스트에 추가해줌
        cnt=0 #현재숫자 횟수 초기화
        cnt+=1 #현재숫자 횟수 카운트 시작
    else: #연속한다
        cnt+=1 #현재숫자 횟수 카운트

# 연속해서 동일한 숫자가 나오는 횟수 중 최댓값 출력
print(max(consecutive_counts)) 