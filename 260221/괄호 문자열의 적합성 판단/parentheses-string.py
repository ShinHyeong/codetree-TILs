str = input()

# Please write your code here.
items = []
isAnswer = True
for i in range(len(str)):
    if str[i] == "(":
        items.append(str[i])
    else: #str[i] == ")"
        if len(items)==0:
            isAnswer = False
            break
        else:
            items.pop()

if isAnswer and len(items)==0:
    print("Yes")
else:
    print("No")