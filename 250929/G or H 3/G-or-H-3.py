n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
# 0으로 채워진 n개의 칸을 만들고 해당위치에 점수를 하나씩 집어넣는다
arr = [0] * max(x)
for i in range(len(c)):
    pos = x[i]
    if c[i]=="H":
        arr[pos-1] = 2
    elif c[i]=="G":
        arr[pos-1] = 1

#연속한 k칸의 총합을 구한 후 
#최대점수인지 확인한다
max_val = 0
for start_idx in range(len(arr)-k+1): #start_idx는 0~len(arr)-k까지 가능하다
    sum_val = sum(arr[start_idx:start_idx+k+1]) #start_idx+0~(start_idx+k)의 합을 구한다
    max_val = max(sum_val, max_val)
#최대점수 출력
print(max_val)