from datetime import datetime
import json

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.base import View
from django.urls import reverse
from videos.models import Category,Video,Push_date
from operation.models import VideoComments,UserFavorite,UserMessage,ChildComment
from users.models import UserProfile,EmailVerifyRecord
from .forms import RegisterForm
from .unit.email_send import send_register_email
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
            return HttpResponseRedirect(reverse('index'))
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
    def post(self,request):
        nick_name = request.POST.get('nick_name',None)
        phone = request.POST.get('phone', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        if UserProfile.objects.filter(username=nick_name):
            return render(request, 'register.html', {'msg': '用户名已存在'})
        if UserProfile.objects.filter(email=email):
            return render(request, 'register.html', {'msg': '邮箱已被使用'})
        add_user = UserProfile()
        add_user.nick_name = nick_name
        add_user.username = nick_name
        add_user.mobile = phone
        #每次生成的密码相同
        add_user.password = make_password(password)
        add_user.email = email
        add_user.save()
        send_register_email(email,"register")
        return render(request,'register.html',{'msg': '注册成功，请验证邮箱'})


class ForgetPass(View):
    def get(self,request):
        return render(request,'forget.html')
    def post(self,request):
        email = request.POST.get('email',None)
        send_register_email(email,'forget')
        return render(request,'forget.html',{'msg':'重设密码的邮件已发到邮箱'})


class ResetPass(View):
    def get(self,request):
        return render(request, 'reset.html', {"msg": "请重置密码"})
    def post(self,request):
        password = request.POST.get('password','')
        email = request.POST.get('email', '')
        match = UserProfile.objects.get(email=email)
        match.set_password(password)
        match.first_name = password
        match.save()
        return render(request, 'reset.html',{"msg": "重置密码成功"})



class ActiveUser(View):
    def get(self,request):
        code = request.GET.get('code','')
        res = EmailVerifyRecord.objects.filter(code=code)
        if res:
            for r in res:
                email = r.email
                match = UserProfile.objects.get(email=email)
                match.is_active = True
                match.save()
        else:
            return render(request,'login.html',{"msg":"账户激活失败"})
        return render(request, 'login.html', {"msg": "账户激活成功"})


class SearchView(View):
    def post(self,request):
        keywords = request.POST.get('keywords',None)
        all_videos = Video.objects.filter(name__icontains=keywords)
        return render(request,'index.html',{
            'all_videos': all_videos,
        })


class IndexView(View):
    def get(self,request):
        all_videos = Video.objects.all()
        all_categorys = Category.objects.all()
        all_date = Push_date.objects.all()
        date_id = request.GET.get('date','')
        all_videos_res = all_videos
        if date_id:
            s_date = Push_date.objects.get(id=int(date_id))
            all_videos_date  = all_videos.filter(push_date=s_date)
            # 对首页进行分页
            # 尝试获取前台get请求传递过来的page参数
            # 如果是不合法的配置参数默认返回第一页
            paginator = Paginator(all_videos_date, 60)  # 每页显示 60
            page = request.GET.get('page')
            try:
                all_videos_res = paginator.page(page)
            except PageNotAnInteger:
                # 如果用户请求的页码号不是整数，显示第一页
                all_videos_res = paginator.page(1)
            except EmptyPage:
                # 如果用户请求的页码号超过了最大页码号，显示最后一页
                all_videos_res = paginator.page(paginator.num_pages)

        category_id = request.GET.get('cate','')
        if category_id:
            cate = Category.objects.get(id=int(category_id))
            all_videos_cate = all_videos.filter(category=cate)
            # 对首页进行分页
            # 尝试获取前台get请求传递过来的page参数
            # 如果是不合法的配置参数默认返回第一页
            paginator = Paginator(all_videos_cate, 60)  # 每页显示 60

            page = request.GET.get('page')
            try:
                all_videos_res = paginator.page(page)
            except PageNotAnInteger:
                # 如果用户请求的页码号不是整数，显示第一页
                all_videos_res = paginator.page(1)
            except EmptyPage:
                # 如果用户请求的页码号超过了最大页码号，显示最后一页
                all_videos_res = paginator.page(paginator.num_pages)

        return render(request,'index.html',{
            'all_categorys': all_categorys,
            'all_videos':all_videos_res,
            'all_date': all_date,
            'category_id' : category_id,
            'date_id' : date_id,
        })


class Comment(View):
    def post(self,request):
        comment = request.POST.get('comment',None)
        video_id = request.GET.get('video_id','')
        video = Video.objects.get(id=int(video_id))
        add_comment = VideoComments()
        add_comment.user = request.user
        add_comment.course = video
        add_comment.comments = comment
        add_comment.save()
        video_detail = Video.objects.get(id=int(video_id))
        comments = VideoComments.objects.filter(course=video_detail)
        return render(request, 'detail.html', {
            'video': video_detail,
            'comments': comments,
        })


class ChildCom(View):
    def post(self,request):
        comment_id = request.GET.get('comment_id',None)
        video_id = request.GET.get('video_id', None)
        comment = request.POST.get('comment', None)
        add_comment = ChildComment()
        add_comment.user = request.user
        add_comment.comments = comment
        add_comment.fa_id = int(comment_id)
        add_comment.save()
        video_detail = Video.objects.get(id=int(video_id))
        comments = VideoComments.objects.filter(course=video_detail).order_by('-add_time')
        return render(request, 'detail.html', {
            'video': video_detail,
            'comments': comments,
        })

class InfoView(View):
    def get(self,request):
        return render(request,'info.html')


class InfoFav(View):
    def get(self,request):
        fav_list = []
        fav = UserFavorite.objects.filter(user=request.user)
        for i in fav:
            video_id = i.fav_id
            match = Video.objects.get(id=video_id)
            fav_list.append(match)
        return render(request,'info_fav.html',{
            'fav_list':fav_list,
        })

class InfoMess(View):
    def get(self,requset):
        user_id = requset.user.id
        mess = UserMessage.objects.filter(user=user_id)
        return render(requset,'info_mess.html',{
            'mess_list':mess
        })


class Detail(View):
    def get(self,request):
        video_id = request.GET.get('id','')
        video_detail = Video.objects.get(id=int(video_id))
        comments = VideoComments.objects.filter(course=video_detail).order_by('-add_time')
        return render(request,'detail.html',{
            'video':video_detail,
            'comments':comments,
        })


from django.shortcuts import render_to_response
def pag_not_found(request):
    # 全局404处理函数
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response

def page_error(request):
    # 全局500处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response































