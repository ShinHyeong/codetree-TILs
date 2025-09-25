n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
max_val = 0 #주어지는 수는 양수이므로

for curr_idx in range(len(numbers)): # numbers 하나씩 고르는데
    for next_idx in range(curr_idx+2, len(numbers)): # 인접하지 않은 수 더하고
        max_val = max(numbers[curr_idx]+numbers[next_idx], max_val) # 최대값인지 확인 후 업데이트

print(max_val)    