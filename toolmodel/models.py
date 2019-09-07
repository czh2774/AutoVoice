from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class user(models.Model):
    class Meta:
        verbose_name = '唯彩账号'
        verbose_name_plural = '唯彩账号'

    mobile = models.IntegerField(verbose_name='手机号')
    password = models.CharField(max_length=180, verbose_name='密码')
    isuse = models.CharField(max_length=180)
    isdead = models.IntegerField(verbose_name='是否死亡')
    utk = models.CharField(max_length=180)
    token = models.CharField(max_length=180)
    user_id = models.CharField(max_length=180)
    nutk = models.CharField(max_length=180)
    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now=True)


class note(models.Model):
    class Meta:
        verbose_name = '广告语'
        verbose_name_plural = '广告语'

    note1 = models.CharField(max_length=180, verbose_name='广告语1')
    note2 = models.CharField(max_length=180, null=True, blank=True, verbose_name='广告语2')
    note3 = models.CharField(max_length=180, null=True, blank=True, verbose_name='广告语3')
    note4 = models.CharField(max_length=180, null=True, blank=True, verbose_name='广告语4')
    isdead = models.IntegerField(null=True, blank=True, verbose_name='已被封，默认不填')
    user = models.CharField(max_length=180, null=True, blank=True, verbose_name='填写者')
    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now=True)


class wxname(models.Model):
    class Meta:
        verbose_name = '微信'
        verbose_name_plural = '微信'

    wxname1 = models.CharField(max_length=180)
    wxname2 = models.CharField(max_length=180, null=True, blank=True)
    wxname3 = models.CharField(max_length=180, null=True, blank=True)
    wxname4 = models.CharField(max_length=180, null=True, blank=True)
    isdead = models.IntegerField(null=True, blank=True)
    user = models.CharField(max_length=180, null=True, blank=True)
    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now=True)


class proxyip(models.Model):
    class Meta:
        verbose_name = '代理IP'
        verbose_name_plural = '代理IP'

    host = models.CharField(max_length=180, null=True, blank=True)
    port = models.CharField(max_length=180, null=True, blank=True)
    hiding = models.CharField(max_length=180, null=True, blank=True)
    proxy_http_http = models.CharField(max_length=180, null=True, blank=True)
    isdead = models.CharField(max_length=180, null=True, blank=True)
    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now=True)


class rid(models.Model):
    class Meta:
        verbose_name = '唯彩会直播间列表'
        verbose_name_plural = '唯彩会直播间列表'

    rid = models.CharField(max_length=180, primary_key=True, verbose_name='房间ID')
    home = models.CharField(max_length=180, verbose_name='主队')
    guest = models.CharField(max_length=180, verbose_name='客队')
    chatCount = models.CharField(max_length=180, verbose_name='房间人数')
    isdead = models.IntegerField(null=True, blank=True, verbose_name='已经结束')
    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now=True)


class log_voice(models.Model):
    class Meta:
        verbose_name = '唯彩会喊话器日志'
        verbose_name_plural = '唯彩会喊话器日志'

    log_title = models.CharField(max_length=180, verbose_name='日志类型')
    log_data = models.CharField(max_length=180, verbose_name='日志数据')

    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now=True)


class cookies_hiyuncai(models.Model):
    cookies = models.CharField(max_length=180, verbose_name='cookies')


class bifen_mofang(models.Model):
    class Meta:
        verbose_name = '足球魔方比分数据'
        verbose_name_plural = '足球魔方比分数据'

    match_id = models.CharField(max_length=180, primary_key=True, verbose_name='比赛ID')
    name_league = models.CharField(max_length=180, null=True, blank=True, verbose_name='联赛名称')
    time = models.CharField(max_length=180, null=True, blank=True, verbose_name='比赛时间')
    status = models.CharField(max_length=180, null=True, blank=True, verbose_name='比赛状态')
    home_name = models.CharField(max_length=180, null=True, blank=True, verbose_name='主队名称')
    home_ranking = models.CharField(max_length=180, null=True, blank=True, verbose_name='主队排名')
    matchHomeScore = models.CharField(max_length=180, null=True, blank=True, verbose_name='主队得分')
    away_name = models.CharField(max_length=180, null=True, blank=True, verbose_name='客队名称')
    away_ranking = models.CharField(max_length=180, null=True, blank=True, verbose_name='客队排名')
    matchAwayScore = models.CharField(max_length=180, null=True, blank=True, verbose_name='客队得分')
    add_date = models.DateTimeField(verbose_name='保存日期', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='最后修改日期', auto_now=True)


