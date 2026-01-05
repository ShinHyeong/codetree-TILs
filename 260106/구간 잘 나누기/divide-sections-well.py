n, m = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.

#만약 완전탐색으로 접근한다면 .. 

#구간을 나눈다
#최댓값 구한다
#최소인지 확인한다
#이 과정을 모든 경우에 대해 반복한다
#ㄴ하지만 모든 과정을 다 하려면 반복문 m번 써야함..

#더 작게 최댓값이 나오도록 구간을 나누려면 골고루 나누는게 중요하다
num_ele = n//m
sum_list = [0]*m
j=0
for i in range(m):
    sum_list[i] = sum(a[j:j+num_ele])
    j+=num_ele
print(max(sum_list))
