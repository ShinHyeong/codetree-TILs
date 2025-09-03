n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

#값을 반환하지 않는 함수 사용
#매개변수 : 배열
#하나씩 돌면서
#짝수인 원소만 2로 나눠줌
def divideBy2(arr):
    for i in range(n):
        if arr[i]%2==0:
            arr[i] = arr[i]//2

#함수 호출 후
#공백을 사이로 두고 출력
divideBy2(arr)
for ele in arr:
    print(ele, end=' ')