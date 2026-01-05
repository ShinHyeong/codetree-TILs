n, m = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.

#완전탐색 접근

#구간을 나눈다
#최댓값 구한다
#최소인지 확인한다
#이 과정을 모든 경우에 대해 반복한다
#한계 : 그러나 for문의 횟수가 가변적이다 (for문 횟수 = m번)

def is_possible(limit): #limit : 최댓값
    m_cnt = 1 #구간 갯수
    curr_sum = 0

    for ele in a:
        if curr_sum + ele <= limit:
            curr_sum += ele #계속 더함
        else:
            m_cnt+=1 #구간늘림
            curr_sum = ele # 새 구간의 첫 숫자가 됨
    
    return m_cnt <= m

answer = 100*(n-((m-1)*2))
for limit in range(max(a)+1, sum(a)+1):
    if is_possible(limit):
        if limit <= answer:
            answer = limit
print(answer)