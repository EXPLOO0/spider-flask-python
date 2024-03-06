import pandas as pd
import pymysql as pymysql
from sqlalchemy import create_engine
import re


class Data_select:

    def __init__(self):
        # 连接本地数据库spider_jd
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='spider_jd', charset='utf8mb4')
        # 创建游标对象
        self.cursor = self.conn.cursor()

        self.engine = create_engine('mysql+pymysql://root:root@localhost:3306/spider_jd')

    def selectKeyword(self, keyword):
        # 执行SQL查询语句
        if keyword == 'none':
            sql = "SELECT keyId, keyword FROM keyword_t "
            # 获取全部结果
            self.cursor.execute(sql)
            # 返回查询结果
            data = self.cursor.fetchall()
        else:
            sql = "SELECT keyId, keyword FROM keyword_t WHERE keyword = %s "
            # 获取结果
            self.cursor.execute(sql, keyword)
            # 返回查询结果
            data = self.cursor.fetchone()
        return data

    def selectGoods(self, keyId, brand1, brand2, brand3, brand4, brand5, shop, pid):
        # # pandas从数据库获取数据
        # sql = 'select pid, brand1, brand2, brand3, brand4, title, price, commit, shop, detail_url from goods_t where keyId = %s '
        # # 锁定查询
        #
        # # 获取全部结果
        # df = pd.read_sql(sql, self.conn, params=(keyId, ))
        # self.close()
        # return df

        # 判断brand1, brand2, brand3是否为空,不为空时增加判断条件
        sql1 = ' '
        if brand1 != '' and brand1:
            sql1 = sql1 + ' and brand1 = "' + brand1 + '" '
        if brand2 != '' and brand2:
            sql1 = sql1 + ' and brand2 = "' + brand2 + '" '
        if brand3 != '' and brand3:
            sql1 = sql1 + ' and brand3 = "' + brand3 + '" '
        if brand4 != '' and brand4:
            sql1 = sql1 + ' and brand4 LIKE "%%' + brand4 + '%%" '
        if brand5 != '' and brand5:
            sql1 = sql1 + ' and brand5 LIKE "%%' + brand5 + '%%" '
        if shop != '' and shop:
            sql1 = sql1 + ' and shop = "' + shop + '" '
        if pid != '' and pid:
            sql1 = sql1 + ' and pid = "' + pid + '" '

        # 使用SQLAlchemy创建数据库连接对象
        # engine = create_engine('mysql+pymysql://root:root@localhost:3306/spider_jd')
        # pandas从数据库获取数据
        sql = 'select pid, brand1, brand2, brand3, brand4, brand5, title, price, commit, shop, p_img, detail_url from goods_t where keyId = %s ' + sql1
        # 获取全部结果
        df = pd.read_sql(sql, self.engine, params=(keyId,))
        return df

    def selectBrand1(self, keyId):
        # pandas从数据库获取数据
        sql = 'select brand1 from goods_t where keyId =  ' + str(keyId)
        # 获取全部结果
        df = pd.read_sql(sql, self.engine)
        # 去除空值
        df = df.dropna(subset=['brand1'])
        df = df[df['brand1'] != 'default_value']
        # 去除重复
        df = df.drop_duplicates()
        # 如果数据为空，返回空
        if df.empty:
            return None
        # 输出list
        return df['brand1'].tolist()

    def selectBrand2(self, keyId, brand1):
        if brand1:
            sql1 = ' and brand1 = "' + str(brand1) +'" '
        else:
            sql1 = ' and brand1 is null '

        sql = 'select brand2 from goods_t where keyId =  ' + str(keyId) + sql1

        print(sql)
        # 获取全部结果
        df = pd.read_sql(sql, self.conn)
        # 去除空值
        df = df.dropna(subset=['brand2'])
        df = df[df['brand2'] != 'default_value']
        # 去除重复
        df = df.drop_duplicates()
        # 如果数据为空，返回空
        if df.empty:
            return None
        # 输出list
        return df['brand2'].tolist()

    def selectBrand3(self, keyId, brand1, brand2):
        if brand1:
            sql1 = ' and brand1 = "' + str(brand1) +'" '
        else:
            sql1 = ' and brand1 is null '
        if brand2:
            sql2 = ' and brand2 = "' + str(brand2) +'" '
        else:
            sql2 = ' and brand2 is null '

        sql = 'select brand3 from goods_t where keyId =  ' + str(keyId) + sql1 + sql2

        # 获取全部结果
        df = pd.read_sql(sql, self.conn)
        # 去除空值
        df = df.dropna(subset=['brand3'])
        df = df[df['brand3'] != 'default_value']
        # 去除重复
        df = df.drop_duplicates()
        # 如果数据为空，返回空
        if df.empty:
            return None
        # 输出list
        return df['brand3'].tolist()

    def selectSpecImg(self, keyId, pid):
        sql = 'select p_img from spec_img_t where kid =  ' + str(keyId) + ' and pid = "' + str(pid) +'" '

        # 获取全部结果
        df = pd.read_sql(sql, self.engine)
        # 去重
        df = df.drop_duplicates()

        pimgList = []
        # 循环调用正则
        for index, row in df.iterrows():
            input_string = row['p_img']
            # 使用正则表达式替换链接中的部分
            pattern = r'^.*?(?=jfs/t1)'
            change_string = 'https://img30.360buyimg.com/shaidan/s616x405'

            output_string = re.sub(pattern, change_string, input_string)
            # 存入列
            pimgList.append(output_string)

        return pimgList

    def selectCommitCount(self, keyId, pid, score):
        sql = 'SELECT count(*) FROM commit_t WHERE kid = ' + str(keyId) + ' and pid = "' + str(pid) + '" '
        if score != '' and score:
            sql = sql + ' and score = ' + str(score) + ' '
        print(sql)
        # 获取全部结果
        df = pd.read_sql(sql, self.engine)
        # 返回第一个结果
        return df.iloc[0, 0]

    def selectSpec(self, keyId, pid):
        sql = 'select CONCAT(param3, "：", param4) as a from spec_t where kid =  ' + str(keyId) + ' and pid = "' + str(pid) +'" ORDER BY CASE param3 WHEN "包装清单" THEN 1 ELSE 2 END'

        # 获取全部结果
        df = pd.read_sql(sql, self.engine)
        # 去重
        df = df.drop_duplicates()
        # df['a']中包含  ’包装信息‘ 的字符 提到第一个
        df['a'] = df['a'].str.replace('包装信息', '', regex=False).str.replace('包装信息', '包装信息',
                                                                  regex=False).str.replace('包装信息', '',
                                                                                  regex=False)

        return df['a'].tolist()


    def close(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()

if __name__ == '__main__':
    ds = Data_select()
    a = ds.selectSpec(17,100061054752)

    print(a)