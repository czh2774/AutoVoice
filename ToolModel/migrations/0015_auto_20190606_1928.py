# Generated by Django 2.2.1 on 2019-06-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToolModel', '0014_auto_20190606_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zuqiumofang_user',
            name='vote_number',
            field=models.IntegerField(blank=True, max_length=255, null=True, verbose_name='票数'),
        ),
    ]
