word1 = input()
word2 = input()

# Please write your code here.
#단어의 갯수가 같은지 체크하는 함수
def len_same(w1, w2):
    return len(w1)==len(w2)

#단어의 요소가 같은지 체크하는 함수
#오름차순으로 정렬 후 리스트 처음~끝까지 돌면서 같은지 체크
def is_same(w1, w2):
    arr1=list(w1)
    arr2=list(w2)

    arr1.sort()
    arr2.sort()

    for i in range(len(arr1)):
        if arr1[i]!=arr2[i]:
            return False
    return True

#Yes/No 출력
if len_same(word1,word2) and is_same(word1, word2):
    print("Yes")
else:
    print("No")