n = int(input())
arr = list(input().split())

# Please write your code here.

##예제 분석
# ADBC
# ABDC -> +1
# ABCD -> +1
# 총 2회

##요구사항 분석
# 목표 : N명 알파벳순으로 줄세우기 (1<=N<=26)
# 제약 : 인접한 두 사람만 순서변경 가능
# 변경횟수 최소 구하기

##로직설정
# B가 A다음에 올 때까지 순서 바꾸기
# C가 B다음에 올 때까지 순서 바꾸기

cnt=0
for i in range(n-1):
    if arr[i]>arr[i+1]:
        tmp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = tmp
        cnt+=1
print(cnt)