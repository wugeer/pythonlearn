import time 
import serial
import csv
import pprint
import os
import matplotlib.pyplot as plt
import pymysql
from twilio.rest import Client
import matplotlib.dates as mdate
import pandas as pd

def main():
    ser = serial.Serial("COM3") #注意选择串口号,从0开始计数,我的是COM3,所以参数是2
    line = ser.readline() 
    ti = [i for i in range(1,100)]
    k = 0
    num = 1
    res = []
    p = []
    cnt = 0
    mytime = "2018-06-23 00:00:00"
    year = "2018-12-31 23:59:59"
    try:
        while line: 
            t = time.strftime("%Y-%m-%d %X\t")
            num = int(line.strip())
            
            print(time.strftime("%Y-%m-%d %X\t") + str(line.strip()))
            if len(res) > 0 and res[len(res)-1][0] == t:
                p.append([t,num])
            else:
                if len(p) > 0:
                    sum = 0
                    for i in p:
                        sum += i[1]
                    sum += res[len(res)-1][1]
                    res[len(res)-1][1] = sum/(len(p)+1)
                    p = []
                else:
                    p = [t,num]
                    res.append(p)
                    #cnt += 1 
                    p = []
            if len(res) > 30:
                insert_data(res)
                res = []
                #cnt = 0
                k += 1
            if num > 120:
                cnt += 1
            else:
                cnt = 0
            if cnt >= 5:
                send_message_to_phone()
                cnt = 0
            line = ser.readline()
            if t >= mytime:
                paint_day(t)
                mytime = t
            if t > year:
                paint_year(year)
                year = t[:4]+"-12-31 23:59:59"
    except IndexError as e:
        print(e)
        
def paint_day(time):#单独画三个图
    x = []
    y = []
    try:
        conn = getConn()
        cursor = conn.cursor()
        search_sql = "select day,num from fog_data where day > '%s'"%(time)
        cursor.execute(search_sql)
        res = list(cursor.fetchall())
        for r in res:
            x.append(str(r[0])[-8:])
            y.append(r[1])
        pprint.pprint(x)
        pprint.pprint(y)
        for i in range(0,3):
            save_pic(x,y,time[:10],i)
    except pymysql.Error as e:
            conn.rollback()
            print(e)
    finally:
        conn.close()
        
def paint_year(time):
    x = []
    y = []
    try:
        conn = getConn()
        cursor = conn.cursor()
        search_sql = "select day,num from fog_data where day > '%s'"%(time)
        cursor.execute(search_sql)
        res = list(cursor.fetchall())
        for r in res:
            x.append(str(r[0]))
            y.append(r[1])
        pprint.pprint(x)
        pprint.pprint(y)
        for i in range(0,3):
            save_pic(x,y,time[:4],i)
    except pymysql.Error as e:
            conn.rollback()
            print(e)
    finally:
        conn.close()
def save_pic(x,y,time,mode=0):
    fig1 = plt.figure(figsize=(15,5))
    ax1 = fig1.add_subplot(1,1,1)
    for tick in ax1.get_xticklabels():
        tick.set_rotation(45)
    plt.title(time)
    if mode == 0:
        plt.scatter(x,y)
        plt.savefig(time+"_scatter"+".png",dpi=300)
        print("保存scatter图成功")
    elif mode == 1:
        plt.bar(x,y)
        plt.savefig(time+"_bar"+".png",dpi=300)
        print("保存bar图成功")
    else:
        plt.plot(x,y,color = 'green',linewidth = 2.0, linestyle = '--')
        y1 = [130 for i in y]
        plt.plot(x,y1,color='red',linewidth = 1.0)
        plt.savefig(time+"_plot"+".png",dpi=300)
        print("保存plot图成功")
        
def send_message_to_phone():
    account_id = "AC8f9cc711a915b10fb6298b864c30d1db"
    auth_token = "cc1caa8e399daaab29f6b0f7d8eedb4b"
    try:
        client = Client(account_id,auth_token)
        message = client.messages.create(to="+8618845756853",from_="+14424447480",body="fog too much")
        print("短信发送成功!")
    except:
        print("短信发送失败!")
    
def insert_data(r):
    try:
        conn = getConn()
        cursor = conn.cursor()
        search = "select * from fog_data;"
        cursor.execute(search)
        res = list(cursor.fetchall())
        cnt = len(res)+1
        pprint.pprint(r)
        for i in r:
            insert_sql = "insert into fog_data values(%d,'%s',%d)"%(cnt,i[1],int(i[2]))
            cursor.execute(insert_sql)
            conn.commit()
            cnt += 1
            print("insert ok ")
    except pymysql.Error as e:
            conn.rollback()
            print(e)
    finally:
        conn.close()
        
def getConn():
    try:
        conn = pymysql.connect(host="localhost",user="root",passwd="xiehongwang",db="fog",charset="utf8")
    except pymysql.Error as e:
            print(e)
    finally:
        return conn
        
if __name__ == "__main__":
    main()
    #paint_day("2018-06-22 00:00:00")
    #paint_year("2018-01-01 00:00:00")
    
