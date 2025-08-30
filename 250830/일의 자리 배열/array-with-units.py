#입력받기
a, b = tuple(map(int,input().split()))

rst = [a, b] #주어진대로 1번째, 2번째 항으로 설정
for i in range (2,10): #3번째 항부터 마지막 항까지
    rst.append((rst[i-2]+rst[i-1])%10) #전전항 + 전항의 합을 구하여 그 합의 1의 자리 추가

#출력
for x in rst: 
    print(x,end=" ")