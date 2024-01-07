n1,n2 = map(int,input().split()) #a의 원소수, b의 원소수
arr_a = list(map(int,input().split()))
arr_b = list(map(int,input().split()))

#연속하게 뽑았을 때 나올 수 있는 수열인지 판단하라
def is_squence(arr_a, arr_b, n1, n2):
    #b의 첫 원소 a의 위치를 찾자
    pos = 0
    for i in range(n1):
        if(arr_a[i] == arr_b[0]):
            pos = i

    #그다음 일치하는지
    for j in range(n2):
        if(arr_a[pos] != arr_b[j]):
            return "No" #한번이라도 일치하지 않으면 false
        pos+=1
        

    return "Yes"

print(is_squence(arr_a, arr_b, n1, n2))