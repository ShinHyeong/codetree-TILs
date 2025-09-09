m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
# [0, 1월, 2월, 3월, 4월, 5월, 6월, 7월, 8월, 9월, 10월, 11월, 12월] 에 해당하는 일수
nums_of_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

print((sum(nums_of_day[:m2])+d2)-(sum(nums_of_day[:m1])+d1)+1)