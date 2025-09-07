n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
# 미래 기상 데이터 클래스
class Forecast:
    def __init__(self, date, day, weather):
        self.date =date
        self.day = day
        self.weather = weather

# n개의 기상 데이터 클래스 저장한 리스트
forecast = [Forecast(date[i], day[i], weather[i]) for i in range(n)]

# 리스트 처음~끝까지 하나씩 꺼내면서 비가 오는데 가장 빠른 날짜 찾기
rst = Forecast("9999-99-99","","")
for i in range(n):
    if forecast[i].weather == "Rain":
        if forecast[i].date < rst.date:
            rst = forecast[i]

#날짜, 요일, 날씨 포맷 출력
print(rst.date, rst.day, rst.weather)