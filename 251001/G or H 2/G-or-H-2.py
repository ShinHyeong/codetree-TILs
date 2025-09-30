n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
def isOnlyOneAlpha(start,end):
    """
    오로지 G 또는 H로만 이루어져있는지 확인하는 함수
    Args:
        start : 사람이 있는 시작 구간
        end : 사람이 있는 종료 구간
    """
    element=arr[start]
    for i in range(start+1,end+1):
        if arr[i] == 0:
            continue
        if arr[i]!=element:
            return False
    return True
    
def isSameCnt(start,end):
    """
    G와 H가 정확히 같은 개수로 이루어져있는지 확인하는 함수
    Args:
        start : 사람이 있는 시작 구간
        end : 사람이 있는 종료 구간
    """
    g_cnt, h_cnt = 0,0
    for i in range(start,end+1):
        if arr[i]==1:
            g_cnt+=1
        elif arr[i]==2:
            h_cnt+=1
    if g_cnt==0 and h_cnt==0:
        return False
    return g_cnt==h_cnt

#===== 메인 로직 =====
arr = [0]*101 #위치 : 0~100

#해당위치에 매칭되는 값 집어넣기 (G->1, H->2)
for i in range(len(pos)):
    position = pos[i]
    if alpha[i] == "G":
        arr[position] = 1
    elif alpha[i] == "H":
        arr[position] = 2

max_size = 0
#사람이 있어야만 start,end이 성립된다
for start in range(len(arr)):
    if arr[start] == 0:
        continue
    for end in range(start, len(arr)):
        if arr[end] == 0:
            continue
        if isOnlyOneAlpha(start,end) or isSameCnt(start,end):
            #print(f"({start}, {end})")
            size = end-start
            max_size = max(size, max_size)
print(max_size)