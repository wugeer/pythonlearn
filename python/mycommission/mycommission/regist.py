import tkinter as tk
import tkinter.simpledialog
import tkinter.messagebox as messagebox
import mydb
import pymysql

class MyRegist(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("regist")
        self.setup_ui()

    def setup_ui(self):
        row1 = tk.Frame(self)
        row1.pack()
        tk.Label(row1,text="name:",width=12,justify='right').grid(row=0,column=0)
        self.name = tk.StringVar()
        self.name.set("")
        tk.Entry(row1,textvariable=self.name,width=20).grid(row=0,column=1)
        #tk.Label(row1,text = "please input english and < 8",width=50,justify='left').grid(row=0,column = 2)
       
        row2 = tk.Frame(self)
        row2.pack()
        tk.Label(row2,text="password:",width=12,justify='right').grid(row=1,column=0)
        self.password = tk.StringVar()
        self.password.set("")
        tk.Entry(row2,textvariable=self.password,width=20,show="*").grid(row=1,column=1)
        #tk.Label(row2,text = "6-10",width=50,justify='left').grid(row=1,column = 2)
        
        row3 = tk.Frame(self)
        row3.pack()
        tk.Label(row3,text="confirm pass:",width=12,justify='right').grid(row=2,column=0)
        self.comfirm_pass = tk.StringVar()
        self.comfirm_pass.set("")
        tk.Entry(row3,textvariable=self.comfirm_pass,width=20,show="*").grid(row=2,column=1)
        #tk.Label(row3,text = "6-10",width=50,justify='left').grid(row=2,column = 2)

        row4 = tk.Frame(self)
        row4.pack()
        tk.Label(row4,text="age:",width=12,justify='right').grid(row=3,column=0)
        self.age = tk.StringVar()
        self.age.set("")
        tk.Entry(row4,textvariable=self.age,width=20).grid(row=3,column=1)
        #tk.Label(row4,text = ">0 and < 70",width=50,justify='left').grid(row=3,column = 2)

        row5 = tk.Frame(self)
        row5.pack()
        tk.Label(row5,text="telephon:",width=12,justify='right').grid(row=4,column=0)
        self.tele = tk.StringVar()
        self.tele.set("")
        tk.Entry(row5,textvariable=self.tele,width=20).grid(row=4,column=1)
        #tk.Label(row1,text = "11numbers",width=50,justify='left').grid(row=4,column = 2)

        row6 = tk.Frame(self)
        row6.pack()
        tk.Label(row6,text="address:",width=12,justify='right').grid(row=4,column=0)
        self.addr = tk.StringVar()
        self.addr.set("")
        tk.Entry(row6,textvariable=self.addr,width=20).grid(row=4,column=1)
        #tk.Label(row1,text = "<20char",width=50,justify='left').grid(row=1,column = 2)

        row7 = tk.Frame(self)
        row7.pack()
        tk.Label(row7,text="class:",width=12,justify='right').grid(row=5,column=0)
        self.v = tk.IntVar()
        self.v.set(2)
        tk.Radiobutton(row7,text="manager",variable =self.v,value = 1).grid(row=5,column=1)
        tk.Radiobutton(row7,text="user",variable =self.v,value = 2).grid(row=5,column=2)

        row8 = tk.Frame(self)
        row8.pack()
        tk.Button(row8,text="comfirm",command=self.ok).grid(row=7,column=0)
        tk.Button(row8,text="cancel",command=self.cancel).grid(row=7,column=1)

    def ok(self):
        if self.name.get()=="" or self.password.get()=="" or self.comfirm_pass.get()=="" or self.age.get()=="" or self.tele.get()=="" or self.addr.get()=="":
            messagebox.showerror("regist error","please check you input to confirm there is not empty")
            return
        if self.password.get() != self.comfirm_pass.get():
            messagebox.showerror("regist error","password is not right")
            return
        try:
            errstr = ""
            if len(str(int(self.tele.get()))) != 11:
                errstr += "please confirm the number of telephon is 11;"
            if len(self.name.get()) > 8:
                errstr += "the length of name is outof 8;"
            if len(self.addr.get()) > 20:
                errstr += "the length of addr is outof 20;"
            if int(self.age.get()) < 0 and int(self.age.get()) > 70:
                errstr += "the num of age is less than 0 or more than 70;"
            self.userinfo = [str(self.name.get()),int(self.tele.get()),str(self.addr.get()),int(self.age.get()),int(self.v.get()),str(self.password.get())]
            self.comm = mydb.Commission()
            self.comm.addUser(self.userinfo)
        except:
            messagebox.showinfo("Error","please check you input;"+errstr)
            return
        self.destroy()

    def cancel(self):
        self.destroy()