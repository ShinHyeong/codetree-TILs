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

#상한 치즈 후보인지 확인 : 아픈사람 모두가 해당치즈를 아프기 전에 먹었나?
def is_bad(cheese_idx):
    for i in range(S): #아픈사람에 대해
        sick_idx = sick_p[i]
        for j in range(D): #치즈먹은기록에서 아픈사람이 해당치즈를 아프기전에 먹었는지 체크한다 
            if p[j]==sick_idx and m[j]==cheese_idx:
                if t[j]>=sick_t[i]: #한명이라도 아니라면 상한치즈후보에서 제외된다
                    return False
    return True

#치즈별로 먹은 시간을 확인한다
#만약 아픈 사람이 발생한 시각보다 이전이라면 상한 치즈일 수 있음
#상한 치즈 후보이므로 해당 치즈를 먹은 다른 시람 또한 아픈 걸로 처리

max_val = 0 #아픈사람 수 최댓값 = 필요한 약의 갯수 최댓값

for cheese_idx in range(1,M+1): #치즈별로 검사하자. 치즈는 1번부터 M번까지이다.
    cnt = 0

    if is_bad(cheese_idx) == False: #상한치즈가 아니라면 카운팅하지 않는다
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