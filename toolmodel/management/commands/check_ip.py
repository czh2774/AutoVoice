from django.core.management.base import BaseCommand, CommandError

from toolmodel.voice_vipc import voice_tool
class Command(BaseCommand):  # 必须继承

    def handle(self, *args, **options):  # 必须实现的方法 ，该方法即自定义命令执行的内容
        data=voice_tool()
        data.check_ip()