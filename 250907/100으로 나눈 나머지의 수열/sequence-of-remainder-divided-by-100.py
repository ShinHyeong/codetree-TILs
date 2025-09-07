N = int(input())

# Please write your code here.
# 수열의 n번째 값 구하는 재귀함수
def result(n):
    #종료조건
    if n==1:
        return 2
    if n==2:
        return 4

    # 2, 4, (a1*a2)%100, (a2*a3)%100, ....
    #일반화 : result(3) = (result(1)*result(2))%100
    return (result(n-1)*result(n-2))%100

# 재귀함수 값 출력
print(result(N))