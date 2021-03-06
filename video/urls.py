"""video URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from users.views import LoginView, RegisterView, LogoutView, IndexView, SearchView, InfoView, InfoFav, InfoMess, Detail, Comment, ActiveUser, ForgetPass, ResetPass, ChildCom
import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('captcha/',include('captcha.urls')),
    path('search/',SearchView.as_view(),name='search'),
    path('info/',InfoView.as_view(),name='info'),
    path('info_fav/',InfoFav.as_view(),name='info_fav'),
    path('message/',InfoMess.as_view(),name='info_mess'),
    path('detail/',Detail.as_view(),name='video_detail'),
    path('comment/',Comment.as_view(),name='comment'),
    path('active/',ActiveUser.as_view(),name='active_user'),
    path('forget/',ForgetPass.as_view(),name='forget_pass'),
    path('reset/',ResetPass.as_view(),name='reset_pass'),
    path('childcom/',ChildCom.as_view(),name='childcom'),

]
