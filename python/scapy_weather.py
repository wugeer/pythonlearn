#coding:utf8
import requests
import bs4
import pprint
import re
import json
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

#url = "http://www.weather.com.cn/weather/101300101.shtml" #南宁天气网址

class getWeather():
    '''
    爬取中国天气网某地七天内天气
    '''
    def __init__(self,url):
        self.response = requests.get(url)
        self.response.encoding='utf-8'
        self.soup = bs4.BeautifulSoup(self.response.text,'html.parser')
        self.res = self.get_weather_seven()
        self.life = self.get_life_num()
        self.body = "\n".join(self.res) + "     " + "\n" + "\n".join(self.life)+ "\n"+"\n".join(self.get_concre_data())
        pprint.pprint(self.body)

    def get_concre_data(self):
        concre_data_time = self.soup.select("script")
        #print(concre_data_time[2].string[15:-1])
        d = json.loads(concre_data_time[2].string[15:-1])
        #pprint.pprint(d["7d"][:3])
        res = ["未来三天内详细天气信息",]
        for i in d["7d"][:3]:
            for j in i:
                res.append(re.sub(r',','    ',j[:6]+j[10:-2]))
        return res
    
    def get_weather_seven(self):#获取七天内天气
        list1 = self.soup.select('ul[class="t clearfix"] > li')
        res_weather = ["未来七天内天气信息",]
        for i in list1:
            weather = ""
            tem_i = i.select("p[class='tem'] > i")[0].string
            if i.select("p[class='tem'] > span") != []:
                tem_span = i.select("p[class='tem'] > span")[0].string
            else:
                tem_span = i.select("p[class='tem'] > span")
            win = i.select("p[class='win'] > em > span")
            weather = i.select("h1")[0].string+"    "
            weather += i.select("p[class='wea']")[0].string + "    "
            if win != []:
                if len(win) == 1:
                    weather += win[0]["title"]
                elif len(win) == 2:
                    weather += win[0]["title"] + "转"+win[1]["title"]
            weather += "  "+i.select("p[class='win'] > i")[0].string+"    "
            if tem_span != []:
                weather += (tem_span+" ~ "+tem_i)
            elif tem_i != []:
                weather += tem_i
            res_weather.append(weather)
        return res_weather
    
    def get_life_num(self):   #获取当天天气的健康提示信息
        life_num = self.soup.select("ul[class='clearfix'] > li")
        res_life = ["今天健康提示",]
        res_life.append(life_num[0].select("em")[0].string+":"+life_num[0].select("span")[0].string+" "+life_num[0].select("p")[0].string)
        res_life.append(life_num[1].select("p")[0].string)
        res_life.append(life_num[2].select("em")[0].string+":"+life_num[2].select("span")[0].string+" "+life_num[2].select("p")[0].string)
        res_life.append(life_num[3].select("span")[0].string+" "+life_num[3].select("p")[0].string)
        res_life.append(life_num[4].select("em")[0].string+":"+life_num[4].select("span")[0].string+" "+life_num[4].select("p")[0].string)
        res_life.append(life_num[5].select("em")[0].string+":"+life_num[5].select("span")[0].string+" "+life_num[5].select("p")[0].string)
        return res_life
    
    
class send_email_of_weather():
    '''
    发送邮件
    '''
    def __init__(self,receiver,subject,body):
        self.sender = '3295468820@qq.com'    # 发件人邮箱账号
        self.psd = 'nlropspeooyvdaii'       # 发件人邮箱密码(当时申请smtp给的口令)
        if receiver is not None:
            for i in receiver:
                if i == '1602983878@qq.com':
                    subject = "给最最最可爱的姝姝"
                ret = self.mail(i,subject,body)
                if ret:
                    print("邮件发送%s成功"%i)
                else:
                    print("邮件发送%s失败"%i)
    #my_sender='3295468820@qq.com'    # 发件人邮箱账号
    #my_pass = 'nlropspeooyvdaii'              # 发件人邮箱密码(当时申请smtp给的口令)
    #receiver='1602983878@qq.com'      # 收件人邮箱账号
    def mail(self,receiver,subject,body):
        ret=True
        try:
            msg=MIMEText(body,'plain','utf-8')
            msg['From']= formataddr(["发件人昵称",self.sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To']= formataddr(["收件人昵称",receiver])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            #msg['Subject']="给最最最可爱的姝姝"                # 邮件的主题，也可以说是标题
            msg['Subject']= subject
            
            server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
            server.login(self.sender, self.psd)  # 括号中对应的是发件人邮箱账号、邮箱密码
            
            server.sendmail(self.sender,[receiver,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            #print("login ok")
            server.quit()# 关闭连接
        except Exception:# 如果 try 中的语句没有执行，则会执行下面的 ret=False
            print("Failed to send email to "+receiver)
            ret=False
        return ret

if __name__ == '__main__':
    #url顺序是博白天气，南宁天气，哈尔滨天气
    url = ["http://www.weather.com.cn/weather/101300902.shtml","http://www.weather.com.cn/weather/101300101.shtml","http://www.weather.com.cn/weather/101050101.shtml"]
    receiver = [["2311077029@qq.com","1423237806@qq.com","2019607084@qq.com"],
                ["1194157042@qq.com",'1602983878@qq.com'],
                ["3295468820@qq.com"]]#'1602983878@qq.com'
    subject = ["博白天气","南宁天气","哈尔滨天气"]
    #my_dict = {"给最最最可爱的姝姝":['1602983878@qq.com'] ,"博白天气":["2311077029@qq.com","2311077029@qq.com"],"南宁天气":["1194157042@qq.com"]}
    j = 0
    for i in url:
        weather = getWeather(i)
        body = weather.body
        send_email = send_email_of_weather(receiver[j],subject[j],body)
        j += 1
