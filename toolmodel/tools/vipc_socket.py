#!/usr/bin/python
# -*- coding:utf-8 -*-
import websocket
import time
from threading import Timer,Event,Thread

class HeartbeatThread(Thread):
    """心跳"""

    def __init__(self,event,ws):
        super(HeartbeatThread,self).__init__()
        self.event=event
        self.ws=ws

    def run(self):
        while 1:
            #发送ping包
            self.ws.send('2')
            self.event.wait(timeout=2)

    def on_message(ws,message):
        """接收消息"""
        print(message)

    def on_error(ws,error):
        print(error)

    def on_close(ws):
        print('### closed ###')

    def on_open(ws):
        """请求连接"""
        ws.send("2probe")

    def on_emit(ws):
        #创建心跳线程
        event=Event()
        heartbeat=HeartbeatThread(event,ws)
        heartbeat.start()

        while 1:
            content=input("input")
            #发送信息
            #4：engine.io message
            #2:socket.io event
            #chat message event message
            ws.send('42["chat message","{0}"]'.format(content))
            time.sleep(.2)

if __name__=="__main__":
    websocket.enableTrace(True)
    # url 格式
    # ws://host:port/socket.io/?EIO=3&transport=websocket
    ws=websocket.websocketApp(
        "ws://live.vipc.cn/socket.io/?EIO=3&transport=websocket",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open=on_open

    t=Timer(3,on_emit,args=(ws,))
    t.start()

    ws.run_forever