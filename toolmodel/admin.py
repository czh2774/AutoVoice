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
        'user_id', 'username', 'has_game', 'is_author', 'is_follow', 'rc', 'wc', 'bc', 'rr', 'sr', 'vote_number',
        'poster',)


@admin.register(FootballWealthPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'user_id', 'username', 'content', 'create_time')


@admin.register(FootballWealthRecommend)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'post_id', 'user_id', 'match_id', 'home', 'away', 'ID_bet007', 'create_time']
