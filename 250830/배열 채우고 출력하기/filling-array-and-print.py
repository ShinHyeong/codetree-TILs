arr = input().split() #입력받기

#뒤에서부터 출력하기
for i in range(len(arr), -1, -1):
    print(arr[i], end="") #줄바꿈없이 출력