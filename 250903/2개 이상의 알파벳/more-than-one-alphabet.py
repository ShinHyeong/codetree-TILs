A = input()

# Please write your code here.
# 서로 다른 알파벳 수를 출력하는 함수
def cnt_different(_str):
    cnt=0

    for i in range(len(A)-1): #i : 0~끝-1
        for j in range(i+1,len(A)): # j: i+1~끝
            if A[i]!=A[j]:
                cnt+=1

    return cnt


#서로 다른 알파벳 수가 2개이상인지 판단 후
# Yes,No 출력
if cnt_different(A)>=2:
    print("Yes")
else:
    print("No")