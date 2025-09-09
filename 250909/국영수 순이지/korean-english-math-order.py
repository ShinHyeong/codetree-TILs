n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
#리스트에 학생별로 정보(튜플형태) 집어넣기
students = []
for i in range(n):
    students.append((name[i], korean[i], english[i], math[i]))

#우선순위(국 내림차순->영 내림차순->수 내림차순)로 정렬
students.sort(key=lambda s : (-s[1], -s[2], -s[3]))

#출력
for name,kor,eng,math in students:
    print(name,kor,eng,math)