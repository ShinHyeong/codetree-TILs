N = int(input())

# Please write your code here.
def sum_val(n):
    if n==1:
        return 1

    return n + sum_val(n-1)

print(sum_val(N))