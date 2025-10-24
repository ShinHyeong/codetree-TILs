n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

max_cnt = 0
for a_tmp in range(1,n+1): #
    for b_tmp in range(1,n+1):
        cnt_tmp = 0
        for a,b in pairs:
            if (a_tmp==a and b_tmp==b) or (a_tmp==b and b_tmp==a):
                cnt_tmp+=1
        max_cnt = max(cnt_tmp,max_cnt)
print(max_cnt)