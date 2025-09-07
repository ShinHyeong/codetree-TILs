secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Schedule:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

schedule1 = Schedule(secret_code, meeting_point, time)
print(f"secret code : {schedule1.secret_code}")
print(f"meeting point : {schedule1.meeting_point}")
print(f"time : {schedule1.time}")