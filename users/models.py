from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):

    gender_choices = (
        ('male','男'),
        ('female','女')
    )

    nick_name = models.CharField('昵称',max_length=50,default='')
    ender = models.CharField('性别',max_length=10,choices=gender_choices,default='female')
    address = models.CharField('地址',max_length=100,default='')
    mobile = models.CharField('手机号',max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to='image/%Y%m',default='image/default.png',max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    send_choices = (
        ('register','注册'),
        ('forget','找回密码'),
        ('update_email','修改邮箱')
    )

    code = models.CharField('验证码',max_length=20)
    email = models.EmailField('邮箱',max_length=50)
    send_type = models.CharField(choices=send_choices,max_length=30)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name
