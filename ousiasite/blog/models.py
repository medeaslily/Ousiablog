from pickletools import read_uint1
from pydoc import describe
from statistics import mode
from turtle import title
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# # 用户


# class Userinfo(models.Model):
#     headImg = models.ImageField()
#     nickName = models.CharField()
#     belong = models.OneToOneField(User)

#     def __init__(self):
#         return self.id

# 文章


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(null=True, blank=True, max_length=80)
    # max_length最大长度300
    cover = models.CharField(null=True, blank=True, max_length=300)
    describe = models.CharField(null=True, blank=True, max_length=200)
    content = models.TextField()
    #belong = models.ForeignKey(Userinfo)

    def __int__(self):
        return self.id

# # 文章分类


# class Category(models.Model):
#     name = models.CharField()
#     belong = models.ForeignKey(self)

#     def __init__(self):
#         return self.id
# # 收藏


# class Favourite(models.Model):
#     belong_user = models.ForeignKey(Userinfo)
#     belong_art = models.ForeignKey(Article)

#     def __init__(self):
#         return self.id
# # 点赞


# class Like(models.Model):
#     belong_art = models.ForeignKey(Article)
#     belong_user = models.ForeignKey(Userinfo)

#     def __init__(self):
#         return self.id
# # 打赏


# class PayOrder(models.Model):
#     order = models.CharField()
#     price = models.CharField()
#     status = models.BooleanField()

#     def __init__(self):
#         return self.id