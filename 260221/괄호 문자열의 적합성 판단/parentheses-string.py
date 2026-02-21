str = input()

# Please write your code here.
items = []
for i in range(len(str)):
    if str[i] == "(":
        items.append(str[i])
    else: #str[i] == ")"
        if len(items)==0:
            print("No")
            break
        else:
            items.pop()

if len(items)==0:
    print("Yes")
else:
    print("No")