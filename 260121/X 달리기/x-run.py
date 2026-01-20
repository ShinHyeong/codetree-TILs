X = int(input())

# Please write your code here.

###예시분석###
# 총 주행 거리 = X
# "최대 속력 지점은 어디로 잡을까?"
# ex. time=1 dist=1= 1*1
# ex. time=3 dist=1+2+1= 2*2
# ex. time=5 dist=1+2+3+2+1= 3*3
# ex. time=7 dist=1+2+3+4+3+2+1 = 4*4
# ex. time=9 dist =5*5
#     time=2*n+1 dist=(n+1)*(n+1)

###로직###
# X가 제곱수가 아닐 경우 어디사이에 위치하는지 생각해보자
# ex. X=10 3*3 <=X<= 4*4

# time=5 pick! 1+2+3+2+1 에 유지할 속도를 끼워넣자 -> 몇번끼워야하는지 확인한다
    # 최대속력을 구하고, X-dist-최대속력<=0인지 확인한다. 그러니까 속도유지 1번으로 충족이 되냐는 뜻이다(답은 time+1로 처리) 
        # 만약 안되면 또 최대속력을 빼고 확인한다. 답은 time+1+1
        #ex. X=13, dist=9라서 13-9=4인 경우
# time+끼워넣은 횟수 가 답!

n, time, dist = 0,0,0
while True:
    time, dist = (2*n)+1, (n+1)*(n+1)
    if dist>X:
        n-=1
        time, dist = (2*n)+1, (n+1)*(n+1)
        break
    elif dist==X:
        break
    n+=1

if dist==X:
    print(time)
else:
    max_speed = n+1
    remain_dist = X-dist     
    while True:
        remain_dist -= max_speed
        time += 1
        if remain_dist<=0:
            break

    print(time)
