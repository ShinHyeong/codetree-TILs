m,d = map(int,input().split())

#1, 3, 5, 7, 8, 10, 12
def is_exist(m,d):
    #상반기
    for i1 in range(1, 7+1, 2):
        if i1==m and d<=31:
            return True
    
    if m==2 and d<=28:
        return True

    for i2 in range(4, 7+1, 2):
        if i2==m and d<=30:
            return True

    #하반기
    for j in range(8, 12+1, 2):
        if j==m and d<=31:
            return True

    for k in range(9, 12+1, 2):
        if k==m and d<=30:
            return True
    
    return False

if is_exist(m,d):
    print("Yes")
else:
    print("No")