n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
#a번 인덱스 원소까지 비교했을때 최댓값 반환하는 재귀함수 
def max_val(a):
    #종료조건
    if a==0:
        return arr[0]

    #일반화 : max_val(10) = max(arr[10], max_val(9))
    return max(arr[a], max_val(a-1))

#최댓값 출력
print(max_val(n-1))