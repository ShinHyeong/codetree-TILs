n = int(input())
word = [input() for _ in range(n)]

# Please write your code here.
#알파벳 오름차순 정렬
word.sort()
for w in word:
    print(w)