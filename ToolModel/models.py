from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class user(models.Model):
    class Meta:
        verbose_name = '唯彩账号'
        verbose_name_plural = '唯彩账号'
    mobile=models.CharField(max_length=255,)
    password=models.CharField(max_length=255)
    isuse=models.CharField(max_length=255)
    isdead=models.CharField(max_length=254)
    utk=models.CharField(max_length=255)
    token=models.CharField(max_length=255)
    user_id=models.CharField(max_length=255)
    nutk=models.CharField(max_length=255)
    add_date = models.DateTimeField(verbose_name='保存日期', default = timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now = True)

class note(models.Model):
    class Meta:
        verbose_name = '广告语'
        verbose_name_plural = '广告语'
    note1=models.CharField(max_length=255,verbose_name='广告语1')
    note2 = models.CharField(max_length=255,null=True,blank=True,verbose_name='广告语2')
    note3 = models.CharField(max_length=255,null=True,blank=True,verbose_name='广告语3')
    note4 = models.CharField(max_length=255,null=True,blank=True,verbose_name='广告语4')
    isdead=models.CharField(max_length=255,null=True,blank=True,verbose_name='已被封，默认不填')
    user=models.CharField(max_length=255,null=True,blank=True,verbose_name='填写者')
    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now=True)
class wxname(models.Model):
    class Meta:
        verbose_name = '微信'
        verbose_name_plural = '微信'
    wxname1 = models.CharField(max_length=255)
    wxname2 = models.CharField(max_length=255,null=True,blank=True)
    wxname3 = models.CharField(max_length=255,null=True,blank=True)
    wxname4 = models.CharField(max_length=255,null=True,blank=True)
    isdead=models.CharField(max_length=255,null=True,blank=True)
    user=models.CharField(max_length=255,null=True,blank=True)
    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now=True)
class proxyip(models.Model):
    class Meta:
        verbose_name = '代理IP'
        verbose_name_plural = '代理IP'

    host=models.CharField(max_length=255,null=True,blank=True)
    port = models.CharField(max_length=255,null=True,blank=True)
    hiding=models.CharField(max_length=255,null=True,blank=True)
    proxy_http_http=models.CharField(max_length=255,null=True,blank=True)
    isdead=models.CharField(max_length=255,null=True,blank=True)
    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now=True)

class rid(models.Model):
    class Meta:
        verbose_name = '唯彩会直播间列表'
        verbose_name_plural = '唯彩会直播间列表'

    rid=models.CharField(max_length=255,primary_key=True,verbose_name='房间ID')
    home = models.CharField(max_length=255,verbose_name='主队')
    guest = models.CharField(max_length=255,verbose_name='客队')
    chatCount = models.CharField(max_length=255,verbose_name='房间人数')
    isdead=models.CharField(max_length=255,null=True,blank=True,verbose_name='已经结束')
    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now=True)

class log_voice(models.Model):
    class Meta:
        verbose_name='唯彩会喊话器日志'
        verbose_name_plural='唯彩会喊话器日志'

    log_title=models.CharField(max_length=255,verbose_name='日志类型')
    log_data = models.CharField(max_length=255, verbose_name='日志数据')

    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now=True)