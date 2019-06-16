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

class cookies_hiyuncai(models.Model):
    cookies = models.CharField(max_length=255, verbose_name='cookies')

class bifen_mofang(models.Model):
    class Meta:
        verbose_name='足球魔方比分数据'
        verbose_name_plural='足球魔方比分数据'
    match_id=models.CharField(max_length=255,primary_key=True,verbose_name='比赛ID')
    name_league=models.CharField(max_length=255,null=True,blank=True,verbose_name='联赛名称')
    time=models.CharField(max_length=255,null=True,blank=True,verbose_name='比赛时间')
    status=models.CharField(max_length=255,null=True,blank=True,verbose_name='比赛状态')
    home_name=models.CharField(max_length=255,null=True,blank=True,verbose_name='主队名称')
    home_ranking=models.CharField(max_length=255,null=True,blank=True,verbose_name='主队排名')
    matchhomescore=models.CharField(max_length=255,null=True,blank=True,verbose_name='主队得分')
    away_name=models.CharField(max_length=255,null=True,blank=True,verbose_name='客队名称')
    away_ranking=models.CharField(max_length=255,null=True,blank=True,verbose_name='客队排名')
    matchawayscore=models.CharField(max_length=255,null=True,blank=True,verbose_name='客队得分')
    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now=True)
#class data_hiyuncai(models.Model):
class zuqiumofang_user(models.Model):
    class Meta:
        verbose_name = '足球财富排行榜'
        verbose_name_plural = '足球财富排行榜'
        ordering=('ranking',)
    user_id =models.CharField(max_length=255,primary_key=True,verbose_name='作者ID')
    ranking = models.IntegerField(max_length=255, null=True, blank=True, verbose_name='排名')
    username = models.CharField(max_length=255, null=True, blank=True, verbose_name='作者名称')
    nickname=models.CharField(max_length=255, null=True, blank=True, verbose_name='昵称')
    has_game=models.CharField(max_length=255,null=True,blank=True,verbose_name='？？')
    is_author=models.CharField(max_length=255,null=True,blank=True,verbose_name='？？')
    is_follow=models.CharField(max_length=255,null=True,blank=True,verbose_name='是否关注')
    rc=models.CharField(max_length=255,null=True,blank=True,verbose_name='红')
    wc = models.CharField(max_length=255, null=True, blank=True, verbose_name='走')
    bc = models.CharField(max_length=255, null=True, blank=True, verbose_name='黑')
    rr=models.CharField(max_length=255,null=True,blank=True,verbose_name='周返还率')
    sr=models.CharField(max_length=255,null=True,blank=True,verbose_name='周胜率')
    vote_number=models.IntegerField(max_length=255,null=True,blank=True,verbose_name='票数')
    poster = models.CharField(max_length=255, null=True, blank=True, verbose_name='？？')

class zuqiumofang_post(models.Model):
    class Meta:
        verbose_name = '足球财富文章列表'
        verbose_name_plural = '足球财富文章列表'
    post_id=models.CharField(max_length=255,primary_key=True,verbose_name='推荐ID')
    user_id=models.CharField(max_length=255,null=True, blank=True,verbose_name='作者ID')
    ranking = models.IntegerField(max_length=255, null=True, blank=True, verbose_name='排名')
    username = models.CharField(max_length=255, null=True, blank=True, verbose_name='作者名称')
    content=models.TextField(null=True, blank=True,verbose_name='推荐正文')
    create_time=models.DateTimeField(max_length=255,null=True, blank=True,verbose_name='创建时间')
    strandlist=models.TextField(null=True, blank=True,verbose_name='推荐单')

class zuqiumofang_tuijian(models.Model):
    class Meta:
        verbose_name = '足球财富推荐'
        verbose_name_plural = '足球财富推荐'
    id=models.IntegerField(max_length=255,primary_key=True,verbose_name='推荐ID')
    post_id=models.CharField(max_length=255,null=True, blank=True,verbose_name='文章ID')
    user_id=models.CharField(max_length=255,null=True, blank=True,verbose_name='作者ID')
    nickname=models.CharField(max_length=255,null=True, blank=True,verbose_name='作者昵称')
    match_id=models.CharField(max_length=255,null=True, blank=True,verbose_name='比赛ID')
    home=models.CharField(max_length=255,null=True, blank=True,verbose_name='主队')
    away=models.CharField(max_length=255,null=True, blank=True,verbose_name='客队')
    ID_bet007=models.CharField(max_length=255,null=True, blank=True,verbose_name='比赛ID')
    create_time=models.DateTimeField(null=True, blank=True,verbose_name='推荐时间')
    tuijian=models.TextField(max_length=255,null=True, blank=True,verbose_name='玩法列表')
    ranking = models.IntegerField(max_length=255, null=True, blank=True, verbose_name='排名')
    rc = models.CharField(max_length=255, null=True, blank=True, verbose_name='红')
    wc = models.CharField(max_length=255, null=True, blank=True, verbose_name='走')
    bc = models.CharField(max_length=255, null=True, blank=True, verbose_name='黑')
    tongji=models.CharField(max_length=255, null=True, blank=True, verbose_name='推荐')
    state=models.IntegerField( null=True, blank=True, verbose_name='结果')