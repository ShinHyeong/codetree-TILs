n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

## 요구사항 분석 ##
# 맨앞 숫자를 수열중간에 집어넣는다
# 최소 몇 번 반복해야 오름차순 정렬이 되는가


## 로직 설정 ##
# 맨뒤에서 봤을 때 이미 오름차순으로 잘 정리된 곳은 건들지 않는다
# 35 50 4 39 54 32 20 53 29 18 55 28 40 44 48 25 21 5 9 14 33 3 16 38 31 23 15 60 27 49 11 51 46 52 30 45 1 6 36 43 24 7 58 56 42 2 8 10 12 13 17 19 22 26 34 37 41 47 57 59
# 이 수열에서 [2 8 10 12 13 17 19 22 26 34 37 41 47 57 59] 이 부분은 건들지 않는다. 그 앞 부분 수들의 정렬이 이상하니까 옮겨준다.


# 이미 잘 정리된 인덱스 시작점 찾기
good_start_idx = -1
for i in range(n-1,-1,-1):
    if sequence[i]<sequence[i-1]:
        good_start_idx = i
        break

# sequence[0:good_start_idx-1]는 어차피 이동해야할 숫자
# 그 숫자의 갯수를 센다
print(good_start_idx)