N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.
# 가장 선물을 많이 구매하는 방법 : 저렴한 것부터 구매한다 -> 가격을 오름차순으로 정렬한다
# 쿠폰 적용할 선물 정하기
    # 쿠폰 적용해도 선물 구매 가능한가? 가능하다면 카운팅한다
    # 나머지 선물에 대해 선물 구매가능한가? 가능하다면 카운팅한다
    # 나머지 선물에 대해 구매가능한지 여부를 확인하기 전에 선물을 가격 기준으로 오름차순으로 정렬한다
    #카운팅한 값이 최댓값인지 확인

#최댓값 출력

max_val = 0
for i in range(N): #쿠폰 적용할 선물 정하기
    cntPresent = 0 #구매가능한 선물갯수
    budget = B #예산
    PriceUsingCoupon = P[i] // 2 #반값쿠폰 적용한 가격
    
    if PriceUsingCoupon <= budget:
        budget -= PriceUsingCoupon
        cntPresent += 1

    P.sort()
    for j in range(N):
        if j==i: #쿠폰 적용한 선물을 제외하고 나머지 선물들에 대해
            continue
        if P[j] <= budget: #예산안에서 구매가능한지 확인한다
            budget -= P[j]
            cntPresent += 1

    max_val = max(cntPresent, max_val)

print(max_val)

    