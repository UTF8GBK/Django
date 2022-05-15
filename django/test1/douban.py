import requests
from lxml import etree

# 获取网页源码
def get_content(url):


    #  todo ：2构建请求头
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

    # todo : 3.发送请求
    request=requests.get(url,headers=headers).content.decode('utf-8')

    # todo  :4. 文档解析
    html= etree.HTML(request)
    # print(html)
    return html

 # 提取具体数量
def get_data(html):
    # todo :获取所有的内容列表
    content_li=html.xpath("//div[@class='indent']//tbody")
    # print(content_li)
    # todo   :  遍历具体的内容
    for i in content_li:
        item={}
        item['title']=i.xpath('.//div[@class=“pl2”]/a/text()')[0].replace('/','').replace('\n','').strip()
        print(item)
 # 保存电影封面

def save_image():
    pass


if __name__ == '__main__':
    url= 'https://movie.douban.com/chart'
    html=get_content(url)
    a=get_data(html)