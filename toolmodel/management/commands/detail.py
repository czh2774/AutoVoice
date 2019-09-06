from django.core.management.base import BaseCommand, CommandError

from toolmodel.tools.zuqiucaifu import zuqiucaifu
class Command(BaseCommand):  # 必须继承

    def handle(self, *args, **options):  # 必须实现的方法 ，该方法即自定义命令执行的内容
        data=zuqiucaifu()
        data.detail()
        data.tuijian()