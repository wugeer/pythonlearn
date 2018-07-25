import tkinter  as Tkinter
import main
import nextday
import sys
import time
from line_profiler import LineProfiler
def checkTime(year,month,day):
    str = ''
    monBig = [1,3,5,7,8,10,12]
    if not (1900<= year <= 2050):
        str += "请输入合适的年份1900-2050："
    if not (1 <= month <= 12):
        str += " 请输入合适的月份1-12："
    if 1 <= day <= 28:
        pass
    elif day == 29 and main.isRunNian(year) and month == 2:
        pass
    elif day == 30 and (month != 2):
        pass
    elif day == 31 and month in monBig:
        pass
    else:
        if day < 1:
            str += "日期不允许小于1"
        else:
            str += "抱歉，%d年%d月没有%d号这一天"%(year,month,day)
    return str

def getNextDay():  
    try:
        year = int(entryYear.get())
        month = int(entryMonth.get())
        day = int(entryDay.get())
    except ValueError as error:
        eLinter.set("时间格式不合法:")
    else:
        time_start = time.time()
        lp = LineProfiler()
        lp.add_function(main.isRunNian)
        lp_wrapper = lp(checkTime)
        lp_wrapper(year,month,day)
        lp.print_stats()
        str1 = checkTime(year,month,day)
        if '' != str1:
            eLinter.set(str1)
            eYear.set('')
            eMonth.set('')
            eDay.set('')
            eLunar.set('')
            return
        newYear, newMonth, newDay = main.getNextday(year,month,day)
        #在界面显示结果
        eYear.set(str(newYear))
        eMonth.set(str(newMonth))
        eDay.set(str(newDay))
        eLinter.set("")
        days = int(nextday.Lunar(newYear, newMonth, newDay).getDays())
        week = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
        #print(week[(days+1)%7])
        eLunar.set(nextday.test(newYear,newMonth,newDay)+" "+week[(days+1)%7])
          
def cancel():  #退出程序
    sys.exit(0)

def clear():
    eYear.set('')
    eMonth.set('')
    eDay.set('')
    eLunar.set('')
    ey.set('')
    em.set('')
    ed.set('')
    eLinter.set('')

def validateYear():
    try:
        year = int(entryYear.get())
        if 1990<= year<=2050:
            return True
        else:
            ey.set("")
            eLinter.set('请输入合适的年份1900-2050：')
            return False
    except:
        ey.set("")
        eLinter.set('请输入合适的年份1900-2050：')
        invalidateYear()
        return False
            
        
def invalidateYear():
    return True

def validateMonth():
    try:
        month = entryMonth.get()
        if 1 <= int(month) <= 12:
            return True
        else:
            em.set("")
            eLinter.set(eLinter.get()+"请输入合适的月份1-12：")
            return False
    except:
        em.set("")
        eLinter.set(eLinter.get()+"请输入合适的月份1-12：")
        invalidateMonth()
        return False

def invalidateMonth():
    return True
    


root = Tkinter.Tk()  
root.title("得到下一天")
root.geometry('400x150') 

labelYear = Tkinter.Label(root,text = '年份:',justify = Tkinter.RIGHT,width = 80)  
labelYear.place(x = 10,y = 5,width = 80,height = 20)  
ey = Tkinter.StringVar()
entryYear = Tkinter.Entry(root,width = 80,textvariable = ey,validate='focusout', validatecommand=validateYear,invalidcommand=invalidateYear)  
entryYear.place(x = 100,y = 5,width = 80,height = 20)  

labelNewYear = Tkinter.Label(root,text = '下一天年份:',justify = Tkinter.RIGHT,width = 80)  
labelNewYear.place(x = 200,y = 5,width = 80,height = 20)  
eYear = Tkinter.StringVar()
entryNewYear = Tkinter.Entry(root,width = 80,textvariable=eYear,state="readonly")  
entryNewYear.place(x = 300,y = 5,width = 80,height = 20)  

labelMonth = Tkinter.Label(root,text = '月份:',justify = Tkinter.RIGHT,width = 80)  
labelMonth.place(x = 10,y = 30,width = 80,height = 20)  
em = Tkinter.StringVar()
entryMonth = Tkinter.Entry(root,width = 80,textvariable = em,validate='focusout', validatecommand=validateMonth,invalidcommand=invalidateMonth)  
entryMonth.place(x = 100,y = 30,width = 80,height = 20)  

labelNewMonth = Tkinter.Label(root,text = '下一天月份:',justify = Tkinter.RIGHT,width = 80)  
labelNewMonth.place(x = 200,y = 30,width = 80,height = 20)  
eMonth = Tkinter.StringVar()
entryNewMonth = Tkinter.Entry(root,width = 80,textvariable=eMonth,state="readonly")  
entryNewMonth.place(x = 300,y = 30,width = 80,height = 20)  
  
labelDay = Tkinter.Label(root,text = '某天:',justify = Tkinter.RIGHT,width = 80)  
labelDay.place(x = 10,y = 55,width = 80,height = 20)  
ed = Tkinter.StringVar()
entryDay = Tkinter.Entry(root,width = 80,textvariable = ed)  
entryDay.place(x = 100,y = 55,width = 80,height = 20) 

labelNewDay = Tkinter.Label(root,text = '下一天某天:',justify = Tkinter.RIGHT,width = 80)  
labelNewDay.place(x = 200,y = 55,width = 80,height = 20)  
eDay = Tkinter.StringVar()
entryNewDay = Tkinter.Entry(root,width = 80,textvariable=eDay,state="readonly")  
entryNewDay.place(x = 300,y = 55,width = 80,height = 20)  

labelLunar = Tkinter.Label(root,text = '农历:',justify = Tkinter.RIGHT,width = 80)  
labelLunar.place(x = 10,y = 80,width = 80,height = 20)  
eLunar = Tkinter.StringVar()
entryLunar = Tkinter.Entry(root,width = 280,textvariable=eLunar,state="readonly")  
entryLunar.place(x = 100,y = 80,width = 280,height = 20)  

labelLinter = Tkinter.Label(root,text = '提示:',justify = Tkinter.RIGHT,width = 80)  
labelLinter.place(x = 10,y = 105,width = 80,height = 20)  
eLinter = Tkinter.StringVar()
entryLinter = Tkinter.Entry(root,width = 280,textvariable=eLinter,state="readonly")  
entryLinter.place(x = 100,y = 105,width = 280,height = 20)  


  
buttonGetNextDay = Tkinter.Button(root,text = '下一天',command = getNextDay)  
buttonGetNextDay.place(x = 100,y = 130,width =50,height = 20)  
buttonClear = Tkinter.Button(root,text = '重试',command = clear)  
buttonClear.place(x = 200,y = 130,width =50,height = 20)  
buttonCancel = Tkinter.Button(root,text = '取消',command = cancel)  
buttonCancel.place(x = 300,y = 130,width = 50,height = 20)  


root.mainloop() 
'''import tkinter as tk

app = tk.Tk()
app.title("下一天程序")
varName = tk.StringVar(value = '')  
labelName = tk.Label(app,text = 'User Name:',justify = tk.RIGHT,width = 80)  
labelName.place(x = 10,y = 5,width = 80,height = 20)  
entryName = tk.Entry(app,width = 80,textvariable = varName)  
entryName.place(x = 100,y = 5,width = 80,height = 20)  
labelYear = tk.Label(app,text='年份',width=100,height=10)

textYear = tk.Entry()
labelYear.pack()
textYear.pack()
def getYear():
    return textYear.get()
app.mainloop()'''
