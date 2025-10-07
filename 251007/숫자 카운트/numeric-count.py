n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.

#생각한 수 자릿수 분리
def get_digit(num):
    third = num%10
    second = (num//10)%10
    first = (num//10**2)%10
    return (first, second, third)

def get_cnt1(num, d1, d2, d3):
    cnt1=0
    f,s,t = get_digit(num)
    if d1==f:
        cnt1+=1
    if d2==s:
        cnt1+=1
    if d3==t:
        cnt1+=1
    return cnt1

def get_cnt2(num, d1, d2, d3):
    cnt2=0
    f,s,t = get_digit(num)
    if d1==s or d1==t:
        cnt2+=1
    if d2==f or d2==t:
        cnt2+=1
    if d3==f or d3==s:
        cnt2+=1
    return cnt2

answer = 0 #후보의 수

#1부터 9까지의 서로 다른 숫자 3개로 만들 수 있는 모든 세 자리 수 후보를 만든다
for d1 in range(1,10):
    for d2 in range(1,10):
        for d3 in range(1,10):
            if d1==d2 or d1==d3 or d2==d3: #서로 다르지 않으면 후보 탈락
                continue
            
            #이 후보가 모든 조건을 통과하는가?
            counter = 0
            for i in range(n):
                cnt1,cnt2 = 0,0
        
                #후보 숫자의 cnt1, cnt2를 구한다
                cnt1 = get_cnt1(a[i],d1,d2,d3)
                cnt2 = get_cnt2(a[i],d1,d2,d3)
                
                if cnt1==b[i] and cnt2==c[i]:
                    counter+=1
            
            #모든 num의 1번카운트, 2번카운트와 일치하면 후보 확정
            if counter == n:
                answer += 1
            
print(answer)