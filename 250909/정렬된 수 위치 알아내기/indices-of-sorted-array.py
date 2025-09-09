n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

# ex. 정렬 전(nums) : [(1,8), (2,3), (3,5)] / 인덱스:위치 , 내용:숫자
# -> 정렬 후(nums) : [(2,3), (3,5), (1,8)] / 인덱스:rank(등수별), 내용:숫자
# 위치별 등수 저장하는 리스트 : [3, 1, 2] / 인덱스: 위치, 내용:rank

# 위치와 내용도 함께 저장하는 리스트 (위치는 1부터 시작이니 +1 해줌)
nums = [(i+1, sequence[i]) for i in range(n)]
#nums = [i+1 for i in range(n)] #[1 2 3 4 5]

# 랭킹 저장하는 리스트 : ex. 1번원소(=8)->정렬후 5번째로 감 / 인덱스:위치, 내용:rank
num_to_rank = [0]*(n+1)

# 내용으로 오름차순 정렬
nums.sort(key=lambda s : s[1])

# 각 번호 위치에 랭킹 저장 (랭킹은 1부터 시작이니 +1 해줌)
for rank, num in enumerate(nums):
    num_to_rank[num[0]] = rank+1

# 공백을 사이에 두고 출력
for ele in num_to_rank[1:]:
    print(ele,end=" ")