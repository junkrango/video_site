# Generated by Django 2.0.2 on 2018-06-26 18:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='分类')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='名字')),
                ('desc', models.TextField(verbose_name='描述')),
                ('author', models.TextField(default='佚名', verbose_name='作者')),
                ('actor', models.TextField(default='佚名', verbose_name='演员')),
                ('video_url', models.TextField(default='')),
                ('image_url', models.TextField(default='')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('c_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='videos.Category')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': 'verbose_name',
            },
        ),
    ]