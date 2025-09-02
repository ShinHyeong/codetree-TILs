a, b = map(int, input().split())

# Please write your code here.
def power(a,b): #a^b
    cnt = 1
    for _ in range(b): #b번 a를 곱함
        cnt *= a
    
    return cnt

print(power(a,b))