N = int(input())
str = input()

# Please write your code here.

#연속부분문자열로 2번 이상 나타나지 않는 문자열의 최소길이 -> 문자열의 완전 탐색

#주어진 문자열의 연속부분문자열 중 길이=1인 문자열 set 만들고 2번이상 나타나는지 확인
#주어진 문자열의 연속부분문자열 중 길이=2인 문자열 set 만들고 2번이상 나타나는지 확인
#..
#주어진 문자열의 연속부분문자열 중 길이=N인 문자열 set 만들고 2번이상 나타나는지 확인

for length in range(1,N+1): #연속부분문자열의 길이를 정한다

    is_duplicate = False

    for i in range(N-length): #length 길이의 검사할 연속부분문자열을 정한다

        target = str[i:i+length]
        
        for j in range(i+1, N-length+1): #2번이상 나타나는지 검사시작
            if target == str[j:j+length]:
                is_duplicate = True
                break #2번이상 나타나면 검사종료
        
        if is_duplicate: #해당 길이의 target에 대하여, 중복이 한번이라도 발생시
            break #길이를 +1하여 다음 검사할 길이의 연속부분문자열을 정한다

    if is_duplicate == False: #해당 길이의 모든 연속부분문자열에 대해 중복이 단 한번도 발생하지 않았다면 이는 답이므로 출력하고 종료한다.
        print(length)
        break