arr = input().split() #입력 -> [a, b, c]
a = arr[0]
b = arr[1]
c = arr[2]

if a<b:
    if b<c:
        print(b) #a b c
    else: #b>c
        if c<a: 
            print(a) #c a b
        else: #c>a 
            print(c) #a c b
else: #b<a
    if c<b:
        print(b) #c b a
    else: #c>b
        print(c) # b c a
