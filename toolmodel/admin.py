from django.contrib import admin
from toolmodel.models import user
from toolmodel.models import wxname
from toolmodel.models import note
from toolmodel.models import proxyip
from toolmodel.models import rid
from toolmodel.models import log_voice
from toolmodel.models import bifen_mofang
from toolmodel.models import FootballWealthUser
from toolmodel.models import FootballWealthPost
from toolmodel.models import FootballWealthRecommend


# Register your models here.

# Blog模型的管理器
@admin.register(user)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'mobile', 'password', 'isuse', 'isdead', 'utk', 'token', 'user_id', 'nutk', 'add_date', 'mod_date')


@admin.register(wxname)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('wxname1', 'wxname2', 'wxname3', 'wxname4', 'isdead', 'user', 'add_date', 'mod_date')


@admin.register(note)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('note1', 'note2', 'note3', 'note4', 'isdead', 'user', 'add_date', 'mod_date')


@admin.register(proxyip)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('host', 'port', 'hiding', 'proxy_http_http', 'isdead', 'add_date', 'mod_date')


@admin.register(rid)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('rid', 'home', 'guest', 'chatCount', 'isdead', 'add_date', 'mod_date')


@admin.register(log_voice)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('log_title', 'log_data', 'add_date', 'mod_date')


@admin.register(bifen_mofang)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'match_id', 'name_league', 'time', 'status', 'home_name', 'home_ranking', 'matchHomeScore', 'away_name',
        'away_ranking', 'matchAwayScore', 'add_date', 'mod_date')


@admin.register(FootballWealthUser)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 'username', 'has_game', 'is_author', 'is_follow', 'rc', 'wc', 'bc', 'rr', 'sr', 'vote_number')


@admin.register(FootballWealthPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'user_id', 'username', 'content', 'create_time', 'week_vote_number')


@admin.register(FootballWealthRecommend)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["away", "awayScore", "bd_yz_hjspl", "bd_yz_hjspl_checked", "bd_yz_hjspl_red", "bd_yz_hjspl_str",
                    "bd_yz_jspk", "bd_yz_result", "bd_yz_rr", "bd_yz_sr", "bd_yz_wjspl", "bd_yz_wjspl_checked",
                    "bd_yz_wjspl_red", "bd_yz_wjspl_str", "chapter_count", "check_rr", "check_sr", "comment_id",
                    "create_time", "dxq_desc", "dxq_hjspl", "dxq_hjspl_checked", "dxq_hjspl_red", "dxq_hjspl_str",
                    "dxq_is_end", "dxq_jspk", "dxq_result", "dxq_rr", "dxq_sr", "dxq_wjspl", "dxq_wjspl_checked",
                    "dxq_wjspl_red", "dxq_wjspl_str", "game_type", "has_dxq", "has_op", "has_yz", "home", "homeScore",
                    "id", "ID_bet007", "is_end", "is_show", "league", "letball", "match_id", "match_time1",
                    "match_time2", "MatchTimeStamp", "op_is_end", "post_id", "rq_goal", "rq_rq0", "rq_rq0_checked",
                    "rq_rq0_red", "rq_rq1", "rq_rq1_checked", "rq_rq1_red", "rq_rq3", "rq_rq3_checked", "rq_rq3_red",
                    "rq_sf_result", "rq_sf_rr", "rq_sf_sr", "rr", "sf_goal", "sf_sf0", "sf_sf0_checked", "sf_sf0_red",
                    "sf_sf1", "sf_sf1_checked", "sf_sf1_red", "sf_sf3", "sf_sf3_checked", "sf_sf3_red", "sort",
                    "spf_goal", "spf_result", "spf_rr", "spf_sf0", "spf_sf0_checked", "spf_sf0_red", "spf_sf1",
                    "spf_sf1_checked", "spf_sf1_red", "spf_sf3", "spf_sf3_checked", "spf_sf3_red", "spf_sr", "sr",
                    "state", "strand_id", "user_id", "yz_desc", "yz_is_end" ]
