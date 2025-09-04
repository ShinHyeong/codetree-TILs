n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
# 매개변수 : 부분수열의 인덱스
# 수열A를 전역변수로 표현하기
# 수열A의 a1 ~ a2 합 구하는 함수
def sum_seq(query):
    global arr
    sum_val = 0
    
    a,b = query[0]-1, query[1]-1
    for i in range(a,b+1):
        sum_val += arr[i]
    
    return sum_val

# M번에 걸쳐 수열A의 a1 ~ a2 합 출력
for q in queries:
    print(sum_seq(q))