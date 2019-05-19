#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
"""
1、确定当前谁在干活
2、
"""

def note_data():
    list=[]
    with open('note.txt','r',encoding='utf8') as f:
        note_txt=f.readlines()
        for i in note_txt:
            list.append(i)
    #list=['杀人夜','呵呵','无话可说','无语','收了','你觉得呢','进一个啊','真是的']
    num=random.randrange(0,len(list))
    print(list[num])
    return list[num]
if __name__ == '__main__':
    note_data()