import xadmin

from .models import UserMessage, VideoComments, UserFavorite


class UserMessageAdmin(object):
    '''用户消息后台'''

    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']



class VideoCommentsAdmin(object):
    '''用户评论后台'''

    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']



class UserFavoriteAdmin(object):
    '''用户收藏后台'''

    list_display = ['user', 'fav_id', 'add_time']
    search_fields = ['user', 'fav_id']
    list_filter = ['user', 'fav_id', 'add_time']


# 将后台管理器与models进行关联注册。
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(VideoComments, VideoCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)