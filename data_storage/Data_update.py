import pandas as pd
import pymysql as pymysql
from sqlalchemy import create_engine
import re


class Data_update:

    def __init__(self):
        # 连接本地数据库spider_jd
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='spider_jd',
                                    charset='utf8mb4')
        # 创建游标对象
        self.cursor = self.conn.cursor()

        self.engine = create_engine('mysql+pymysql://root:root@localhost:3306/spider_jd')

    def updataKeywordStus(self, kid, value):
        try:
            # 执行SQL修改语句
            sql = "UPDATE keyword_t SET stus = " + str(value) + " WHERE keyId = "+ str(kid)
            # 获取结果
            self.cursor.execute(sql)

            return True
        except Exception as e:
            print('up1')
            print(e)
            return False

    def updataKeyword(self, kid, createDate, listPage, commitPage, goodsCount, commitCount, commitImgCount, price):
        try:
            sql  = "UPDATE keyword_t SET createDate = '" + str(createDate) + "',listPage = " + str(listPage) +  \
                   ",commitPage = " + str(commitPage) + ",goodsCount = " + str(goodsCount) + \
                   ",commitCount = " + str(commitCount) + ",commitImgCount = " + str(commitImgCount) + \
                   ",price = " + str(price) + \
                   " WHERE keyId = "+ str(kid)
            # 获取结果
            self.cursor.execute(sql)
            return True
        except Exception as e:
            print('up2')
            print(e)
            return False
    def commit(self):
        # 提交
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()
