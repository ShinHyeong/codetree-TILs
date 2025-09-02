n = int(input())

# Please write your code here.
def div_10(n):
    sum_val=0
    for i in range(1,n+1):
        sum_val += i
    return sum_val//10

print(div_10(n))