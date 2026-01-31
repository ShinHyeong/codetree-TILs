N = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.

## 요구사항 분석
# 묶음 합이 짝홀이 번갈아 나게 묶어라.
# 최대 묶음 수를 구하라
# 주어진 순서랑 상관없이 묶음 만들어도 됨

## 로직 설정 (방법2)
even_cnt, odd_cnt = 0,0
for num in numbers:
    if num%2==0:
        even_cnt +=1
    else:
        odd_cnt+=1

group_cnt = 0
while True:
    if group_cnt%2==0: #짝수묶음을 만들때
        if even_cnt > 0: #1) 짝수가 있다면 1개만 쓴다
            even_cnt -=1
            group_cnt+=1 
        elif odd_cnt >= 2: #2) 짝수가 없다면 홀수2개로 짝수묶음을 구성한다
            odd_cnt -= 2
            group_cnt+=1 
        else:
            if even_cnt>0 or odd_cnt>0: #짝수를 다 썼거나 재료가 홀수 1개뿐이라서 짝수묶음에 편입시켜야한다면
                group_cnt -= 1
            break
    else: #홀수묶음을 만들때
        if odd_cnt > 0: # 홀수가 있다면 1개만 쓴다
            odd_cnt -=1
            group_cnt+=1
        else: #재료가 없으면 끝난 상태(짝홀...짝홀)
            break
print(group_cnt)