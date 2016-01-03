
#!-*- coding:utf-8 -*-
from Tkinter import *
toutAQI=[86,98,77,
         119,103,80,144,102,62,60,51,78,104,70,
         85,72,38,40,44,42,39,43,47,74,
         83,104,92,64,57,67,90,60,63,47,
         57,98,79,163,84,43,33,43,49,60,
         82,68,58,65,45,53,55,56,57,60,
         53,60,62,65,64,42,79,36,34,23,
         42,80,97,77,82,75,58,79,69,39,
         79,102,82,72,84,79,104,80,74,97,
         65,65,84,92,52,88,72,50,55,60,
         77,74,67,101,78,70,69,70,92,89,
         94,88,97,85,132,134,77,60,57,52,
         80,122,104,107,97,87,44,54,78,80,
         100,166,112,110,170,233,158,94,83,74,
         71,103,165,144,90,72,67,81,118,74,
         108,186,163,117,178,162,88,54,88,
         108,123,88,95,149,180,156,99,95,74,77,80,75,47,41,36,77,85,55,82,
         108,218,223,117,73,172,288,215,178,99,94,140,128,67,94,165,103,51,52,69,84,142,133,182,85,82,125,80,63]

prepol=['臭氧8小时','PM2.5','PM2.5',
        'PM10','PM10','PM10','PM2.5','PM2.5',
        'PM2.5','臭氧8小时','臭氧8小时','臭氧8小时','PM2.5',
         'PM2.5','PM2.5','PM2.5','none','none',
        'none','none','none','none','none',
        '臭氧8小时','PM2.5','PM2.5','PM2.5','臭氧8小时',
        '臭氧8小时','PM2.5','PM2.5','PM2.5','PM2.5',
        'none','PM2.5','PM2.5','PM2.5','PM2.5',
        'PM2.5','none','none','none','none',
        'PM2.5','PM2.5','PM2.5','PM2.5','PM2.5',
        'none','PM10','PM10','PM10','PM10',
        'PM10','PM10','PM10','PM10','PM10',
        'PM10','none','PM2.5','none','none',
        'none','none','PM2.5','PM2.5','臭氧8小时',
        'PM2.5','PM2.5','臭氧8小时','PM2.5','臭氧8小时',
        'none','PM2.5','PM2.5','PM2.5','PM2.5',
        'PM2.5','PM2.5','PM2.5','臭氧8小时','PM2.5,臭氧8小时',
        'PM2.5','PM2.5','PM2.5','PM2.5','PM2.5',
        'PM2.5,臭氧8小时','PM2.5','PM2.5','none','臭氧8小时',
        '臭氧8小时','PM2.5','PM2.5','臭氧8小时','臭氧8小时',
        'PM2.5','PM2.5','PM2.5','PM2.5,臭氧8小时','PM2.5',
        'PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','臭氧8小时','臭氧8小时','臭氧8小时',
        '臭氧8小时','PM10','PM10','PM10','PM2.5','PM2.5','PM2.5','none','臭氧8小时','PM10,PM2.5',
        'PM2.5','PM2.5','PM2.5','PM2.5','臭氧8小时','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5',
        'PM2.5','臭氧8小时','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM10','PM10','PM2.5',
        'PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5',
        'PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5',
        'PM2.5','PM2.5','PM2.5','none','none','none','PM2.5','PM2.5','PM2.5','PM2.5',
        'PM2.5','PM2.5','PM2.5','PM2.5','PM10','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5',
        'PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM10','PM2.5','PM2.5',
        'PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5','PM2.5']

def judge():#定义一个函数看看等级
    level=toutAQI[j]
    if level<=50:
        print('tres bien')
    elif level<=100:
        print('bon')
    elif level<=150:
        print('un peu de pollution')
    elif level<=200:
        print('assez de pollution')
    elif level<=300:
        print('beaucoup de pollution')
    else:
        print('trop de pollution')
