n = int(input())
a = [0] + list(map(int, input().split()))

# Please write your code here.

# 새로운 배열을 만들어 정렬하고
# 2번째로 작은 숫자(target)을 정의한다
sorted_a = sorted(a[1:])
target = -1
for ele in sorted_a:
    if ele != sorted_a[0]:
        target = ele
        break

ans = -1
cnt = 0
for i in range(1,n+1):
    if a[i]==target:
        ans = i
        cnt += 1

    if cnt > 1:
        ans = -1
        break

print(ans)