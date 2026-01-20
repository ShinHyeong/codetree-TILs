X = int(input())

# Please write your code here.

# 총 주행 거리 = X
# 최단시간으로 가려면 증가->감소->유지 패턴으로
# 감소지점을 잘 잡자!

min_time = 10000
decrease_second = 2 #속도 감소 지점

while decrease_second<=X:

    dist, time, speed = 1,1,1
    while dist<X: #1초이후 시뮬레이션
        time += 1
        if speed>1 and time >= decrease_second:
            speed -= 1
        elif speed == 1 and time >= decrease_second:
            speed = 1
        else:
            speed += 1
        dist+=speed
    
    if speed==1 and dist==X:
        min_time = min(time, min_time)
    else:
        break
    
    decrease_second +=1
    
    

print(min_time)