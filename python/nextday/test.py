import nextday

days = int(nextday.Lunar(1997, 1, 1).getDays())
week = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
print(week[(days+1)%7])
