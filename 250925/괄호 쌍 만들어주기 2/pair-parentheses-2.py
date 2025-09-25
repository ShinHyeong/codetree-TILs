A = input()

# Please write your code here.
# 연속한 여는괄호 2개 + 연속한 닫는괄호 2개 조합 경우의 수 구하기
##로직
# 연속한 여는 괄호를 찾는다
# 그 뒤에오는 문자열 중 연속한 닫는 괄호를 찾고
    # 카운팅한다
cnt=0
for i in range(len(A)-1):
    if A[i]=="(" and A[i+1]=="(":
        for j in range(i+1, len(A)-1):
            if A[j]==")" and A[j+1]==")":
                cnt+=1
#출력
print(cnt)