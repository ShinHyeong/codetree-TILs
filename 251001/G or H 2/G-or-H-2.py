n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.\
#===== 메인 로직 =====
arr = [0]*101 #위치 : 0~100

#해당위치에 매칭되는 값 집어넣기 (G->1, H->2)
for i in range(len(pos)):
    position = pos[i]
    arr[position] = 1 if alpha[i]=="G" else 2

max_size = 0
for start in range(len(arr)):
    for end in range(start, len(arr)):
        #사람이 있어야만 start,end이 성립된다
        if arr[start]==0 or arr[end] == 0:
            continue
        
        g_cnt, h_cnt = 0,0
        for i in range(start,end+1):
            if arr[i]==1:
                g_cnt+=1
            elif arr[i]==2:
                h_cnt+=1
        
        if g_cnt==0 or h_cnt==0 or g_cnt==h_cnt:
            size = end-start
            max_size = max(size, max_size)
print(max_size)