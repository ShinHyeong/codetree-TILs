n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

# ex. 정렬 전(nums) : [(1,8), (2,3), (3,5)] / 인덱스:pos(위치별) , 내용:value
# -> 정렬 후(nums) : [(2,3), (3,5), (1,8)] / 인덱스:rank(등수별), 내용:value
# 위치별 등수 저장하는 리스트 : [3, 1, 2] / 인덱스: pos, 내용:rank

# 위치와 내용도 함께 저장하는 리스트 (위치는 1부터 시작이니 +1 해줌)
values = [(i+1, sequence[i]) for i in range(n)]

# 랭킹 저장하는 리스트 : ex. 1번원소(=8)->정렬후 5번째로 감 / 인덱스:pos, 내용:rank
ranks = [0]*(n+1)

# 내용으로 오름차순 정렬
values.sort(key=lambda v : v[1])

# 각 번호 위치에 랭킹 저장 (랭킹은 1부터 시작이니 +1 해줌)
for rank, (pos, value) in enumerate(values):
    ranks[pos] = rank+1

# 공백을 사이에 두고 출력
for ele in ranks[1:]:
    print(ele,end=" ")