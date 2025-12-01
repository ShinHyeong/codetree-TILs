# 가장 세련된 O(N) 풀이 (누적합 방식)
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
current_diff = 0 # 현재 누적해서 넘겨받은(또는 줘야할) 사람 수

for i in range(n):
    # (원래 있던 사람) - (있어야 할 사람)
    # 양수면 남아서 옆으로 넘기는 거고, 음수면 부족해서 옆에서 받아야 함
    current_diff += A[i] - B[i]
    
    # 옆 집으로 이동해야 하는 사람 수만큼 거리에 더함
    ans += current_diff 

print(ans)