class FootballWealthUser(models.Model):
    class Meta:
        verbose_name = '足球财富排行榜'
        verbose_name_plural = '足球财富排行榜'
        ordering = ('vote_number',)

    user_id = models.IntegerField(primary_key=True, verbose_name='作者ID')
    username = models.CharField(max_length=180, null=True, blank=True, verbose_name='作者名称')
    has_game = models.CharField(max_length=180, null=True, blank=True, verbose_name='？？')
    is_author = models.CharField(max_length=180, null=True, blank=True, verbose_name='？？')
    is_follow = models.CharField(max_length=180, null=True, blank=True, verbose_name='是否关注')
    rc = models.CharField(max_length=180, null=True, blank=True, verbose_name='红')
    wc = models.CharField(max_length=180, null=True, blank=True, verbose_name='走')
    bc = models.CharField(max_length=180, null=True, blank=True, verbose_name='黑')
    rr = models.CharField(max_length=180, null=True, blank=True, verbose_name='周返还率')
    sr = models.CharField(max_length=180, null=True, blank=True, verbose_name='周胜率')
    vote_number = models.IntegerField(null=True, blank=True, verbose_name='票数')
    poster = models.CharField(max_length=180, null=True, blank=True, verbose_name='头像')
    phone = models.CharField(max_length=180, null=True, blank=True, verbose_name='手机号')


class FootballWealthPost(models.Model):
    class Meta:
        verbose_name = '足球财富文章列表'
        verbose_name_plural = '足球财富文章列表'

    post_id = models.IntegerField(primary_key=True, verbose_name='推荐ID')
    user_id = models.IntegerField(null=True, blank=True, verbose_name='作者ID')
    username = models.CharField(max_length=180, null=True, blank=True, verbose_name='作者名称')
    content = models.TextField(null=True, blank=True, verbose_name='推荐正文')
    create_time = models.CharField(max_length=180, null=True, blank=True, verbose_name='创建时间')
    week_vote_number = models.IntegerField(null=True, blank=True, verbose_name='票数')


