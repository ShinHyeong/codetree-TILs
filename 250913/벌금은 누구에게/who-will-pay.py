N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
# 학생번호별로 벌칙에 걸린 횟수를 저장하는 리스트 (idx:학생번호 / value:벌칙에걸린횟수)
penalty_counts = [0] * (N+1) #0번은 학생번호로 취급안하므로 idx=0의 value는 0으로 남겨두고, idx=1부터 적용

# 학생번호가 m번에 걸쳐 주어질 때마다
for i in student:
    penalty_counts[i] += 1 #해당 번호의 벌칙받은횟수+1

# 학생번호별로 벌칙에 걸린 횟수를 확인하면서
# 만약 그 횟수(=리스트의 value)가 k 이상이라면 학생번호(=리스트의 idx) 출력
# 없으면 -1 출력

def over_k(penalty_counts, k):
    for i, cnt in enumerate(penalty_counts):
        if cnt >= k:
            return i
    return -1

print(over_k(penalty_counts, K))


