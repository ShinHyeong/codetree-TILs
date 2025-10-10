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
for cheese_idx in range(M+1): #치즈별로
    bad_condition1,bad_condition2 = False, False
    cnt = 0

    #상한 치즈 후보인지 확인

    # 조건1:해당치즈 먹은 시각 < 환자 발생한 시각
    for i in range(D):
        for j in range(S):
            if m[i]==cheese_idx: #치즈먹은기록에서 해당치즈먹은 시각을 찾고
                if t[i] < sick_t[j]:
                    bad_condition1 = True
                    break
    
    #조건2: 아픈사람 모두가 해당치즈를 먹었다
    for sick_idx in range(S): #아픈사람이 해당치즈를 먹었는지 치즈먹은기록에서 확인한다
        if not (sick_p[sick_idx] in p): #아픈사람 한 사람이라도 해당 치즈를 먹지 않으면 이 치즈는 상한 치즈가 아니다
            bad_condition2=False
            break            
        bad_condition2=True #아픈사람 모두 해당 치즈를 먹었다는 뜻

    bad = bad_condition1 and bad_condition2 #결론 : 조건1과 조건2를 만족하면 상한치즈이다

    if bad == False: #상한치즈가 아니라면 카운팅하지 않는다
        continue

    sick_list = []
    for k in range(D): #기록을 하나씩 보는데
        if m[k]==cheese_idx: #상한 치즈를 먹은 사람이라면
            if p[k] in sick_list: #단, 이미 카운팅된 사람은 세지않음
                continue
            sick_list.append(p[k]) #카운팅
    
    #최대로 아픈 사람 수인지 확인
    max_val = max(len(sick_list),max_val)

print(max_val)