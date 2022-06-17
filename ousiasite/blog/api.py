import imp
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Article
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
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
    # 使用爬虫处理文章内容
    # 解析富文本html文档
    soup = BeautifulSoup(content, 'html.parser')
    # 获取所有img标签 图片
    imgList = soup.find_all('img')
    # print(imgList)
    for img in range(0, len(imgList)):
        # 4.15_1.a src是imgList的img标签元素的src属性（地址）
        src = imgList[img]['src']
        # 4.15_1.b 判断图片 是远程 还是 本地
        if 'http://' in src or 'https://' in src:
            # 请求远程图片
            image = requests.get(src)
            print(image.text)
            # 转换二进制
            image_data = Image.open(BytesIO(image.content))
            # 设定文件名称
            image_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '-' + \
                str(new_article.id)+'-'+str(img)
            image_data.save("upload/"+image_name+".png")
            # content的远程图片src替换为新保存的本地src
            new_src = hostUrl+"upload/"+image_name+".png"
            content = content.replace(src, new_src)
        else:
            pass
    # 4.15_1.c 接着保存文章的内容
    new_article.content = content
    new_article.save()
    return Response('ok')
