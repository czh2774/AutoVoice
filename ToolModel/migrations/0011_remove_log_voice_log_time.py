# Generated by Django 2.1.7 on 2019-05-09 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToolModel', '0010_auto_20190510_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log_voice',
            name='log_time',
        ),
    ]
