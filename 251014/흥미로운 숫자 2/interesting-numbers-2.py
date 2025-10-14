X, Y = map(int, input().split())

# Please write your code here.
def get_num(num):
    digits = []
    while num>=10:
        digits.append(num%10)
        num//=10
    digits.append(num%10)
    return digits[::-1]

def is_interesting(num):
    digit_cnts = [0]*10 #0~9
    digits = get_num(num)
    for digit in digits:
        digit_cnts[digit] += 1

    for i in range(len(digit_cnts)):
        for j in range(len(digit_cnts)):
            if i==j:
                continue

            if digit_cnts[i]==1 and digit_cnts[j]==len(digits)-1:
                return True

    return False

cnt=0
for num in range(X,Y+1):
    if is_interesting(num):
        cnt+=1
print(cnt)