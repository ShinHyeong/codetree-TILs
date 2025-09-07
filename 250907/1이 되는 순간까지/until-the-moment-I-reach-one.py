N = int(input())

# Please write your code here.
# n이 짝수 -> 2로 나눈 몫
# n이 홀수 -> 3으로 나눈 몫 취하다가
# 값이 1이 되면 지금까지 진행한 횟수 구하는 재귀함수
def get_cnt(n):
    #종료 조건 : n==1
    if n==1:
        return 0

    if n%2==0:
        n //= 2
    else:
        n //= 3

    return get_cnt(n)+1

print(get_cnt(N))