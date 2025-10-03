abilities = list(map(int, input().split()))

# Please write your code here.
def get_diff(s1,s2):
    """
    두 합의 차를 리턴함
    """
    return abs(s1-s2)

#3명씩 팀 구성
min_val = 1000000
for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            sum1 = abilities[i]+abilities[j]+abilities[k]
            sum2 = sum(abilities) - sum1
            diff = get_diff(sum1, sum2)
            min_val = min(min_val, diff)
print(min_val)