n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
#리스트에 사람별로 정보(튜플) 집어넣기
users=[]
for i in range(n):
    users.append((name[i], height[i], weight[i]))

#키를 기준으로 오름차순 정렬
users.sort(key=lambda u : u[1])

#출력
for n,h,w in users:
    print(n,h,w)