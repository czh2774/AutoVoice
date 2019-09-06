#coding=utf8
from werobot import WeRoBot

robot = WeRoBot(enable_session=False,
                token='czh2774',
                APP_ID='wx25679f2d1a926280',
                APP_SECRET='51d108100585a1e0d38bfa38fa453df9')

@robot.handler
def hello(message):
    return 'Hello world'