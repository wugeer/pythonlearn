import user_commit
import mydb
import tkinter as tk
import showsales
import tkinter.messagebox as messagebox
import datetime
import showmanagersales
import search_user

class user(tk.Toplevel,tk.Tk):
    def __init__(self,userinfo):
        super().__init__()
        self.window = tk.Tk()
        self.user_name = userinfo[0]
        self.priot = userinfo[1]
        self.window.title("manager")
        menubar = tk.Menu(self.window)  
        # create a pulldown menu, and add it to the menu bar  
        filemenu = tk.Menu(menubar, tearoff=0)  
        filemenu.add_command(label="search sales for month", command=self.look_sales_month)  
        filemenu.add_separator()  
        filemenu.add_command(label="search sales for year", command=self.look_sales_year)#command=self.window.quit  
        menubar.add_cascade(label="sales", menu=filemenu)  
          
        # create more pulldown menus  
        
        editmenu = tk.Menu(menubar, tearoff=0)  
        editmenu.add_command(label="search salry for month", command=self.look_salary_month)  
        editmenu.add_separator() 
        editmenu.add_command(label="search salry for year", command=self.look_salary_year)  
        #editmenu.add_command(label="Paste", command=self.hello)  
        menubar.add_cascade(label="salary", menu=editmenu)  

        
        searmenu = tk.Menu(menubar, tearoff=0)  
        searmenu.add_command(label="search sales and salry of user", command=self.look_sales_salary_of_user)  
        #searmenu.add_separator() 
        #searmenu.add_command(label="search salry for year", command=self.look_salary_year)  
        #editmenu.add_command(label="Paste", command=self.hello)  
        menubar.add_cascade(label="search", menu=searmenu)  
          
        helpmenu = tk.Menu(menubar, tearoff=0)  
        helpmenu.add_command(label="About", command=self.help)  
        helpmenu.add_command(label="quit", command=self.window.quit)  
        menubar.add_cascade(label="Help", menu=helpmenu)  
          
        # display the menu  
        self.window.config(menu=menubar)  

    def look_sales_salary_of_user(self):
        search_us = search_user.search_user()
        if search_us is None:
            print('failed')
            return

    def look_sales_month(self):
        comm =  mydb.Commission()
        res = list(comm.get_manager_search_month(1))
        show_sale = showmanagersales.show_salary()
        if res is None:
            messagebox.showerror("Error","data is none")
            return
        id_name = comm.get_id_to_name()
        num = [0,"","",0,0,0,0]
        for r in res:
            name = id_name[r[0]-1][1]
            num[2] = name
            num[1] = r[1]
            num[0] += 1
            num[3:] = r[2:6]
            show_sale.showSalaryData(num)

    def look_sales_year(self):
        comm =  mydb.Commission()
        res = list(comm.get_manager_search_month(2))
        show_sale = showmanagersales.show_salary()
        if res is None:
            messagebox.showerror("Error","data is none")
            return
        id_name = comm.get_id_to_name()
        num = [0,"","",0,0,0,0]
        num[1] = res[0][1][:4]
        id1 = res[0][0]
        for r in res:
            if id1 == r[0] and num[1] == r[1][:4]:
                #index = r[0]
                num[2] = id_name[r[0]-1][1]
                num[1] = r[1][:4]
                num[3] += r[2]
                num[4] += r[3]
                num[5] += r[4]
                num[6] += r[5]
            else:
                num[0] += 1
                show_sale.showSalaryData(num)
                num[1] = r[1][:4]
                num[2] = id_name[r[0]-1][1]
                num[3] = r[2]
                num[4] = r[3]
                num[5] = r[4]
                num[6] = r[5]
        num[0] += 1
        show_sale.showSalaryData(num)
        
    def look_salary_year(self):
        comm =  mydb.Commission()
        res = list(comm.get_manager_search_month(2))
        show_sale = showmanagersales.show_salary()
        if res is None:
            messagebox.showerror("Error","data is none")
            return
        id_name = comm.get_id_to_name()
        num = [0,"","",0,0,0,0]
        num[1] = res[0][1][:4]
        id1 = res[0][0]
        for r in res:
            if id1 == r[0] and num[1] == r[1][:4]:
                #index = r[0]
                num[2] = id_name[r[0]-1][1]
                num[1] = r[1][:4]
                num[3] += r[2]
                num[4] += r[3]
                num[5] += r[4]
                num[6] += r[5]-r[6]
            else:
                num[0] += 1
                #num[8] = num[6]-num[7]
                show_sale.showSalaryData(num)
                num[1] = r[1][:4]
                num[2] = id_name[r[0]-1][1]
                num[3] = r[2]
                num[4] = r[3]
                num[5] = r[4]
                num[6] = r[5]-r[6]
        num[0] += 1
        show_sale.showSalaryData(num)
    def look_salary_month(self):
        comm =  mydb.Commission()
        res = list(comm.get_manager_search_month(1))
        show_sale = showmanagersales.show_salary()
        if res is None:
            messagebox.showerror("Error","data is none")
            return
        id_name = comm.get_id_to_name()
        num = [0,"","",0,0,0,0]
        for r in res:
            name = id_name[r[0]-1][1]
            num[2] = name
            num[1] = r[1]
            num[0] += 1
            num[3:6] = r[2:5]
            num[6] = r[5] - r[6]
            show_sale.showSalaryData(num)
    def help(self):
        messagebox.showinfo("help","this is a commission system")