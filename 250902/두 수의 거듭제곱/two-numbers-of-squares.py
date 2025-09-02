a, b = map(int, input().split())

# Please write your code here.
def square_ab(a,b):
    multiple = a
    for _ in range(b-1): #b-1번 a를 곱함
        a *= multiple
    return a

print(square_ab(a,b))