n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
# 리스트에 사람정보 담기
students = []
for i in range(len(name)):
    students.append((name[i], height[i], weight[i]))

# 우선순위에 따라 정렬 (이름 오름차순)
students.sort(key=lambda s : s[0])

# 리스트 돌면서 출력
print("name")
for n,h,w in students:
    print(n,h,w)

print()

# 우선순위에 따라 정렬 (키 내림차순)
students.sort(key=lambda s : -s[1])

# 리스트 돌면서 출력
print("height")
for n,h,w in students:
    print(n,h,w)
