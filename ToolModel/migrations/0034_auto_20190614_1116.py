# Generated by Django 2.2.1 on 2019-06-14 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToolModel', '0033_auto_20190614_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zuqiumofang_tuijian',
            name='tuijian_id',
            field=models.IntegerField(blank=True, max_length=255, null=True, verbose_name='推荐ID'),
        ),
    ]