class FootballWealthRecommend(models.Model):
    class Meta:
        verbose_name = '足球财富推荐'
        verbose_name_plural = '足球财富推荐'

    away = models.CharField(verbose_name='客队名称', max_length=180, null=True, blank=True)  # "away":"鹿岛鹿角"
    awayScore = models.CharField(verbose_name='客队比分', max_length=180, null=True, blank=True)  # "awayScore":"3"
    bd_yz_hjspl = models.CharField(verbose_name='北单_yz_hjspl', max_length=180, null=True,
                                   blank=True)  # 'bd_yz_hjspl': '0.94'
    bd_yz_hjspl_checked = models.IntegerField(verbose_name='北单_yz_hjspl_checked', null=True,
                                              blank=True)  # 'bd_yz_hjspl_checked': 0
    bd_yz_hjspl_red = models.IntegerField(verbose_name='北单_yz_hjspl_red', null=True, blank=True)  # 'bd_yz_hjspl_red': 0
    bd_yz_hjspl_str = models.CharField(verbose_name='北单_yz_hjspl_str', max_length=180, null=True,
                                       blank=True)  # 'bd_yz_hjspl_str': '主让0.5'
    bd_yz_jspk = models.CharField(verbose_name='北单_yz_jspk', max_length=180, null=True,
                                  blank=True)  # 'bd_yz_jspk': '-0.5'
    bd_yz_result = models.IntegerField(verbose_name='北单_yz_结果', null=True, blank=True)  # 'bd_yz_result': 2
    bd_yz_rr = models.CharField(verbose_name='北单_yz_rr', max_length=180, null=True, blank=True)  # 'bd_yz_rr': '0'
    bd_yz_sr = models.CharField(verbose_name='北单_yz_胜率？', max_length=180, null=True, blank=True)  # 'bd_yz_sr': '0'
    bd_yz_wjspl = models.CharField(verbose_name='北单_yz_wjspl', max_length=180, null=True,
                                   blank=True)  # 'bd_yz_wjspl': '0.94'
    bd_yz_wjspl_checked = models.IntegerField(verbose_name='北单_yz_wjspl_checked', null=True,
                                              blank=True)  # 'bd_yz_wjspl_checked': 1
    bd_yz_wjspl_red = models.IntegerField(verbose_name='北单_yz_wjspl_red', null=True, blank=True)  # 'bd_yz_wjspl_red': 0
    bd_yz_wjspl_str = models.CharField(verbose_name='亚盘盘口？', max_length=180, null=True,
                                       blank=True)  # 'bd_yz_wjspl_str': '客受让0.5'
    chapter_count = models.IntegerField(verbose_name='chapter_count', null=True, blank=True)  # 'chapter_count': 1
    check_rr = models.CharField(verbose_name='check_rr', max_length=180, null=True, blank=True)  # 'check_rr': '0.00'
    check_sr = models.CharField(verbose_name='check_sr', max_length=180, null=True, blank=True)  # 'check_sr': '0.00'
    comment_id = models.IntegerField(verbose_name='评论ID', null=True, blank=True)  # "comment_id":1738867
    create_time = models.CharField(verbose_name='推荐比赛时间', max_length=180, null=True,
                                   blank=True)  # "create_time":1567568901549
    dxq_desc = models.CharField(verbose_name='大小球_desc', max_length=180, null=True, blank=True)  # 'dxq_desc': '大小球'
    dxq_hjspl = models.CharField(verbose_name='大小球_hjspl', max_length=180, null=True, blank=True)  # 'dxq_hjspl': '0.83'
    dxq_hjspl_checked = models.IntegerField(verbose_name='大小球_hjspl_checked', null=True,
                                            blank=True)  # 'dxq_hjspl_checked': 0
    dxq_hjspl_red = models.IntegerField(verbose_name='大小球_hjspl_red', null=True, blank=True)  # 'dxq_hjspl_red': 0
    dxq_hjspl_str = models.CharField(verbose_name='大小球_hjspl_str', max_length=180, null=True,
                                     blank=True)  # 'dxq_hjspl_str': '大2.50'
    dxq_is_end = models.IntegerField(verbose_name='大小球_is_end', null=True, blank=True)  # 'dxq_is_end': 1
    dxq_jspk = models.CharField(verbose_name='大小球_jspk', max_length=180, null=True, blank=True)  # 'dxq_jspk': '2.50'
    dxq_result = models.IntegerField(verbose_name='大小球_结果', null=True, blank=True)  # 'dxq_result': 0
    dxq_rr = models.CharField(verbose_name='大小球_rr', max_length=180, null=True, blank=True)  # 'dxq_rr': '0'
    dxq_sr = models.CharField(verbose_name='大小球_胜率', max_length=180, null=True, blank=True)  # 'dxq_sr': '0'
    dxq_wjspl = models.CharField(verbose_name='大小球_wjspl', max_length=180, null=True, blank=True)  # 'dxq_wjspl': '1.03'
    dxq_wjspl_checked = models.IntegerField(verbose_name='大小球_wjspl_checked', null=True,
                                            blank=True)  # 'dxq_wjspl_checked': 0
    dxq_wjspl_red = models.IntegerField(verbose_name='大小球_wjspl_red', null=True, blank=True)  # 'dxq_wjspl_red': 0
    dxq_wjspl_str = models.CharField(verbose_name='大小球_wjspl_str', max_length=180, null=True,
                                     blank=True)  # 'dxq_wjspl_str': '小.50'
    game_type = models.IntegerField(verbose_name='游戏类型', null=True, blank=True)  # 'game_type': 4
    has_dxq = models.IntegerField(verbose_name='has_大小球', null=True, blank=True)  # 'has_dxq': 0
    has_op = models.IntegerField(verbose_name='????', null=True, blank=True)  # 'has_op': 0
    has_yz = models.IntegerField(verbose_name='has_yz', null=True, blank=True)  # 'has_yz': 1
    home = models.CharField(verbose_name='主队名称', max_length=180, null=True, blank=True)  # "home":"浦和红钻"
    homeScore = models.CharField(verbose_name='主队比分', max_length=180, null=True, blank=True)  # "homeScore":"2"
    id = models.IntegerField(primary_key=True, verbose_name='推荐ID')
    ID_bet007 = models.CharField(verbose_name='ID_bet007', max_length=180, null=True,
                                 blank=True)  # "ID_bet007":"1767712"
    is_end = models.IntegerField(verbose_name='比赛是否结束', null=True, blank=True)  # "is_end":1
    is_show = models.IntegerField(verbose_name='是否显示', null=True, blank=True)  # 'is_show': 1
    league = models.CharField(verbose_name='比赛日期', max_length=180, null=True, blank=True)  # "league":"日联杯"
    letball = models.CharField(verbose_name='让球', max_length=180, null=True, blank=True)  # "letball":"让球"
    match_id = models.CharField(verbose_name='比赛场次', max_length=180, null=True, blank=True)  # "match_id":"周三002"
    match_time1 = models.CharField(verbose_name='比赛日期', max_length=180, null=True, blank=True)  # 'match_time1': '09/04'
    match_time2 = models.CharField(verbose_name='比赛小时', max_length=180, null=True, blank=True)  # 'match_time2': '02:45'
    MatchTimeStamp = models.CharField(verbose_name='比赛时间',max_length=180, null=True, blank=True, )  # "MatchTimeStamp":1567593000000
    op_is_end = models.IntegerField(verbose_name='？？？', null=True, blank=True)  # 'op_is_end': 1
    post_id = models.IntegerField(verbose_name='推荐所属文章ID', null=True, blank=True)  # "post_id":72317
    rq_goal = models.CharField(verbose_name='让球数', max_length=180, null=True, blank=True)  # "rq_goal":"+1"
    rq_rq0 = models.CharField(verbose_name='让球负赔率', max_length=180, null=True, blank=True)  # "rq_rq0":"4.30"
    rq_rq0_checked = models.IntegerField(verbose_name='让球负检查', null=True, blank=True)  # "rq_rq0_checked":0
    rq_rq0_red = models.IntegerField(verbose_name='让球负red', null=True, blank=True)  # "rq_rq0_red":0
    rq_rq1 = models.CharField(verbose_name='让球平赔率', max_length=180, null=True, blank=True)  # "rq_rq1":"3.80"
    rq_rq1_checked = models.IntegerField(verbose_name='让球平检查', null=True, blank=True)  # "rq_rq1_checked":0
    rq_rq1_red = models.IntegerField(verbose_name='让球平red', null=True, blank=True)  # "rq_rq1_red":0
    rq_rq3 = models.CharField(verbose_name='让球胜赔率', max_length=180, null=True, blank=True)  # "rq_rq3":"1.51"
    rq_rq3_checked = models.IntegerField(verbose_name='让球胜检查', null=True, blank=True)  # "rq_rq3_checked":0
    rq_rq3_red = models.IntegerField(verbose_name='让球胜red', null=True, blank=True)  # "rq_rq3_red":0
    rq_sf_result = models.IntegerField(verbose_name='让球胜负结果', null=True, blank=True)  # "rq_sf_result":1
    rq_sf_rr = models.CharField(verbose_name='让球胜率', max_length=180, null=True, blank=True)  # "rq_sf_rr":"0"
    rq_sf_sr = models.CharField(verbose_name='让球胜率', max_length=180, null=True, blank=True)  # "rq_sf_sr":"100.00"
    rr = models.CharField(verbose_name='rr', max_length=180, null=True, blank=True)  # 'rr': '0'
    sf_goal = models.CharField(verbose_name='胜平负让球数', max_length=180, null=True, blank=True)  # "sf_goal":"0"
    sf_sf0 = models.CharField(verbose_name='胜平负负', max_length=180, null=True, blank=True)  # "sf_sf0":"2.10"
    sf_sf0_checked = models.IntegerField(verbose_name='胜平负负检查', null=True, blank=True)  # "sf_sf0_checked":1
    sf_sf0_red = models.IntegerField(verbose_name='胜平负负red', null=True, blank=True)  # "sf_sf0_red":1
    sf_sf1 = models.CharField(verbose_name='胜平负平赔率', max_length=180, null=True, blank=True)  # "sf_sf1":"3.35"
    sf_sf1_checked = models.IntegerField(verbose_name='胜平负平检查', null=True, blank=True)  # "sf_sf1_checked":1
    sf_sf1_red = models.IntegerField(verbose_name='胜平负平red', null=True, blank=True)  # "sf_sf1_red":0
    sf_sf3 = models.CharField(verbose_name='胜平负胜赔率', max_length=180, null=True, blank=True)  # "sf_sf3":"2.60"
    sf_sf3_checked = models.IntegerField(verbose_name='胜负胜检查', null=True, blank=True)  # "sf_sf3_checked":0
    sf_sf3_red = models.IntegerField(verbose_name='胜平负胜red', null=True, blank=True)  # "sf_sf3_red":0
    sort = models.IntegerField(verbose_name='分类', null=True, blank=True)  # "sort":277
    spf_goal = models.CharField(verbose_name='胜平负_goal', max_length=180, null=True, blank=True)  # 'spf_goal': '0'
    spf_result = models.IntegerField(verbose_name='胜平负结果', null=True, blank=True)  # 'spf_result': 0
    spf_rr = models.CharField(verbose_name='胜平负胜率', max_length=180, null=True, blank=True)  # 'spf_rr': '0'
    spf_sf0 = models.CharField(verbose_name='胜平负_负', max_length=180, null=True, blank=True)  # 'spf_sf0': '无'
    spf_sf0_checked = models.IntegerField(verbose_name='胜平负_负_checked', null=True, blank=True)  # 'spf_sf0_checked': 0
    spf_sf0_red = models.IntegerField(verbose_name='胜平负', null=True, blank=True)  # 'spf_sf0_red': 0
    spf_sf1 = models.CharField(verbose_name='胜平负_平', max_length=180, null=True, blank=True)  # 'spf_sf1': '无'
    spf_sf1_checked = models.IntegerField(verbose_name='胜平负_平_checked', null=True, blank=True)  # 'spf_sf1_checked': 0
    spf_sf1_red = models.IntegerField(verbose_name='胜平负_平_red', null=True, blank=True)  # 'spf_sf1_red': 0
    spf_sf3 = models.CharField(verbose_name='胜平负_胜', max_length=180, null=True, blank=True)  # 'spf_sf3': '无'
    spf_sf3_checked = models.IntegerField(verbose_name='胜平负_胜_checked', null=True, blank=True)  # 'spf_sf3_checked': 0
    spf_sf3_red = models.IntegerField(verbose_name='胜平负_胜_red', null=True, blank=True)  # 'spf_sf3_red': 0
    spf_sr = models.CharField(verbose_name='胜平负_胜率', max_length=180, null=True, blank=True)  # 'spf_sr': '0'
    sr = models.CharField(verbose_name='胜率sr', max_length=180, null=True, blank=True)  # 'sr': '0'
    state = models.IntegerField(verbose_name='推荐结果', null=True, blank=True)  # "state":-1
    strand_id = models.IntegerField(verbose_name='串ID', null=True, blank=True)  # "strand_id":24055
    user_id = models.IntegerField(verbose_name='作者ID', null=True, blank=True)  # "user_id":151525
    yz_desc = models.CharField(verbose_name='亚盘玩法？', max_length=180, null=True, blank=True)  # 'yz_desc': '亚盘'
    yz_is_end = models.IntegerField(verbose_name='yz_is_end', null=True, blank=True)  # 'yz_is_end': 1
