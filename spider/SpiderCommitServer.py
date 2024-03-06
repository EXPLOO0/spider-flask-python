"""
这是一个京东评论爬虫
"""
import csv
import json

import pandas as pd
import requests

from spider.SpiderCommitDataDefine import Record


class Spider_commit:
    url = None  # 请求链接
    header = None

    def __init__(self, productId, score=0, page=50):
        self.productId = productId
        self.score = score
        self.page = page

    def request(self, page) -> dict:
        """
        请求数据的方法
        :return:
        """

        self.url = f"https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv30672" \
                   f"&productId={self.productId}&score={self.score}&sortType=5&page={page}&pageSize=10" \
                   f"&isShadowSku=0&rid=0&fold=1"

        # 设置请求头
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38."
        }

        data = requests.get(url=self.url, headers=self.header).text
        # 去除不符合json格式的开头
        data = data.replace("fetchJSON_comment98vv30672(", "")
        # 去除不符合json格式的结尾
        data = data[:-2]

        # 将返回的json数据转换成python字典格式
        data_dict = json.loads(data)

        return data_dict  # 返回一个dict

    def data_parse(self, page):
        """
        处理返回字典的方法
        :return: 返回一个列表，列表中的每个元素是一个Record类对象
        """
        record_list = []
        data_dict = self.request(page)
        comment_list = data_dict["comments"]
        for i in comment_list:
            comment_text = str(i["content"])
            comment_text = comment_text.replace('\n', '')  # 去掉评论所有的换行符
            record = Record(self.productId, i["productColor"], i["productSize"], i["id"], comment_text, i["score"])
            record_list.append(record)
            # 判断i['images']是否存在
            if 'images' in i and i['images']:
                imgList = i['images']
                for img in imgList:
                    with open("static/data/csv/data-commit-img.csv", mode='a', newline='', encoding='utf-8') as f:
                        csv.writer(f).writerow([self.productId, i["id"], img['imgUrl']])

        return record_list

    def data_print(self):
        for j in range(0, self.page):
            data_list = self.data_parse(j)
            for i in data_list:
                print(i)

    def clear_csv(self):
        with open("static/data/csv/data-commit.csv", mode='w', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow(["ProductId", "ProductColor", "ProductSize", "ID", "score", "content"])
        with open("static/data/csv/data-commit-img.csv", mode='w', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow(["ProductId", "ID", "img"])

    def csv_write(self):
        f = open(f"static/data/csv/data-commit.csv", "a", encoding="utf8")
        write = csv.writer(f)
        for j in range(0, self.page):
            print(str(self.productId)+'------第'+str(j)+'页---------')
            data_record = self.data_parse(j)
            for i in data_record:
                data = [i.ProductId, i.ProductColor, i.ProductSize, i.ID, i.Score, i.Content.encode('GBK', 'ignore').decode('GBK', 'ignore')]
                write.writerow(data)
        f.close()


if __name__ == '__main__':
    df1 = pd.read_csv("./10052999059796的评论.csv")
    print(df1.head(645))