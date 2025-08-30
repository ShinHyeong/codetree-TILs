sex = int(input())
age = int(input())

#if1 : 성인인지
#if2 : 성별
if age >= 19:
    if sex == 0:
        print("MAN")
    else:
        print("WOMAN")
else:
    if sex == 0:
        print("BOY")
    else: 
        print("GIRL")
