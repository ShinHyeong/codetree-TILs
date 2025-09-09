n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.
#리스트에 학생별로 정보(튜플형태) 집어넣기
students = []
for i in range(n):
    students.append((name[i], score1[i], score2[i], score3[i]))

#우선순위(총점 오름차순)로 정렬
students.sort(key=lambda s : (s[1]+s[2]+s[3]))

#출력
for name,s1,s2,s3 in students:
    print(name,s1,s2,s3)