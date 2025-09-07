user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class User:
    def __init__(self,user_id,user_level):
        self.uid = user_id
        self.lv = user_level

#객체1 초기화 : 아이디 - "codetree" / 레벨 : 10
u1 = User("codetree",10)

#객체2: 새롭게 입력받은 값
u2 = User(user2_id,user2_level)

#형식대로 출력 : user 아이디 ㅣv 레벨
print(f"user {u1.uid} lv {u1.lv}")
print(f"user {u2.uid} lv {u2.lv}")
