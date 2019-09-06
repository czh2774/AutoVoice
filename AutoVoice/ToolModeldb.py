# -*- coding: utf-8 -*-
import logging
from django.http import HttpResponse
import toolmodel.tools.vipc
from toolmodel.voice_vipc import voice_vipc,voice_tool
from toolmodel import models
import random
# 生成唯彩账号
def vipc_getuser(request):
    data=[]

    for i in range(1,50):
        try:
            ob=toolmodel.tools.vipc.vipc_data()
            value=ob.user_reqister()
            logging.debug(value)
            dic=value
            data.append(dic.copy())
            models.user.objects.create(**dic)
        except:
            logging.error('注册账号出错,继续下一个')
            continue


    logging.info('当前注册成功%d,账号列表%s',len(data),data)
    return HttpResponse("<p>本次添加的手机号%s</p>",str(len(data)))
#从数据库中获取唯彩账号并传输至请求端
def vipc_user(request):
    response = []
    ob=models.user.objects
    list = ob.all()
    for i in list:
        response.append(i.mobile)
    data=response[random.randint(0,len(response)-1)]
    ob.filter(mobile=data).update(isuse=1)
    return HttpResponse(data)
#从数据库中获取话术并传输至请求端
def vipc_note(request):
    if (request.method == 'POST'):
        print("the POST method")
        concat = request.POST
        concat=concat['name']
        print(concat)
    response=[]
    data=[]
    ob=models.note.objects
    list=ob.all()
    #print(request)


    for i in list:
        #print(i)
        response.append(i)
    response = response[random.randint(0, len(response) - 1)]
    #print(type(response))
    if response.note1:
        data.append(response.note1)
        if response.note2:
            data.append(response.note2)
            if response.note3:
                data.append(response.note3)
                if response.note4:
                    data.append(response.note4)
                else:
                    pass
            else:
                pass
        else:
            pass
    data=str(data)[1:-1]
    data=data.replace("'",'')
    return HttpResponse(data)
#从数据库中获取微信账号并传输至请求端
def vipc_wxname(request):

    return HttpResponse("<p>数据添加成功！</p>")
def vipc_getip(request):

    return HttpResponse("<p>数据添加成功！</p>")
def vipc_rid(request):

    return HttpResponse("<p>数据添加成功！</p>")
def vipc_port(request):
    if (request.method == 'POST'):
        print("the POST method")
        concat=request.POST
        postBody=request.body
        print(concat['name'][0])
        print(postBody)

    #print(HttpRequest.method)

    return HttpResponse("<p>数据添加成功！</p>")

def vipc_voice(request):

    #获取房间数据




    room_list=voice_vipc()
    room_list=room_list.voice_room()
    #进行喊话



    return HttpResponse("<p>开始喊话！</p>")

if __name__ == '__main__':
    #data=vipc_user()
    cookies_ob=voice_vipc(mobile='15159903754')
    cookies=cookies_ob.get_cookies()
    print(cookies)