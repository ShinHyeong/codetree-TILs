A = input()

# Please write your code here.

#멀리있어도 좋으니 먼저 여는괄호부터 시작 -> 닫는괄호 ==> 쌍 완성
#문자열 하나씩 돌면서 여는괄호 찾기
#그 뒤 인덱스의 닫는괄호 찾기
#카운팅
# 다시 그 다음 여는괄호 찾기
# 그 뒤 인덱스의 닫는 괄호 찾기
# 카운팅
# ..
cnt=0
for i in range(len(A)):
    if A[i]=="(":
        for j in range(i+1, len(A)):
            if A[j]==")":
                cnt+=1
print(cnt)