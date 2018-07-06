from datetime import datetime

from django.db import models

from users.models import UserProfile
from videos.models import Video





class VideoComments(models.Model):
    '''视频评论'''
    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Video,verbose_name='视频',on_delete=models.CASCADE)
    comments = models.CharField('评论',max_length=200)
    add_time = models.DateTimeField('添加时间', default=datetime.now)


    class Meta:
        verbose_name = '视频评论'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    fav_id = models.IntegerField('数据id',default=0)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class ChildComment(models.Model):
    '''子评论'''
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    comments = models.CharField('评论', max_length=200)
    add_time = models.DateTimeField('添加时间', default=datetime.now)
    fa = models.ForeignKey(VideoComments, verbose_name='子评论', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '视频评论'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField('接受用户',default=0)
    message = models.CharField('消息内容',max_length=500)
    has_read = models.BooleanField('是否已读',default=False)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name
