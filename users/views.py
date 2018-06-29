from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.base import View
from django.urls import reverse
from videos.models import Category,Video,Push_date

class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        # 获取用户提交的用户名和密码
        user_name = request.POST.get('username', None)
        pass_word = request.POST.get('password', None)
        # 成功返回user对象,失败None
        user = authenticate(username=user_name, password=pass_word)
        # 如果不是null说明验证成功
        if user is not None:
            # 登录
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})


class LogoutView(View):
    '''用户登出'''
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class RegisterView(View):
    '''用户注册'''
    def get(self,request):
        return render(request,'register.html')


# class IndexView(View, **kwargs):
#     def get(self,request):
#         all_videos = Video.objects.all()
#         all_categorys = Category.objects.all()
#         return render(request,'index.html',{
#             'all_categorys': all_categorys,
#             'all_videos':all_videos,
#         })

class SearchView(View):
    def get(self,request,cate_id):
        all_video = Video.objects.all()
        all_videos = all_video.filter(category_id=int(cate_id))
        return render(request,'index.html',{
            'all_videos': all_videos,
        })


class IndexView(View):
    def get(self,request):
        all_videos = Video.objects.all()
        all_categorys = Category.objects.all()
        all_date = Push_date.objects.all()
        date_id = request.GET.get('date','')
        if date_id:
            s_date = Push_date.objects.get(id=int(date_id))
            all_videos  = all_videos.filter(push_date=s_date)

        category_id = request.GET.get('cate','')
        if category_id:
            cate = Category.objects.get(id=int(category_id))
            all_videos = all_videos.filter(category=cate)

        return render(request,'index.html',{
            'all_categorys': all_categorys,
            'all_videos':all_videos,
            'all_date': all_date,
            'category_id' : category_id,
            'date_id' : date_id,
        })