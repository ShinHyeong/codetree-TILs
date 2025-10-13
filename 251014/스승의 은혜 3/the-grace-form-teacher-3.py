N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.
#최대한 선물 주기 -> 선물가격 낮은 거부터 구매
gifts.sort(key=lambda x:x[0]) #선물가격을 기준으로 오름차순 정렬
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

max_val = 0 #선물가능한 학생의 최대명수

for target in range(len(P)): #반값할인쿠폰을 적용할 선물
    buget = B #예산
    cnt=0 #선물 가능한 학생 수
    
    useCoupon = P[target]//2 #할인쿠폰 적용
    if buget>=(useCoupon+S[target]): #할인쿠폰 적용해도 구매 가능한지 확인
        buget -= (useCoupon+S[target])
        #print(target, useCoupon, S[target], "buget:", buget)
        cnt+=1
    
    for i in range(len(P)): #할인쿠폰 적용한 선물을 제외한 것들 구매가능한지 확인
        if i==target:
            continue
        if buget>=(P[i]+S[i]):
            buget -= (P[i]+S[i])
            #print(target, i, "buget:", buget)
            cnt+=1
    
    max_val = max(max_val, cnt)

print(max_val)