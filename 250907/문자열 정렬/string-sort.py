str = input()

# Please write your code here.
#알파벳 오름차순으로 정렬하는 문자열
#1. 문자열->리스트
arr = list(str)
#2. 알파벳 오름차순으로 정렬
arr.sort()
#3. 리스트->문자열
#4. 출력
print(''.join(arr))