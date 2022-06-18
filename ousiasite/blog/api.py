import imp
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Article
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import base64
import os
import datetime
import requests

hostUrl = 'http://127.0.0.1:9000/'


@api_view(['POST'])
def add_article(request):
    # 获取文章数据
    title = request.POST['title']
    describe = request.POST['describe']
    cover = request.POST['cover']
    content = request.POST['content']
    # 保存文章的大致实体（标题）
    new_article = Article(title=title)
    new_article.save()
    # 使用爬虫处理文章内容content
    # 解析富文本html文档
    soup = BeautifulSoup(content, 'html.parser')
    # 获取所有img标签 图片
    imgList = soup.find_all('img')
    # print(imgList)
    for img in range(0, len(imgList)):
        # 4.15_1.a src是imgList的img标签元素的src属性（对于远程图片来说是地址；本地是一个包含图片说明信息，以及描述图片二进制信息的字符串）
        src = imgList[img]['src']
        # 4.15_1.b 判断图片 是远程 还是 本地
        if 'http://' in src or 'https://' in src:
            # 请求远程图片
            image = requests.get(src)
            # 转换二进制
            image_data = Image.open(BytesIO(image.content))
            # 设定文件名称
            image_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '-' + \
                str(new_article.id)+'-'+str(img)
            # 保存图片
            image_data.save("upload/"+image_name+".png")
            # content的远程图片src替换为新保存的本地src
            new_src = hostUrl+"upload/"+image_name+".png"
            content = content.replace(src, new_src)
            # 封面设定
            if cover == src:
                cover = new_src
        else:
            # 处理本地图片的src。取出图片二进制信息字符串，并转码成二进制
            # base64.b64decode将描述图片二进制信息的字符串还原成二进制
            image_data = base64.b64decode(src.split(',')[1])
            # 设定文件名称
            image_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '-' + \
                str(new_article.id)+'-'+str(img)+'.' + \
                src.split(',')[0].split('/')[1].split(';')[0]
            # 保存图片
            image_url = os.path.join('upload', image_name).replace('\\', '/')
            with open(image_url, 'wb') as f:
                f.write(image_data)
            new_src = hostUrl + image_url
            # content的本地图片src替换为新保存的本地src
            content = content.replace(src, new_src)
            # 封面设定
            if cover == src:
                cover = new_src
    # 4.15_1.c 接着保存文章的其他数据项
    new_article.content = content
    new_article.describe = describe
    new_article.cover = cover
    new_article.save()
    return Response('ok')
