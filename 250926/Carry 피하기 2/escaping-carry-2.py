n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.


# carry : 수와 수를 더했을 때, 10의 자리를 넘기는 것 (받아올림이 발생하는가?)
# ex. 3+6 = 9 -> 발생 x
# ex. 5+7 = 12 -> 발생 o
# ex. 81+72 = 153 -> 일의자리는 발생 x / 십의자리는 발생 o
# 각 자리수를 모두 각각 더했을 때 10이상이 되는 경우가 없어야함

def is_carry(a,b,c): #자리수를 넣고
    return a+b+c>=10 #각 자리 수를 더 했을 때 10이상일 경우 false 리턴

#만약 모든 수 쌍에서 carry가 발생할 경우 -1 출력해야 해서 초기화는 -1
max_val = -1

# 서로 다른 3개의 수 고르기
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):

            # 각 자리수에 받아올림이 발생하는지 조사
            # = 계속 10으로 나눠주면서 일의 자리를 조사함
            carry_cnt=0
            a,b,c = arr[i],arr[j],arr[k]
            while max(a,b,c)>0 :
                if is_carry(a%10,b%10,c%10):
                    carry_cnt+=1
                a//=10
                b//=10
                c//=10

            # 합의 최댓값
            if carry_cnt==0:
                max_val = max(arr[i]+arr[j]+arr[k], max_val)

# 출력
print(max_val)