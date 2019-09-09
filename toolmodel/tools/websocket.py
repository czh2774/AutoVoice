#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import re
from mitmproxy import ctx,http




def websocket_message(flow):
    # get the latest message
    message = flow.messages[-1]
    ctx.log.info(message.content)
    if 'create' in str(message.content):
    # simply print the content of the message
        ctx.log.info(message.content)

    #str(static.note_socket())
    # manipulate the message content
    if '12331' in str(message.content):
        print('有这个数')
        message.content = re.sub(r'12331','dada', message.content)

