text = input()
pattern = input()

# Please write your code here.

#target이 origin[n]부터의 수열과 일치하는지 확인
def is_same(n):
    for i in range(len(pattern)):
        if pattern[i]!=text[n+i]:
            return False
    return True


#부분 문자열이 있는지 확인 : 가능한 모든 위치에서 같은지 확인
#존재한다면 그 시작 인덱스 구하기
#없다면 -1
def getFirstIndex():
    for i in range(len(text)-len(pattern)+1):
        if is_same(i):
            return i
    return -1

print(getFirstIndex())