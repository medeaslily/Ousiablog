from django.urls import path
from blog import api

urlpatterns = [
    # 添加文章
    path('add-article/', api.add_article),
    # 文章列表
    path('artitle-list/', api.artitleList),
    # 登录
    path('ousia-login/', api.ousia_login),
    # 注册
    path('ousia-register/', api.ousia_register),
    # 自动登录
    path('auto-login/', api.ousia_autologin),
    # 登出
    path('ousia-logout/', api.ousia_logout),
    # 删除
    path('delete-article/', api.deleteArticle)
]
