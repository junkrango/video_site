from django import forms

# 登录表单验证
from captcha.fields import CaptchaField

class RegisterForm(forms.Form):
    '''注册验证表单'''    
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    # 验证码，字段里面可以自定义错误提示信息
    captcha = CaptchaField()