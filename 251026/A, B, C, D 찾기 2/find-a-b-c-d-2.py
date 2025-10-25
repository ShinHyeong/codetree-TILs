nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()

MIN_NUM, MAX_NUM = 1, 40 

def solve():
    for a in range(MIN_NUM, MAX_NUM+1):
        for b in range(a, MAX_NUM+1):
            for c in range(b, MAX_NUM+1):
                for d in range(c, MAX_NUM+1):
                    tmp = [a,b,c,d,a+b,b+c,c+d,d+a,a+c,b+d,a+b+c,a+b+d,a+c+d,b+c+d,a+b+c+d]
                    tmp.sort()
                    if tmp==nums:
                        print(a,b,c,d)
                        return True
    return False

solve()