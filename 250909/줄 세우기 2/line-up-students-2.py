n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
#student = (키, 몸무게, 번호)
#우선순위로 정렬 (키 오름차순->몸무게 내림차순)
students.sort(key=lambda s : (s[0], -s[1]))

#정렬후 키, 몸무게, 번호 출력
for h,w,n in students:
    print(h,w,n)