n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

max_cnt = 0
for a_tmp in range(1,n+1): #후보들을 만든다
    for b_tmp in range(1,n+1):
        cnt_tmp = 0 
        for a,b in pairs: #해당 후보가 pair를 만족하는 갯수를 구한다
            if (a_tmp==a and b_tmp==b) or (a_tmp==b and b_tmp==a):
                cnt_tmp+=1
        max_cnt = max(cnt_tmp,max_cnt) #그 해당 후보에 일치하는 갯수가 최댓값인지 확인한다 
print(max_cnt)