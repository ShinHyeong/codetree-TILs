n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.
# 우선순위에 따라 정렬 (키 내림차순 -> 몸무게 내림차순 -> 번호 오름차순)
students.sort(key=lambda s : (-s[0], -s[1], s[2]))

for h, w, n in students:
    print(h,w,n)