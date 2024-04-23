import pandas as pd
import pymysql as pymysql
from sqlalchemy import create_engine
import re
import configparser


class Data_update:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('configData.ini')  # 读取配置文件

        host = config.get('MySQL', 'host')
        port = int(config.get('MySQL', 'port'))
        user = config.get('MySQL', 'user')
        password = config.get('MySQL', 'password')
        db = config.get('MySQL', 'db')
        charset = config.get('MySQL', 'charset')

        # 连接本地数据库spider_jd
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
        # 创建游标对象
        self.cursor = self.conn.cursor()

        self.engine = create_engine('mysql+pymysql://'+user+':'+password+'@'+host+':'+str(port)+'/'+db+'')

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
