m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

# [0, 1월, 2월, 3월, 4월, 5월, 6월, 7월, 8월, 9월, 10월, 11월, 12월] 에 해당하는 일수
nums_of_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

#m1/d1~m2/d2까지 총 며칠이 되는지 구하고 
elapsed_day = (sum(nums_of_day[:m2])+d2) - (sum(nums_of_day[:m1])+d1) + 1

#현재 요일 = 월요일
curr_idx = 1
target_idx = day_of_week.index(A)

# target요일(=a) 등장횟수 초기화
target_cnt = 0

# m1/d1~m2/d2 까지의 총 일수동안
for _ in range(elapsed_day):

#현재요일에서 하나씩 이동하는데
    curr_idx += 1
#단, 현재요일 인덱스가 7이되면 0으로 초기화해줌    
    if curr_idx==7:
        curr_idx=0
# target요일이 등장할 때마다 등장횟수+1
    if curr_idx==target_idx:
        target_cnt +=1

# target요일(=a) 등장횟수 출력
print(target_cnt)