import pymysql
import tkinter.messagebox as messagebox
import manager
import tkinter as tk
import user
import pprint

class Commission(tk.Tk):
    def __init__(self):
        self.conn = self.getConn()
        if self.conn is None:
            messagebox.showerror("Error","fail to connect to mysql database!")
            return
        self.conn.autocommit(True)
  
    def getConn(self):
        try:
            self.conn = pymysql.connect(host="localhost",user="root",passwd="xiehongwang",db="commission",charset="utf8")
        except pymysql.Error as e:
            messagebox.showerror("Error",e)
        finally:
           return self.conn

    def getCommission(self):
        cursor = self.conn.cursor()
        cursor.execute("truncate table commission")#取巧了
        self.conn.commit()
        searchsql_1 = "select user_id,user_name,sale_time,lock_num,stock_num,barrel_num from sales order by user_id;"
        cursor.execute(searchsql_1)
        res = list(cursor.fetchall())
        if res is not None:
            month = str(res[0][2])[:7]
            usr = res[0][0]
            m = [0,0,0]
            p = [usr,month,0,0,0,0,0.,0.]
            for r in res:
                day = str(r[2])[:7]
                if usr == r[0] and month == day:
                    m[0] += r[3]
                    m[1] += r[4]
                    m[2] += r[5]
                else:
                    if 0 not in m:
                        p[2] = 1
                    p[6] = m[0]*45+m[1]*30+m[2]*25
                    p[5],p[4],p[3] = m
                    m = [0,0,0]
                    m[0] += r[3]
                    m[1] += r[4]
                    m[2] += r[5]
                    if p[2] != 0:
                        if p[6] <= 1000:
                            p[7] = p[6]*0.1
                        elif p[6] <= 1800:
                            p[7] = p[6]*0.15
                        else:
                            p[7] = p[6]*0.2
                    else:
                        p[7] = 0.0
                    self.insert_to_commission(p)
                    usr = r[0]
                    month = day
                    p = [usr,month,0,0,0,0,0.,0.]

        #pprint.pprint(res)

    def insert_to_commission(self,p):
        try:
            cursor = self.conn.cursor()
            insert_sql = "insert into commission values(%d,'%s',%d,%d,%d,%d,%d,%d)"%(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7])
            cursor.execute(insert_sql)
            self.conn.commit()
        except pymysql.Error as e:
            self.conn.rollback()
            print(e)

    def get_records_form_id(self,id):
        try:
            cursor = self.conn.cursor()
            s_sql = "select sale_time,lock_num,stock_num,barrel_num,sale_amount,salary from commission where user_id = '%d' ;"%(id)
            cursor.execute(s_sql)
            res = list(cursor.fetchall())
            return res
        except pymysql.Error as e:
            self.conn.rollback()
            print(e)
    def get_id_from_name(self,name):
        try:
            cursor = self.conn.cursor()
            s_sql = "select user_id from person where user_name = '%s';"%name
            cursor.execute(s_sql)
            res = list(cursor.fetchone())
            return res
        except pymysql.Error as e:
            self.conn.rollback()
            print(e)

    def get_id_to_name(self):
        try:
            cursor = self.conn.cursor()
            s_sql = "select user_id,user_name from person order by user_id;"
            cursor.execute(s_sql)
            res = list(cursor.fetchall())
            return res
        except pymysql.Error as e:
            self.conn.rollback()
            print(e)
            #return
        #finally:
            #self.conn.close()
            
    def get_user_search_month(self,info):
        try:
            self.user_name,self.priot = info[0],info[1]
            self.cursor = self.conn.cursor()
            #if self.priot == 2:
            search_sql = "select user_id from person where user_name = '%s' and priot = %d;"%(self.user_name,self.priot)
            self.cursor.execute(search_sql)
            self.user_id = self.cursor.fetchone()
            search_sql2 = "select sale_time,lock_num,stock_num,barrel_num,salary from commission where user_id = '%d' ;"%(self.user_id)
            self.cursor.execute(search_sql2)
            self.res = list(self.cursor.fetchall())
        except pymysql.Error as e:
            self.conn.rollback()
            print(e)
            #return
        finally:
            #self.conn.close()
            return list(self.res)
    def get_manager_search_month(self,cl):
        try:
            cursor = self.conn.cursor()
            search_sql = "select user_id,sale_time,lock_num,stock_num,barrel_num,sale_amount,salary from commission "
            if cl == 1:
                search_sql += " order by sale_time;"
            else:
                search_sql += " order by user_id"
            cursor.execute(search_sql)
            res = list(cursor.fetchall())
        except pymysql.Error as e:
            self.conn.rollback()
            print(e)
            #return
        finally:
            #self.conn.close()
            return list(res)
    def login(self,userinfo):
        if userinfo[0] == "" or userinfo[1] == "":
            return
        if self.conn is None:
            messagebox.showerror("Error","fail to connect to mysql database!")
            return
        try:
            search_sql = "select user_pass from person where user_name = '%s' and priot = %d;"%(userinfo[0],userinfo[1])
            self.cursor = self.conn.cursor()
            self.cursor.execute(search_sql)
            rs = self.cursor.fetchone()
            if rs is None:
                messagebox.showerror("Error","nothing fetch")
            else:
                if userinfo[2] in rs:
                    messagebox.showinfo("Success","login success")
                    self.getCommission()
                    if userinfo[1] == 1:
                        us = manager.user(userinfo)
                    else:
                        us = user.user(userinfo)
                else:
                    messagebox.showerror("Error","count and password error")
        except pymysql.Error as e:
            self.conn.rollback()
            print(e)
        #finally:
            #self.conn.close()

    def addUser(self,userinfo):
        try:
            self.checkNameAvailable(userinfo[0],userinfo[4])
            cursor = self.conn.cursor()
            sql = "select * from person;"
            cursor.execute(sql)
            rs = cursor.fetchall()
            self.id = len(rs)+1
            userinfo.insert(1,self.id)
            print(userinfo)
            insert_sql = "insert into person(user_name,user_id,user_tele,user_addr,user_age,priot,user_pass) values('%s',%d,%d,'%s',%d,%d,'%s');"%(userinfo[0],userinfo[1],userinfo[2],userinfo[3],userinfo[4],userinfo[5],userinfo[6])
            print(insert_sql)
            cursor.execute(insert_sql)
            self.conn.commit()
           # cursor.close()
            messagebox.showinfo("success","add user ok")
        except pymysql.Error as e:
            self.conn.rollback()
            print(e)
        #finally:
         #   self.conn.close()
            
            

    def checkNameAvailable(self,name,priot):
        try:
            cursor = self.conn.cursor()
            sql = "select * from person where user_name = '%s' and priot = %d;"%(str(name),int(priot))
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 0:
                messagebox.showerror("error","the user doesn't exist")
                raise Exception("user %s doesn't exist"%name)
        except pymysql.Error as e:
            self.conn.rollback()
            print(e)
        #finally:
        #    cursor.close()