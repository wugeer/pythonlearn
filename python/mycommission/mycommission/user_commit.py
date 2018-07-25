import tkinter as tk
import mydb
import tkinter.messagebox as messagebox
import pymysql
import re
import datetime

class usr_op(tk.Tk):
    def __init__(self,userinfo):
        super().__init__()
        self.user_name = userinfo[0]
        self.priot = userinfo[1]
        self.title("commit")
        self.commit_ui()

    def commit_ui(self):
        '''
        row1 = tk.Frame(self)
        row1.pack()
        tk.Label(row1,text="time:",width=8,justify='right').grid(row=0,column=0)
        self.time = tk.StringVar()
        self.time.set("")
        tk.Entry(row1,textvariable=self.time,width=20).grid(row=0,column=1)

        row1 = tk.Frame(self)
        row1.pack()
        tk.Label(row1,text="locate:",width=8,justify='right').grid(row=0,column=0)
        self.locate = tk.StringVar()
        self.locate.set("")
        tk.Entry(row1,textvariable=self.locate,width=20).grid(row=0,column=1)'''

        row1 = tk.Frame(self)
        row1.pack()
        tk.Label(row1,text="stock:",width=8,justify='right').grid(row=0,column=0)
        self.stock = tk.IntVar()
       # self.stock.set("")
        tk.Entry(row1,textvariable=self.stock,width=20).grid(row=0,column=1)

        row2 = tk.Frame(self)
        row2.pack()
        tk.Label(row2,text="lock:",width=8,justify='right').grid(row=1,column=0)
        self.lock = tk.IntVar()
      #  self.lock.set("")
        tk.Entry(row2,textvariable=self.lock,width=20).grid(row=1,column=1)

        row3 = tk.Frame(self)
        row3.pack()
        tk.Label(row3,text="barrel:",width=8,justify='right').grid(row=2,column=0)
        self.barrel = tk.IntVar()
      #  self.lock.set("")
        tk.Entry(row3,textvariable=self.barrel,width=20).grid(row=2,column=1)

        row4 = tk.Frame(self)
        row4.pack()
        tk.Button(row4,text="confim",command=self.commit_ok).grid(row=3,column=0)
        tk.Button(row4,text="cancel",command=self.cancel).grid(row=3,column=1)

    def commit_ok(self):
        if self.lock.get() < 0 or self.stock.get() < 0 or self.barrel.get() < 0:
            messagebox.showerror("commit error","please check you input to confim there is not empty")
            return
        try:
            errorstr = ""
            search_sql = "select user_id from person where user_name = '%s' and priot = %d;"%(self.user_name,self.priot)
            self.conn = mydb.Commission().getConn()
            self.cursor = self.conn.cursor()
            self.cursor.execute(search_sql)
            self.user_id = self.cursor.fetchone()
            now = datetime.datetime.now()
            time_str = "%s/%s/%s"%(now.year,now.month,now.day)
            self.info = [self.user_id[0],self.user_name,time_str,"hdkdajlk",self.lock.get(),self.stock.get(),self.barrel.get()]
            insert_sql = "insert into sales values(%d,'%s','%s','%s',%d,%d,%d);"%(self.info[0],self.info[1],self.info[2],self.info[3],self.info[4],self.info[5],self.info[6])
            #print(insert_sql)
            self.cursor.execute(insert_sql)
            self.conn.commit()
            mydb.Commission().getCommission()
            messagebox.showinfo("success","ok")
        except pymysql.Error as e:
            self.conn.rollback()
            print(e)
        finally:
            self.conn.close()
            self.destroy()

    def cancel(self):
        self.destroy()