#n,m 입력받기
#1번째n*m격자 받기
#2번째격자받기
n,m=tuple(map(int,input().split()))
arr1 = [list(map(int,input().split())) for _ in range(n)]
arr2 = [list(map(int,input().split())) for _ in range(n)]
arr3 = [[0 for _ in range(m)] for _ in range(n)]

#n*m격자돌기
#두 격자의 각 위치의 값이 같으면 0 그렇지 않다면 1
#새롭게만든격자출력하기
for i in range(n):
    for j in range(m):
        if arr1[i][j]==arr2[i][j]:
            arr3[i][j] = 0
        else:
            arr3[i][j] = 1
        
        print(arr3[i][j], end=' ')
    print()