n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

# Please write your code here.
#주어진 직선을 표시한다
MAX_INT = 100
arr = [0] * (MAX_INT+1)
for i in range(len(l)):
    left,right = l[i], r[i]
    for k in range(left, right+1):
        arr[k] += 1

def delete_line(arr, line_idx):
    left, right = l[line_idx], r[line_idx]
    for i in range(left, right+1):
        arr[i] -= 1

#서로 다른 선분 3개를 고른다
#제거해본다
#남은 n-3개의 선분끼리 서로 겹치지 않는지 확인한다
    #겹치지 않는다면 카운팅
cnt=0 
for l1_idx in range(n): #서로 다른 선분 3개 고르기
    for l2_idx in range(l1_idx+1, n):
        for l3_idx in range(l2_idx+1, n):
            #제거해본다
            arr_cpy = arr.copy()
            delete_line(arr_cpy, l1_idx)
            delete_line(arr_cpy, l2_idx)
            delete_line(arr_cpy, l3_idx)

            overlap = False
            
            for i in range(len(arr_cpy)):
                if arr_cpy[i]>1: #한번이라도 겹치면 True
                    overlap = True
            if overlap == False:
                #print(l1_idx, l2_idx, l3_idx, arr[0:10])
                cnt+=1
print(cnt)