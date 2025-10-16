n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
MAX_INT, MIN_INT = 100, 1
MAX_N = 100
min_val = (MAX_INT - MIN_INT) * MAX_N

for i in range(n):# 2배할 하나의 숫자를 고른다
    tmp = arr.copy()
    tmp[i]*=2
    for j in range(n): #제거할 하나의 숫자를 고른다
        remaining_list = [elem for k,elem in enumerate(tmp) if k!=j]
        sum_val = 0
        #남은 n-1개의 원소 중 인접한 숫자의 차의 합을 구한다
        for l in range(n-2):
            sum_val += abs(remaining_list[l]-remaining_list[l+1])
        
        min_val = min(sum_val, min_val)

print(min_val)