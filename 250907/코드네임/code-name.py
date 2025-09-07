MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
# 코드네임과 점수를 갖는 요원
class User:
    def __init__(self,codename,score):
        self.cn=codename
        self.score=score

# 각 사람의 정보를 담은 객체 5개 생성
users=[]
for i in range(5):
    users.append(User(codenames[i], scores[i]))

# 리스트 처음~끝까지 돌면서 가장 낮은 점수 가진 요원 찾기
min_score = 100
min_idx = 0
for i in range(5):
    if users[i].score < min_score:
        min_score = users[i].score
        min_idx = i

# 정보 출력
print(users[min_idx].cn, users[min_idx].score)