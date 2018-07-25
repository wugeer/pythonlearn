import tkinter  
from  tkinter import ttk  
  
class show_salary(object):
    def __init__(self):
        super().__init__()
        self.window = tkinter.Tk()
        self.window.title("salary")
        self.setup_ui()
    def setup_ui(self):
        self.tree=ttk.Treeview(self.window)
        self.tree["columns"]=("time","lock_num","stock_num","barrel_num","salary")  
        self.tree.column("time",width=100)   
        self.tree.column("lock_num",width=100)  
        self.tree.column("stock_num",width=100)  
        self.tree.column("barrel_num",width=100)
        self.tree.column("salary",width=100)  

        self.tree.heading("time",text="time")  
        self.tree.heading("lock_num",text="lock_num")  
        self.tree.heading("stock_num",text="stock_num")
        self.tree.heading("barrel_num",text="barrel_num")
        self.tree.heading("salary",text="salary")  

        self.tree.pack()  
        
    def showSalaryData(self,data):
        self.tree.insert("",data[0],text=str(data[0]) ,values=(data[1],data[2],data[3],data[4],data[5]))
        
  

