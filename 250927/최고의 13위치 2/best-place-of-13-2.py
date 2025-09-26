n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

#=====메인실행부분=====
max_val = 0

#1. 격자범위 처리 로직 : 1x3 격자 2개가 nxn격자 범위를 넘지 않게 한다
#첫번째 격자를 놓는다
for x1 in range(n):
    for start_y1 in range(n-2): #nxn격자 범위를 넘지 않게 한다 : n=5, 마지막 인덱스=4 라면 start_idx=2까지 가능함
        #두번째 격자를 놓는다
        for x2 in range(n):
            for start_y2 in range(n-2): #nxn격자 범위를 넘지 않게 한다
                
                #2. 겹침 처리 로직
                #두 격자가 겹칠 경우 동전수를 세지 않는다
                if x1==x2 and abs(start_y1-start_y2)<=2:
                    continue                
                
                #두 격자 모두 nxn 격자를 벗어나지 않는다면 해당 범위 안애 있는 동전의 개수를 센다
                cnt1= arr[x1][start_y1]+arr[x1][start_y1+1]+arr[x1][start_y1+2]
                cnt2= arr[x2][start_y2]+arr[x2][start_y2+1]+arr[x2][start_y2+2]
		                
                #최대 동전의 수 업데이트
                max_val = max(cnt1+cnt2, max_val)

print(max_val) #최대 동전의 수 출력