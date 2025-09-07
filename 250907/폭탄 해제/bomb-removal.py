unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
# 폭탄정보 (해체코드, 선의 색, 특정 초)
class Bomb:
    def __init__(self,unlock_code,wire_color,seconds):
        self.uc = unlock_code
        self.wc = wire_color
        self.sc = seconds

# 폭탄정보 입력        
b1 = Bomb(unlock_code,wire_color,seconds)

# 폭탄정보 출력
print(f"code : {b1.uc}")
print(f"color : {b1.wc}")
print(f"second : {b1.sc}")