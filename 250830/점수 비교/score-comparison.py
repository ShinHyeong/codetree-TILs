scoreA = list(map(int,input().split()))
scoreB = list(map(int,input().split()))

if scoreA[1]>scoreB[1] and scoreA[0]>scoreB[0]:
    print(1)
else:
    print(0)