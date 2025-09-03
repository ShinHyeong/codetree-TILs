n, m = map(int, input().split())

# Please write your code here.
#값을 교환하는 함수 작성
def swap(a,b):
    a,b = b,a
    return a,b

#값 교환 후 덮어쓰기
n,m = swap(n,m)

#출력
print(n,m)