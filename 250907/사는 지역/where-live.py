n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
#사람 자료 저장하는 클래스
class User:
    def __init__(self, name, street_address, region):
        self.name = name
        self.addr = street_address
        self.city = region

#n개의 객체 저장하는 리스트
users=[]
for i in range(n):
    users.append(User(name[i], street_address[i], region[i]))

#리스트 처음~끝까지 사전순으로 이름이 가장 느린 사람의 자료 찾기 
target_idx = 0
for i in range(n):
    if users[i].name > users[target_idx].name:
        target_idx = i

#그 사람 인덱스를 기반으로 정보 출력
print("name",users[target_idx].name)
print("addr",users[target_idx].addr)
print("city",users[target_idx].city)