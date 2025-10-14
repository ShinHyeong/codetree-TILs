n = int(input())
h = [int(input()) for _ in range(n)]

# Please write your code here.
#해수면의 높이 k가 주어지면, n개의 빙산이 잠기는지 안잠기는지 리스트로 반환
def get_sinks(k):
    sinks = []
    for i in range(len(h)):
        if h[i]<=k:
            sinks.append(True)
        else:
            sinks.append(False)
    return sinks

max_val = 0
for k in range(1000+1):
    cnt=0 #해수면의 높이가 k일때의 빙산의 갯수
    #빙산의 갯수는 다음 빙산이 해수면에 잠길 때 카운팅된다
    sinks = get_sinks(k)
    for i in range(len(sinks)-1):
            if sinks[i]==False and sinks[i+1]==True:
                cnt+=1
    if sinks[-1]==False:
        cnt+=1 
    max_val = max(cnt,max_val)
print(max_val)