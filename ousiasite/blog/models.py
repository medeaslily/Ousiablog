from pickletools import read_uint1
from pydoc import describe
from statistics import mode
from turtle import title
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# # 用户


class Userinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    headImg = models.CharField(null=True, blank=True, max_length=200)
    nickName = models.CharField(null=True, blank=True, max_length=200)
    belong = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __int__(self):
        return self.id

# 文章


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(null=True, blank=True, max_length=80)
    # max_length最大长度300
    cover = models.CharField(null=True, blank=True, max_length=300)
    describe = models.CharField(null=True, blank=True, max_length=200)
    content = models.TextField()
    # 前端需要的文章数据是关联用户的，因此需要修改文章数据表，添加用户字段
    belong = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='artitle_user')
    #belong = models.ForeignKey(Userinfo)

    def __int__(self):
        return self.id

# # 文章分类


# class Category(models.Model):
#     name = models.CharField()
#     belong = models.ForeignKey(self)

#     def __int__(self):
#         return self.id
# # 收藏


# class Favourite(models.Model):
#     belong_user = models.ForeignKey(Userinfo)
#     belong_art = models.ForeignKey(Article)

#     def __int__(self):
#         return self.id
# # 点赞


# class Like(models.Model):
#     belong_art = models.ForeignKey(Article)
#     belong_user = models.ForeignKey(Userinfo)

#     def __int__(self):
#         return self.id
# # 打赏


# class PayOrder(models.Model):
#     order = models.CharField()
#     price = models.CharField()
#     status = models.BooleanField()

#     def __int__(self):
#         return self.id
