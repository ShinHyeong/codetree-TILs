#문자열 받아주고
#변화1 = 앞에서 2번째 원소가 뭔지 알아내고(index) a로 대체(replace) 처음만
#변화2 = 뒤에서 2번째 원소가 뭔지 알아내고(index) a로 대체(replace) 처음만
#출력

s = input()
new1 = s.replace(s[1], "a", 1)
new2 = new1.replace(new1[-2], "a", 1)
print(new2)