n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.

max_val = 0
for i in range(1,n+1): #시작위치를 고른다
    sum_val = 0 #시작위치 i에 대한, m번의 움직임에 대한 누적합
    for _ in range(m): #움직임은 M번 반복한다
        elm = arr[i]
        i = elm #움직임
        sum_val += arr[elm] #원소들의 누적합을 구한다
    max_val = max(sum_val, max_val) #시작위치 i에 대한 원소들의 누적합이 최대인지 확인한다
print(max_val)