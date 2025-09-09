m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
# [0, 1월, 2월, 3월, 4월, 5월, 6월, 7월, 8월, 9월, 10월, 11월, 12월] 에 해당하는 일수
nums_of_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

day_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
#m1/d1에서 며칠이 지나야 m2/d2 되는지 구하고 
elapsed_day = (sum(nums_of_day[:m2])+d2) - (sum(nums_of_day[:m1])+d1)
# 5/4과 5/3라고 가정했을 때 elasped_day=-1
#현재 요일 인덱스
curr_idx = 1

#만약 흐른시간이 음수면 현재요일인덱스-1 하면서 현재요일에서 하나씩 차례로 앞으로 이동한다
#단, 현재요일인덱스-1의 결과가 -1이면 6으로 초기화시킴
if elapsed_day<0:
    for i in range(-elapsed_day):
        curr_idx-=1
        if curr_idx==-1:
            curr_idx=6
#만약 흐른시간이 0이나 양수면 현재요일인덱스+1 하면서 현재요일에서 하나씩 차례로 뒤로 이동한다 
#단, 현재요일인덱스+1의 결과가 7이면 0으로 초기화시킴
else:
    for i in range(elapsed_day):
        curr_idx+=1
        if curr_idx == 7:
            curr_idx=0


print(day_of_week[curr_idx])