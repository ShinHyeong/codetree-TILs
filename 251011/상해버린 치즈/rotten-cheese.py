N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

# Please write your code here.
#아픈사람 수 최댓값 = 필요한 약의 갯수 최댓값
max_val = 0

#치즈별로 먹은 시간을 확인한다
#만약 아픈 사람이 발생한 시각보다 이전이라면 상한 치즈일 수 있음
#상한 치즈 후보이므로 해당 치즈를 먹은 다른 시람 또한 아픈 걸로 처리
for i in range(M):
    bad = False
    cnt = 0

    #상한 치즈 후보인지 확인
    for j in range(S):
        if sick_t[j] < t[i]:
            bad = True
            break
    
    #해당 치즈를 먹은 다른 사람 수 구하기
    for k in range(D):
        if m[k]==m[i]:
            cnt+=1
    
    #최대로 아픈 사람 수인지 확인
    max_val = max(cnt,max_val)

print(max_val)