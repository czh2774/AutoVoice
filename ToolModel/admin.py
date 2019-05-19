
from django.contrib import admin

from ToolModel.models import user




from django.contrib import admin
from ToolModel.models import user
from ToolModel.models import wxname
from ToolModel.models import note
from ToolModel.models import proxyip
from ToolModel.models import rid
from ToolModel.models import log_voice
# Register your models here.

# Blog模型的管理器
@admin.register(user)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'mobile', 'password', 'isuse','isdead','utk','token','user_id','nutk','add_date','mod_date')

@admin.register(wxname)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('wxname1', 'wxname2', 'wxname3', 'wxname4','isdead','user','add_date','mod_date')

@admin.register(note)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('note1', 'note2', 'note3', 'note4','isdead','user','add_date','mod_date')

@admin.register(proxyip)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('host', 'port','hiding','proxy_http_http' ,'isdead','add_date','mod_date')

@admin.register(rid)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('rid', 'home', 'guest', 'chatCount','isdead','add_date','mod_date')

@admin.register(log_voice)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('log_title', 'log_data','add_date','mod_date')

