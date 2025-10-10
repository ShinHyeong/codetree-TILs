n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.

#해고 시뮬레이션 : 한명씩 해고해보면서 완전탐색한다
max_val = 0
for e in range(n) : #해고할사람 정하기
    
    #해고할 사람을 제외하고 개발자마다 [A,B)에 일하게 됨을 표시한다
    cntPeopleAtThisTime = [0]*1001 #1-indexed 해당 시간대에 몇 명이 일하는지 기록한다
    for i in range(n):
        if i==e:
            continue
        start,end = a[i],b[i]
        for t in range(start,end):
            cntPeopleAtThisTime[t] += 1

    #해고할 사람을 제외한 운행되고 있는 시간을 구한다
    cntTime=0
    for cntPeople in cntPeopleAtThisTime:
        if cntPeople>=1:
            cntTime+=1
            
    #그 시간이 최댓값인지 확인한다
    max_val = max(cntTime, max_val)

#최댓값 출력
print(max_val)