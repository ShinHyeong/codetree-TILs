arr = input().split() #입력 -> [a, b, c]
a = arr[0]
b = arr[1]
c = arr[2]

#a, b 위치 케이스 -> c 위치를 샌드위치처럼 끼우기
if (a>b): #b a
    if c<b:
        print(b)  # c b a
    if b<c and c<a:
        print(c) # b c a 
    if a<c:
        print(a) # b a c
else: # a b
    if c<a:
        print(a) # c a b
    if a<c and c<b:
        print(c) # a c b
    if b<c:
        print(b) # a b c