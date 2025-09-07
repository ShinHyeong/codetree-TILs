a, b, c = map(int, input().split())

# Please write your code here.
#각 자리 수의 합 반환하는 재귀함수 
def sum_digit(n):
    #종료조건 : n이 한자리 수
    if n<10:
        return n

    #일반화 : sum_digit(18539) = sum_digit(1853)+9
    return sum_digit(n//10) + (n%10)

#각 자리 수의 합 출력
print(sum_digit(a*b*c))