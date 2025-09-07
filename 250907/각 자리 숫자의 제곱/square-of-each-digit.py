N = int(input())

# Please write your code here.
# 각 자리의 제곱의 합 구하는 재귀함수
def square_sum(n):
    # 종료조건 : n이 한자리 수 -> n<10
    if n<10:
        return n*n

    # 일반화 : f(1527) = f(152) + 7^2
    return square_sum(n//10) + (n%10)*(n%10)

print(square_sum(N))