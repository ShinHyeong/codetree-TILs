#입력받아서 튜플에 저장하고
#단어 길이 확인하고
#만약 단어 길이가 같다면
#"same"을 출력합니다.

a,b = tuple(input().split()) 
if len(a)==len(b):
    print("same")
elif len(a)>len(b):
    print(f"{a} {len(a)}")
else:
    print(f"{b} {len(b)}")