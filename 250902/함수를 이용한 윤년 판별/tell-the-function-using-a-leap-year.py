y = int(input())

# Please write your code here.
def is_leapYear(y):
    if y%4==0:
        if y%100==0 and y%400!=0:
            return False
        return True
    else:
        return False
    
    

if is_leapYear(y):
    print("true")
else:
    print("false")