n, m, p = map(int, input().split()) #인원, 메세지수, 확인필요한메세지번호
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages] #누가올린메세지?
u = [int(msg[1]) for msg in messages] #읽지않은 사람수

# Please write your code here.

###예시 분석###
# 총 6명 : A B C D E F
# D 0명이 안읽었다 
# C 1명이 안읽었다 확실:C,A,B,F / 후보:D,E
# B 2명이 안읽었다 확실:B,A,F / 후보:C,D,E
# B 2명이 안읽었다 
# A 2명이 안읽었다 확실:A,F / 후보:B,C,D,E
# F 4명이 안읽었다 확실:F / 후보:A,B,C,D,E

# 만약 u[i] == u[i+1](연속된 인덱스)라면 안읽은 사람 리스트의 구성도 똑같다

###조건 분석###
#인원은 최소1에서 최대26명까지 가능한 톡방
#안읽은 사람 수는 메세지수보다 적다
#메세지수는 최소1에서 최대 100개

###로직### 후보를 찾는다. 
# 만약 u[i] == u[i+1](연속된 인덱스)라면 안읽은 사람 리스트의 구성도 똑같다.
#   예를 들어, B 2 A 2 F 2 이라면(u[0]==u[2]) p=1와 p=3 후보 리스트 구성도 똑같으므로 p=1으로 치환해서 구한다
#확실 -> 자기자신 + 그 뒤로 메세지 보낸 사람들
#후보 = 전체사람리스트 - 확실리스트 

allUserList = [chr(i) for i in range(65,65+n)]

target_idx = p-1

while target_idx >= 0 and u[target_idx] == u[target_idx-1]: 
    target_idx -= 1

readUserSet = set() #확실히 읽은 사람
for i in range(m):
    if i < target_idx:
        continue
    readUserSet.add(c[i])

answer = [] #안읽은사람 후보
for user in allUserList:
    if user not in readUserSet:
        answer.append(user)
answer.sort()

if u[target_idx]==0:
    print()
else:
    for ele in answer:
        print(ele,end=" ")
