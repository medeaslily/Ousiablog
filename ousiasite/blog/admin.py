from django.contrib import admin
from blog.models import Article, Userinfo

# Register your models here.
# 把models.py的Article注册到后台界面
admin.site.register(Article)
admin.site.register(Userinfo)
