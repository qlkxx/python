import requests
import pyquery
from pyquery import PyQuery
import re
def generate_url_list():   # 添加：定义函数名
    url_list = []
    template = 'https://book.douban.com/tag/哲学?start={num}&type=T'
    for p in range(1,6):
        url = template.format(num=(p-1)*20)
        url_list.append(url)
    return url_list        # 添加：返回网址列表
url_list_tmp = generate_url_list()
# print(url_list_tmp)
def get_html(url):         # 添加：定义函数名
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;\
     x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'}
    resp = requests.get(url,headers=headers)
    html = resp.text
    return html
url_tmp = 'https://book.douban.com/tag/哲学?start=900&type=T'  # 第46页
html_tmp = get_html(url_tmp)
# print(html_tmp)
doc = PyQuery(html_tmp) # 将html字符串转换为pyquery数据，便于解析
# print(doc)
# print(type(doc))  # 数据类型为pyquery.pyquery.PyQuery
# print(doc.text())

# # 直接提取（书名、简介、评分、书书籍图片链接）
# for book in doc.items('.subject-item'):
#     book_name = book('.info h2 a').text()
#     desc = book('.info p').text()
#     score = book('.rating_nums').text()
#     img = book('.pic a img').attr('src')
#     print(book_name, desc, score, img)


# # 列表提取（作者、出版社、发布时间、价格）
# for book in doc.items('.subject-item'):
#     # info_list = book('.info .pub').text()    # 用左下划线'/'分隔的字符串
#     # print(info_list)
#     info_list = book('.info .pub').text().split('/')
#     # print(info_list)
# #     print(info_list[-3])    # 用[]提取列表元素，例如倒数第3个是出版社，索引为-3
#     publisher = info_list[-3].strip()   # 以同样的方式获得authors, publisher, pub_time, price字段
#     # print(publisher)
#     pub_time = info_list[-2]
#     price = info_list[-1]
#     authors = ','.join(info_list[:-3])   # 将多个作者元素，组合到一个字符串里
# #     print(authors)
#     print(authors, publisher, pub_time, price)


# # 正则（）提取评价人数
# for book in doc.items('.subject-item'):
#     people_num_raw = book('.pl').text()
#     # print(people_num_raw)
#     print(re.findall('[0-9]+', people_num_raw))


# # 整体提取
# bookinfo_list = []  # 生成空列表，用于存储书籍信息
# # doc = PyQuery(html)
# for book in doc.items('.subject-item'):
#     book_name = book('.info h2 a').text()  # 情况1：直接解析
#     desc = book('.info p').text()
#     score = book('.rating_nums').text()
#     img = book('.pic a img').attr('src')
#
#     info_list = book('.info .pub').text().split('/')  # 情况2：提取列表元素
#     publisher = info_list[-3].strip()
#     pub_time = info_list[-2]
#     price = info_list[-1]
#     authors = ''.join(info_list[:-3])
#
#     people_num_raw = book('.pl').text()  # 情况3：正则表达式提取
#     # people_num = re.findall('[0-9]+', people_num_raw)[0]
#     people_num = re.findall('[0-9]+', people_num_raw)
#     bookinfo = {'book_name': book_name,  # 为每本书创建一个字典，不同字段建构不同键值对
#                 'authors': authors,
#                 'publisher': publisher,
#                 'pub_time': pub_time,
#                 'desc': desc,
#                 'score': score,
#                 'people_num': people_num,
#                 'price': price,
#                 'img': img
#                 }
#
#     bookinfo_list.append(bookinfo)  # 将字典添加进bookinfo_list列表中
# # %%
# print(bookinfo_list)
# print(len(bookinfo_list))


# # 函数整体
# def extract_bookinfo_list(html):  # 添加：定义函数名
#     bookinfo_list = []
#     doc = PyQuery(html)
#     for book in doc.items('.subject-item'):
#         try:  # 添加：try语句，避免特殊网页中断整个循环。后跟except语句，用来防止因出现特殊情况，而导致的循环崩溃。
#             book_name = book('.info h2 a').text()
#             desc = book('.info p').text()
#             score = book('.rating_nums').text()
#             img = book('.pic a img').attr('src')
#             info_list = book('.info .pub').text().split('/')
#             publisher = info_list[-3].strip()
#             pub_time = info_list[-2]
#             price = info_list[-1]
#             authors = ''.join(info_list[:-3])
#             people_num_raw = book('.pl').text()
#             people_num = re.findall('[0-9]+', people_num_raw)[0]
#
#             bookinfo = {'book_name': book_name,
#                         'authors': authors,
#                         'publisher': publisher,
#                         'pub_time': pub_time,
#                         'desc': desc,
#                         'score': score,
#                         'people_num': people_num,
#                         'price': price,
#                         'img': img
#                         }
#
#             bookinfo_list.append(bookinfo)
#         except:  # 添加：except和pass语句，如果碰到bug，那么跳出此次循环、不执行任何操作，进行下一次循环
#             pass
#
#     return bookinfo_list  # 添加：返回书籍的字典列表
#
#
# # %%
# # html
# # %%
# # 调用函数extract_bookinfo_list(html)
# bookinfo_list = extract_bookinfo_list(html_tmp)
# print(bookinfo_list)
# print('书籍数量为：', len(bookinfo_list))
