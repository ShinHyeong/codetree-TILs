n = int(input())
S = input()

# Please write your code here.
# c를 찾는다
# 다음 인덱스들 중에서 o를 찾는다
# 그 다음인덱스들 중에서 w를 찾는다

cnt=0
for i in range(n):
    if S[i]=="C":
        for j in range(i+1, n):
            if S[j]=="O":
                for k in range(j+1, n):
                    if S[k]=="W":
                        cnt+=1

# "cow" 조합이 몇 개인지
print(cnt)
