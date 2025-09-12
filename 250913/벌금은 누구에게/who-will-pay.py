N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
# 학생번호별로 벌칙에 걸린 횟수를 저장하는 리스트 (idx:학생번호 / value:벌칙에걸린횟수)
penalty_counts = [0] * (N+1) #0번은 학생번호로 취급안하므로 idx=0의 value는 0으로 남겨두고, idx=1부터 적용

#최초로 벌금을 내게 되는 학생
first_over_k = -1

# 학생번호가 m번에 걸쳐 주어질 때마다
for i in student:
    penalty_counts[i] += 1 #해당 번호의 벌칙받은횟수+1
    if penalty_counts[i] >= K:
        first_over_k = i
        break

print(first_over_k)