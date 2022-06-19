from django.urls import path
from blog import api

urlpatterns = [
    # 添加文章
    path('add-article/', api.add_article),
    # 用户管理
    # 登录
    path('ousia-login/', api.ousia_login),
    # 注册
    path('ousia-register/', api.ousia_register)
]
