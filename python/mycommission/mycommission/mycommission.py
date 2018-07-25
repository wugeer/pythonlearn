import time
import tkinter as tk
from regist import MyRegist
import tkinter.simpledialog
import tkinter.messagebox as messagebox
import mydb
import user_commit
from line_profiler import LineProfiler
class my_commission(tk.Tk):
    def __init__(self):
        super().__init__()
    
        self.title("commisson system")
        #self.window.geometry('450x300')
        self.setup_UI()
    
    def setup_UI(self):
       
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='count: ', width=10).grid(row=0,column=0,columnspan=2,ipadx=20)
        self.name = tk.StringVar()
        tk.Entry(row1, textvariable=self.name, width=20).grid(row=0,column=2,columnspan=2)
        row2 = tk.Frame(self)
        row2.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row2, text='pass: ', width=10).grid(row=1,column=0,columnspan=2,ipadx=20)
        self.password = tk.StringVar()
        tk.Entry(row2, textvariable=self.password, show = "*", width=40).grid(row=1,column=2,columnspan=4)
        
        row3 = tk.Frame(self)
        row3.pack()
        tk.Label(row3,text="class:",width=8,justify='right').grid(row=3,column=0,columnspan=2,ipadx=20)
        self.v = tk.IntVar()
        self.v.set(1)
        tk.Radiobutton(row3,text="manager",variable =self.v,value = 1).grid(row=3,column=2,columnspan=2)
        tk.Radiobutton(row3,text="putong",variable =self.v,value = 2).grid(row=3,column=4,columnspan=2)
        row4 = tk.Frame(self)
        row4.pack(fill="x")
        tk.Button(row4, text="login", command=self.login).grid(row=4,column=0,columnspan=2,padx=40)
        tk.Button(row4, text="regist", command=self.regist).grid(row=4,column=2,columnspan=2)
        tk.Button(row4, text="quit", command=self.quit).grid(row=4,column=4,columnspan=2,padx=40)

    def login(self):
        time_start = time.time()
        lp = LineProfiler()
        self.comm = mydb.Commission()
        self.userinfo = [self.name.get(),self.v.get(),self.password.get()]
        lp_wrapper = lp(self.comm.login)
        lp_wrapper(self.userinfo)
        lp.print_stats()
        time_finish = time.time()
        print("login function over ,elapse",time_finish-time_start)
        #self.comm.login(self.userinfo)
        self.destroy()
        #self.wait_visibility()

    def regist(self):
        res = self.my_regist()
        if res is None:
            print('failed')
            return

    def my_regist(self):
        inputDialog = MyRegist()
        self.wait_window(inputDialog)
        return inputDialog

if __name__ == "__main__":
    app = my_commission()
    app.mainloop()
