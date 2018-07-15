#coding:utf8
import requests
import bs4
import pprint
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

url = "http://www.weather.com.cn/weather/101300101.shtml" #南宁天气网址

response = requests.get(url)
response.encoding='utf-8'
soup = bs4.BeautifulSoup(response.text,'html.parser')

def get_weather_seven(soup):
    list1 = soup.select('ul[class="t clearfix"] > li')
    res = []
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
        res.append(weather)
    return res

def get_life_num(soup):
    life_num = soup.select("ul[class='clearfix'] > li")
    res = []
    #tmp = ""
    res.append(life_num[0].select("em")[0].string+":"+life_num[0].select("span")[0].string+" "+life_num[0].select("p")[0].string)
    res.append(life_num[1].select("p")[0].string)
    res.append(life_num[2].select("em")[0].string+":"+life_num[2].select("span")[0].string+" "+life_num[2].select("p")[0].string)
    res.append(life_num[3].select("span")[0].string+" "+life_num[3].select("p")[0].string)
    res.append(life_num[4].select("em")[0].string+":"+life_num[4].select("span")[0].string+" "+life_num[4].select("p")[0].string)
    res.append(life_num[5].select("em")[0].string+":"+life_num[5].select("span")[0].string+" "+life_num[5].select("p")[0].string)
    tmp = "\n".join(res)
    pprint.pprint(tmp)
    return tmp

res = get_weather_seven(soup)
life = get_life_num(soup)
body = "\n".join(res) + "     " + life

my_sender='3295468820@qq.com'    # 发件人邮箱账号
my_pass = 'nlropspeooyvdaii'              # 发件人邮箱密码(当时申请smtp给的口令)
my_user='1602983878@qq.com'      # 收件人邮箱账号
def mail(body):
    ret=True
    try:
        msg=MIMEText(body,'plain','utf-8')
        msg['From']=formataddr(["发件人昵称",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["收件人昵称",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="给最最最可爱的姝姝"                # 邮件的主题，也可以说是标题

        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()# 关闭连接
    except Exception:# 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret

ret=mail(body)
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
    

#send_message_to_phone(res)    
pprint.pprint(body)
