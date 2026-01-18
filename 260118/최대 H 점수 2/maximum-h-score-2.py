N, L = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.

# "최대 L개"라고 했으므로 L은 일종의 기회
# 원소값과 N의 최댓값이 100이므로 H점수의 최댓값 = 100

# 핵심문제 : <L번의 기회를 써서 H를 최댓값으로 만들 수 있는가>

# 리스트 값들 중에서
    # H이상인 값 -> countA
    # H-1인 값 -> countB (최대 L번만)
    # H-2 이하 값 : 고려 x

def get_h(t_list):
    t_list.sort(reverse=True)
    
    for i in range(0,N-1):
        target = t_list[i]
        chance = L
        cntA, cntB = 0, 0

        for ele in t_list:
            if ele >= target:
                cntA += 1
            elif chance > 0 and ele == target-1:
                chance -= 1
                cntB += 1

        target_cnt = cntA + cntB

        if target_cnt >= target:
            return target      

    return target

print(get_h(a))     


