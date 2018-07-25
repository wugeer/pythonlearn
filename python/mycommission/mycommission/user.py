import user_commit
import mydb
import tkinter as tk
import showsales
import showsalary
import tkinter.messagebox as messagebox
import datetime
class user(tk.Toplevel,tk.Tk):
    def __init__(self,userinfo):
        super().__init__()
        self.window = tk.Tk()
        self.user_name = userinfo[0]
        self.priot = userinfo[1]
        self.window.title("user")
        menubar = tk.Menu(self.window)  
        # create a pulldown menu, and add it to the menu bar  
        filemenu = tk.Menu(menubar, tearoff=0)  
        filemenu.add_command(label="commit", command=self.commit)  
        filemenu.add_separator() 
        filemenu.add_command(label="search sales for month", command=self.look_sales_month)  
        filemenu.add_separator()  
        filemenu.add_command(label="search sales for year", command=self.look_sales_year)#command=self.window.quit  
        menubar.add_cascade(label="sales", menu=filemenu)  
          
        # create more pulldown menus  
        editmenu = tk.Menu(menubar, tearoff=0)  
        editmenu.add_command(label="search salary for month", command=self.look_salary_month)  
        filemenu.add_separator() 
        editmenu.add_command(label="search salary for year", command=self.look_salary_year)  
        #editmenu.add_command(label="Paste", command=self.hello)  
        menubar.add_cascade(label="salary", menu=editmenu)  
          
        helpmenu = tk.Menu(menubar, tearoff=0)  
        helpmenu.add_command(label="About", command=self.hello)  
        helpmenu.add_command(label="quit", command=self.window.quit)  
        menubar.add_cascade(label="Help", menu=helpmenu)  
          
        # display the menu  
        self.window.config(menu=menubar)  

    def look_sales_month(self):
        comm =  mydb.Commission()
        res = list(comm.get_user_search_month([self.user_name,self.priot]))
        show_sale = showsales.show_sale()
        if res is None:
            messagebox.showerror("Error","data is none")
            return
        num = [0,"",0,0,0]
        for r in res:
            num[0] += 1
            num[1:] = r
            show_sale.showData(num)
        
    def look_sales_year(self):
        comm =  mydb.Commission()
        res = list(comm.get_user_search_month([self.user_name,self.priot]))
        show_sale = showsales.show_sale()
        if res is None:
            messagebox.showerror("Error","data is none")
            return
        num = [1,"",0,0,0]
        num[1] = res[0][0][:4]
        for r in res:
            if num[1] == r[0][:4]:
                num[2] += r[1]
                num[3] += r[2]
                num[4] += r[3]
            else:
                show_sale.showData(num)
                num[0] += 1
                num[1] = r[0][:4]
                num[2:] = r[1:]
        show_sale.showData(num)

    def look_salary_year(self):#没有修改成功
        comm =  mydb.Commission()
        show_salary = showsalary.show_salary()
        res = list(comm.get_user_search_month([self.user_name,self.priot]))
        if res is None:
            messagebox.showerror("Error","data is none")
            return
        num = [1,"",0,0,0,0.]
        num[1] = res[0][0][:4]
        for r in res:
            if num[1] == r[0][:4]:
                num[2] += r[1]
                num[3] += r[2]
                num[4] += r[3]
                num[5] += r[4]
            else:
                show_salary.showSalaryData(num)
                num[0] += 1
                num[1] = r[0][:4]
                num[2:] = r[1:]
        show_salary.showSalaryData(num)

    def look_salary_month(self):
        comm =  mydb.Commission()
        res = list(comm.get_user_search_month([self.user_name,self.priot]))
        show_salary = showsalary.show_salary()
        if res is None:
            messagebox.showerror("Error","data is none")
            return
        num = [0,"",0,0,0,0.]
        for r in res:
            num[0] += 1
            num[1] = r[0]
            num[2:] = r[1:]
            show_salary.showSalaryData(num)
    
    def commit(self):
        usr = user_commit.usr_op([self.user_name,self.priot])
        if usr is None:
            print('failed')
            return

    def hello(self):
        messagebox.showinfo("help","this is a commission system")

