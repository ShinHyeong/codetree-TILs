n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

# ex. 정렬 전(nums) : [(1,8), (2,3), (3,5)] / 인덱스:pos(위치별) , 내용:value
# -> 정렬 후(nums) : [(2,3), (3,5), (1,8)] / 인덱스:rank(등수별), 내용:value
# 위치별 등수 저장하는 리스트 : [3, 1, 2] / 인덱스: pos, 내용:rank

# 위치와 내용도 함께 저장하는 리스트
indexed_sequence = list(enumerate(sequence))

# 랭킹 저장하는 리스트
ranks = [0]*n

# 내용으로 오름차순 정렬
indexed_sequence.sort(key=lambda s : s[1])

# 각 번호 위치에 랭킹 저장 (랭킹은 1부터 시작이니 +1 처리해줌)
for rank, (pos, value) in enumerate(indexed_sequence):
    ranks[pos] = rank+1

# 공백을 사이에 두고 출력 
for r in ranks:
    print(r,end=" ")