top = Tk()
aq=[]
j=0
def consulter():#一点按钮就用这个函数查询
    date=e.get()#把输入的东西存起来 通过变量来访问组件内容
    mois,jour=map(int,date.split(r"."))   #.是正则表达式的关键字，用正则表达式切割后为字符列表，可以直接用int转化，不必琐碎判断

#每个月的数字通过计算对应到上面列表里的值，各种判断，各种输出
    if mois==6:
        j=jour-8
        judge()
        s=0
        while (1):
            jy=int(toutAQI[s])
            if jy<=50:
                aq.append('tres bien')
            elif jy<=100:
                aq.append('bon')
            elif jy<=150:
                aq.append('un peu de pollution')
            elif jy<=200:
                aq.append('assez de pollution')
            elif jy<=300:
                aq.append('beaucoup de pollution')
            else:
                aq.append('trop de pollution')
            s+=1
            if s>22:
                break
        print("numTresbien is",aq.count('tres bien'))
        print("numbon is",aq.count('bon'))
        print("numunpeu is",aq.count('un peu de pollution'))
        print("numassezde is",aq.count('assez de pollution'))
        print("numbeaucoupde is",aq.count('beaucoup de pollution'))
        print("numtropde is",aq.count('trop de pollution'))
        print(prepol[0:23].count('臭氧8小时'))
        print(prepol[0:23].count('PM2.5'))
        print(prepol[0:23].count('PM10'))
    elif mois==7:
        j=jour+22
        judge()
        s=23
        while (1):
            jy=int(toutAQI[s])
            if jy<=50:
                aq.append('tres bien')
            elif jy<=100:
                aq.append('bon')
            elif jy<=150:
                aq.append('un peu de pollution')
            elif jy<=200:
                aq.append('assez de pollution')
            elif jy<=300:
                aq.append('beaucoup de pollution')
            else:
                aq.append('trop de pollution')
            s+=1
            if s>53:
                break
        print("numTresbien is",aq.count('tres bien'))
        print("numbon is",aq.count('bon'))
        print("numunpeu is",aq.count('un peu de pollution'))
        print("numassezde is",aq.count('assez de pollution'))
        print("numbeaucoupde is",aq.count('beaucoup de pollution'))
        print("numtropde is",aq.count('trop de pollution'))
        print(prepol[23:54].count('臭氧8小时'))
        print(prepol[23:54].count('PM2.5'))
        print(prepol[23:54].count('PM10'))
    elif mois==8:
        j=jour+53
        judge()
        s=54
        while (1):
            jy=int(toutAQI[s])
            if jy<=50:
                aq.append('tres bien')
            elif jy<=100:
                aq.append('bon')
            elif jy<=150:
                aq.append('un peu de pollution')
            elif jy<=200:
                aq.append('assez de pollution')
            elif jy<=300:
                aq.append('beaucoup de pollution')
            else:
                aq.append('trop de pollution')
            s+=1
            if s>83:
                break
        print("numTresbien is",aq.count('tres bien'))
        print("numbon is",aq.count('bon'))
        print("numunpeu is",aq.count('un peu de pollution'))
        print("numassezde is",aq.count('assez de pollution'))
        print("numbeaucoupde is",aq.count('beaucoup de pollution'))
        print("numtropde is",aq.count('trop de pollution'))
        print(prepol[54:84].count('臭氧8小时'))
        print(prepol[54:84].count('PM2.5'))
        print(prepol[54:84].count('PM10'))
    elif mois==9:
        j=jour+83
        judge()
        s=84
        while (1):
            jy=int(toutAQI[s])
            if jy<=50:
                aq.append('tres bien')
            elif jy<=100:
                aq.append('bon')
            elif jy<=150:
                aq.append('un peu de pollution')
            elif jy<=200:
                aq.append('assez de pollution')
            elif jy<=300:
                aq.append('beaucoup de pollution')
            else:
                aq.append('trop de pollution')
            s+=1
            if s>113:
                break
        print("numTresbien is",aq.count('tres bien'))
        print("numbon is",aq.count('bon'))
        print("numunpeu is",aq.count('un peu de pollution'))
        print("numassezde is",aq.count('assez de pollution'))
        print("numbeaucoupde is",aq.count('beaucoup de pollution'))
        print("numtropde is",aq.count('trop de pollution'))
        print(prepol[84:114].count('臭氧8小时'))
        print(prepol[84:114].count('PM2.5'))
        print(prepol[84:114].count('PM10'))
    elif mois==10:
        j=jour+113
        judge()
        s=114
        while (1):
            jy=int(toutAQI[s])
            if jy<=50:
                aq.append('tres bien')
            elif jy<=100:
                aq.append('bon')
            elif jy<=150:
                aq.append('un peu de pollution')
            elif jy<=200:
                aq.append('assez de pollution')
            elif jy<=300:
                aq.append('beaucoup de pollution')
            else:
                aq.append('trop de pollution')
            s+=1
            if s>144:
                break
        print("numTresbien is",aq.count('tres bien'))
        print("numbon is",aq.count('bon'))
        print("numunpeu is",aq.count('un peu de pollution'))
        print("numassezde is",aq.count('assez de pollution'))
        print("numbeaucoupde is",aq.count('beaucoup de pollution'))
        print("numtropde is",aq.count('trop de pollution'))
        print(prepol[114:145].count('臭氧8小时'))
        print(prepol[114:145].count('PM2.5'))
        print(prepol[114:145].count('PM10'))
    elif mois==11:
        j=jour+144
        judge()
        s=145
        while (1):
            jy=int(toutAQI[s])
            if jy<=50:
                aq.append('tres bien')
            elif jy<=100:
                aq.append('bon')
            elif jy<=150:
                aq.append('un peu de pollution')
            elif jy<=200:
                aq.append('assez de pollution')
            elif jy<=300:
                aq.append('beaucoup de pollution')
            else:
                aq.append('trop de pollution')
            s+=1
            if s>174:
                break
        print("numTresbien is",aq.count('tres bien'))
        print("numbon is",aq.count('bon'))
        print("numunpeu is",aq.count('un peu de pollution'))
        print("numassezde is",aq.count('assez de pollution'))
        print("numbeaucoupde is",aq.count('beaucoup de pollution'))
        print("numtropde is",aq.count('trop de pollution'))
        print(prepol[145:175].count('臭氧8小时'))
        print(prepol[145:175].count('PM2.5'))
        print(prepol[145:175].count('PM10'))
    elif mois==12:
        j=jour+174
        judge()
        s=175
        while (1):
            jy=int(toutAQI[s])
            if jy<=50:
                aq.append('tres bien')
            elif jy<=100:
                aq.append('bon')
            elif jy<=150:
                aq.append('un peu de pollution')
            elif jy<=200:
                aq.append('assez de pollution')
            elif jy<=300:
                aq.append('beaucoup de pollution')
            else:
                aq.append('trop de pollution')
            s+=1
            if s>201:
                break
        print("numTresbien is",aq.count('tres bien'))
        print("numbon is",aq.count('bon'))
        print("numunpeu is",aq.count('un peu de pollution'))
        print("numassezde is",aq.count('assez de pollution'))
        print("numbeaucoupde is",aq.count('beaucoup de pollution'))
        print("numtropde is",aq.count('trop de pollution'))
        print(prepol[175:201].count('臭氧8小时'))
        print(prepol[175:201].count('PM2.5'))
        print(prepol[175:201].count('PM10'))
#弄一个界面出来
Label(top,text = "Please input date like 06.01:").pack(side = LEFT)
e=StringVar()  #MVC模式开发需要给文本框View绑定一个字符串变量Model
Entry(top,textvariable=e).pack(side = RIGHT)#实现组件和变量的绑定
Button(top,text = 'print_entry',command=consulter).pack(side = BOTTOM)#调上面的函数出来看看

top.mainloop()
