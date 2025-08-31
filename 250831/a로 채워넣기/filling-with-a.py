#문자열 받아주고
#변화1 = 앞에서 2번째 원소가 뭔지 알아내고(index) a로 대체(replace) 1번만
#replace 도는 순서가 앞에서부터니까 일단 한번 뒤집어주고
#변화2reverse = 변화1reverse의 2번째 원소가 뭔지 알아내고(index) a로 대체(replace) 1번만
#변화2 = 다시 뒤집어줘서 원래순서대로
#출력

s = input()
new1 = s.replace(s[1], "a", 1)
new1_reverse = new1[::-1]
new2_reverse = new1_reverse.replace(new1_reverse[1], "a", 1)
new2 = new2_reverse[::-1]
print(new2)