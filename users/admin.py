from django.contrib import admin
from .models import EmailVerifyRecord, UserProfile
# Register your models here.
admin.site.register(EmailVerifyRecord)
admin.site.register(UserProfile)