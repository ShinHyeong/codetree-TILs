n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# 중앙값 출력하는 함수
def get_mid(i):
    sample = arr[:i+1]
    # ex. 5개의 원소 0 1 2 3 4-> index 2
    return sorted(sample)[len(sample)//2]

# 순서대로 정수를 읽다가
# 홀수번쨰 원소이면
# 지금까지 입력 받은 값의 중앙값 출력 (오름차순으로 정렬했을 때 가장 중앙에 위치한값 출력)
for i in range(n):
    if i%2==0:
        print(get_mid(i),end=' ')
        