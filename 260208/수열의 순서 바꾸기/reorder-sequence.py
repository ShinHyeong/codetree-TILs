n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

## 요구사항 분석 ##
# 맨앞 숫자를 수열중간에 집어넣는다
# 최소 몇 번 반복해야 오름차순 정렬이 되는가

## 예제분석 ##
# 1 2 4 3
# 2 4 3 -> 1을 2뒤, 4뒤, 3뒤에 집어넣을 수 있다
# 2 4 1 3 -> 4뒤 pick cnt=1
# 4 1 3 -> 2를 4뒤, 1뒤, 3뒤에 집어넣을 수 있다
# 4 1 2 3 -> 1뒤 pick cnt=2
# 1 2 3 -> 4를 1뒤 2뒤 3뒤에 집어넣을 수 있다
# 1 2 3 4 -> 3뒤 pick cnt=3

## 로직 설정 ##
# 순환 구조
# 맨 앞 숫자가 a라면 a-1뒤에 집어넣으면 된다
# (단, 맨 앞 숫자가 1이라면 N뒤에 집어넣는다)
cnt = 0
sorted_seq = sorted(sequence)
while True:
    if sequence==sorted_seq:
        break
    target = sequence[0]-1 if sequence[0]!=1 else n
    target_idx = sequence.index(target)
    sequence = sequence[1:target_idx+1]+[sequence[0]]+sequence[target_idx+1:]
    cnt+=1

print(cnt)