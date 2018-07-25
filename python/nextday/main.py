import nextday
monBig = [1,3,5,7,8,10,12]
monMid = [4,6,9,11]
def getNextday(year,month,day):
    if month in monBig:
        month += int(day/31)
        day += 1
        day = day-31 if(day > 31) else day
        if month > 12:
            year += 1
            month -= 12
    elif month in monMid:
        month += int(day/30)
        day += 1
        day = day-30 if(day > 30) else day
    else:
        if isRunNian(year):
            month += int(day/29)
            day += 1
            day = day-29 if(day > 29) else day
        else:
            month += int(day/28)
            day += 1
            day = day-28 if(day > 28) else day
    return (year,month,day)

def isRunNian(year):
        if year%400==0 or (year%4==0 and year %100 != 0):
            return True
        return False
'''        
if __name__ == "__main__":
    while True:
        year = int(input("请输入年份(1900-2050):"))
        if 1900<= year <= 2050:
            break
        print("请输入合适的年份:")
    while True:
        month = int(input("请输入月份(1-12):"))
        if 1 <= month <= 12:
            break
        print("请输入合适的月份:")
    while True:
        day = int(input("请输入某天(1-31):"))
        if 1 <= day <= 28:
            break
        if day == 29 and isRunNian(year) and month == 2:
            break
        if day == 30 and (month != 2):
            break
        if day == 31 and month in monBig:
            break
        
    newYear, newMonth,newDay = getNextday(year,month,day)
    print('{}-{}-{}的下一天是:'.format(year,month,day))
    nextday.test(newYear,newMonth,newDay)'''
        