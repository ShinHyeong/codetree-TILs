N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    if line[0] == "push_front":
        A = [line[1]]+A
    if line[0] == "push_back":
        A.append(line[1])
    if line[0] == "pop_front":
        print(A[0])
        if len(A)==1:
            A = []
        else:
            A = A[1:]
    if line[0] == "pop_back":
        print(A[-1])
        if len(A)==1:
            A = []
        else:
            A = A[:-1]
    if line[0] == "size":
        print(len(A))
    if line[0] == "front":
        print(A[0])
    if line[0] == "back":
        print(A[-1])
    if line[0] == "empty":
        print(1 if len(A)==0 else 0)
