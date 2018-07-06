from django.db import models

from datetime import datetime

class Category(models.Model):
    '''种类'''
    cate = models.TextField("分类")
    desc = models.TextField("desc",default="")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "category"

    def __str__(self):
        return self.cate


class Push_date(models.Model):
    '''种类'''
    date = models.TextField("发布日期")

    class Meta:
        verbose_name = "发布日期"
        verbose_name_plural = "发布日期"

    def __str__(self):
        return self.date


class Video(models.Model):
    '''视频'''
    name = models.TextField("名字")
    desc = models.TextField("描述")
    author = models.TextField("作者", default='佚名')
    actor = models.TextField("演员",default='佚名')
    video_url = models.TextField(default='')
    image_url = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    add_time = models.DateTimeField("添加时间",default=datetime.now,)
    push_date = models.ForeignKey(Push_date, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = "视频"

    def __str__(self):
        return self.name


