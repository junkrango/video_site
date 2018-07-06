import xadmin

from .models import EmailVerifyRecord
from xadmin import views


# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = '后台管理界面'
    # 修改footer
    site_footer = '公司'
    # 收起菜单
    # menu_style = 'accordion'

#xadmin中这里是继承object，不再是继承admin
class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']


# class UserProfileAdmin(object):
#     list_display = ['nick_name', 'ender', 'address', 'mobile']
#     search_fields = ['nick_name', 'ender', 'address', 'mobile']
#     list_filter = ['nick_name', 'ender', 'address', 'mobile']




xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
# xadmin.site.register(UserProfile,UserProfileAdmin)


# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)

# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)