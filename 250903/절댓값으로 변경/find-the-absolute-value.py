n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# 매개변수 : 배열
# 원소마다 절댓값을 씌워주는 함수 : 원소 하나씩 돌면서 0보다 작으면 양수로 바꿔줨 (*-1)
# 값을 반환하지 않는 함수 사용
def absolute(arr):
    for i in range(n): 
        if arr[i]<0:
            arr[i] *= (-1)
        
# 함수 호출
absolute(arr)
# 각 원소의 값 출력
for ele in arr:
    print(ele, end=" ")