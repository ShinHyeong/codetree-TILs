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

#로직 : 정렬된 결과 나올때까지 처음부터 끝까지 인접 순서바꾸기 반복
cnt=0
sorted_list = sorted(arr)
while arr!=sorted_list:
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            cnt+=1
            #print(arr)
print(cnt)