N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.
# 쿠폰 적용할 선물 정하기
    # 쿠폰 적용해도 선물 구매 가능한가? 가능하다면 카운팅한다
# 전체 선물에 대해 선물 구매가능한지 따져보기
    # 선물가능하다면 카운팅

for i in range(N): #쿠폰 적용할 선물 정하기
    cntPresent = 0 #선물 가능한 갯수
    budget = B #예산
    PriceUsingCoupon = P[i] // 2 #반값쿠폰 적용한 가격
    
    if PriceUsingCoupon <= budget:
        budget -= PriceUsingCoupon
        cntPresent += 1

    for j in range(N):
        if j==i: #쿠폰 적용한 선물을 제외하고 나머지 선물들에 대해
            continue
        if P[j] <= budget: #예산안에서 구매가능한지 확인한다
            budget -= P[j]
            cntPresent += 1

print(cntPresent)

    