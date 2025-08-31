#입력받고
#리스트에서 역순으로 하나씩 꺼내서
#짝수인지 확인하고
#출력합니다.
n=int(input())
arr = list(map(int, input().split()))
for i in range(n-1, -1, -1):
    if arr[i]%2==0:
        print(arr[i],end=" ")