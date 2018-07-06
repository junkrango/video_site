import xadmin

from .models import Video,Category,Push_date


class CategoryAdmin(object):
    list_display = ["cate"]


class VideoAdmin(object):
    list_display = ['name', 'author', 'actor', 'category', 'add_time']

class Push_dateAdmin(object):
    list_display = ['date']

xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(Push_date,Push_dateAdmin)