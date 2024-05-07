import requests   # 导入requests包
import json
import time
import random
import csv  # 导入csv包

def generate_url_list(product_id, max_page):
    url_list = []
    template = 'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1691385196787&loginType=3&uuid=122270672.16913846884751013594747.1691384688.1691384688.1691384688.1&productId={product_id}&score=0&sortType=5&page={page}&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield='
    for p in range(1,max_page+1):        # range取1到100，即p循环1到100页
        url = template.format(product_id = product_id, page=(p-1))
        url_list.append(url)
    return url_list

#%%
# 函数：获得json  get_json(url)
# 参数说明：url为单个网址
# 返回值：raw_comments为原始的评论数据
def get_json(url):
    resp = requests.get(url)
    raw_comments = resp.text
    return raw_comments


def extract_comments(raw_comments):
    data_list = []

    comments = json.loads(raw_comments)['comments']

    for comment in comments:  # 将一条条评论写入data_list中
        data = {}
        data['content'] = comment.get('content')
        data['creationTime'] = comment.get('creationTime')
        data['nickname'] = comment.get('nickname')
        data['plusAvailable'] = comment.get('plusAvailable')
        data['score'] = comment.get('score')
        data['usefulVoteCount'] = comment.get('usefulVoteCount')
        data['replyCount'] = comment.get('replyCount')
        data['productColor'] = comment.get('productColor')
        data['productSize'] = comment.get('productSize')
        data_list.append(data)

    return data_list

def main(product_id, max_page, filename):
    print('开始采集商品id为{product_id}的商品评论！'.format(product_id=product_id))

    # 生成所有网址url_list
    url_list = generate_url_list(product_id, max_page)

    # 打开文件
    file = open(filename, 'a+', encoding='utf-8-sig', newline='')
    fieldnames = ['content', 'creationTime', 'nickname', 'plusAvailable', 'score', 'usefulVoteCount', 'replyCount',
                  'productColor', 'productSize']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    # 对所有网址url_list循环步骤2-4
    for url in url_list:
        print('正在采集：{url}'.format(url=url))
        raw_comments = get_json(url)  # 【步骤2：请求+获取网页数据】
        time.sleep(random.random() * 3)  # 间隔不定长时间
        data_list = extract_comments(raw_comments)  # 【步骤3：解析数据】
        for data in data_list:  # 【步骤4：存储数据】
            writer.writerow(data)

    file.close()

    print('采集完毕！')

main(product_id = 100002781562, max_page=5, filename='umbrella_5p.csv')


# # 读取文件内容，不影响整体代码
#
# import pandas as pd
#
# # 用pandas.read_csv()读取
#
# # 设置行不限制数量,不然会中间有省略号，数据会看不到
# pd.set_option('display.max_rows', None)
# # 设置列不限制数量,不然会中间有省略号，数据会看不到
# pd.set_option('display.max_columns', None)
# # 控制台输出的列数超过1000换行，不然数据表格会折回来
# pd.set_option('display.width', 1000)
# # pd.set_option('display.max_colwidth',1000)
#
# #%%
# pd_reader = pd.read_csv('umbrella_5p.csv')
# # print(pd_reader)
# # #%%
# # print(pd_reader.shape)    # 查看行数，列数
# #%%
# print(pd_reader.head(10))    # 查看前几行信息，默认为5
# #%%
# print(pd_reader.tail(8))    # 查看后几行信息，默认为5