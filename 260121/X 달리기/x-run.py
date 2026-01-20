X = int(input())

# Please write your code here.

# 총 주행 거리 = X
# 최단시간으로 가려면 증가->감소->유지 패턴으로

dist, time, speed = 1,1,1

while dist<X: #1초 이후부터 계산
    time+=1

    #속력 유지/증가/감소 선택기준 : 속력증가 시킨 후 다음 상태를 미리 예측한다
    #속력증가 시나리오 시 다음 상태 거리(nxt_dist) = dist+(speed+1)
    #속력 증가 조건 : nxt_dist < X
    #속력 감소/유지 조건 : nxt_dist==X를 달성해도 speed!=1이면 감소/유지해야한다
    
    #nxt_dist = dist+(speed+1)
    if dist < X//2: #속력 증가 조건
        speed += 1
    elif speed!=1: #속력 감소 조건
        speed -= 1
        
    dist+=speed

    #print(time,speed,dist)

print(time)