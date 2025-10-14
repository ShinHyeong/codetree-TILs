n = int(input())
h = [int(input()) for _ in range(n)]

# Please write your code here.

max_val = 0
for k in range(1000+1):
    cnt=0 #해수면의 높이가 k일때의 빙산의 갯수
    #빙산의 갯수는 다음 빙산이 해수면에 잠길 때 카운팅된다
    for i in range(len(h)-1):
        if h[i]>k and h[i+1]<=k:
            cnt+=1
    if h[-1]>k:
        cnt+=1
    max_val = max(cnt,max_val)
print(max_val)