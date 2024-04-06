import datetime
import math

import pandas as pd

from data_storage.Data_insert import Data_insert
from data_storage.Data_select import Data_select
from data_storage.Data_update import Data_update


class Data_clean:

    di = Data_insert()

    # 将字符串型的评论数转换为整数
    def trans(self, num):
        if isinstance(num, int):
            return str(num)
        if num.find('+') != -1:
            num = num.replace('+', '')
        if num.find('万') != -1:
            num = num.replace('万', '')
            # 以万为单位的评论数可能为小数，比如3.4万，因此强制转换为float类型存储
            num = float(num) * 10000
        num = str(int(num))
        return num

    def goods_process(self):
        print('处理goods数据---------')
        df = pd.read_csv('static/data/csv/data-goods.csv',encoding_errors='ignore', on_bad_lines='skip')
        df = df.dropna()
        df = df.fillna('default_value')  # value为要替换的值
        df = df.drop_duplicates()  # 删除重复值
        df["p_commit"] = df["p_commit"].apply(self.trans)
        df["p_commit"] = df["p_commit"].apply(pd.to_numeric)
        df['p_commit'] = df['p_commit'].astype(int)
        df['p_price'] = df['p_price'].astype(int)

        return df

    def brand_process(self):
        print('处理brand数据---------')
        df = pd.read_csv('static/data/csv/data-brand.csv',encoding_errors='ignore', on_bad_lines='skip')
        df = df.dropna()
        df = df.fillna('default_value')  # value为要替换的值
        df = df.drop_duplicates()  # 删除重复值

        # 去除brand3列中数据中的（）和（）中的信息，如：小米（MI） 变为 小米
        df['p_brand4'] = df['p_brand4'].str.replace('（.*）', '', regex=True)
        df['p_brand5'] = df['p_brand5'].str.replace(' ', '').str.replace('（.*）', '', regex=True).str.lower()
        # df = df[df['brand5'].str.len() <= 30]
        return df

    def goods_brand_merge_insert(self, kid):
        try:
            print('合并商品和品牌数据，并insert数据库---------')
            goodsDF = self.goods_process()
            goodsDF = goodsDF.drop_duplicates()  # 删除重复值
            brandDF = self.brand_process()
            brandDF = brandDF.drop_duplicates()  # 删除重复值
            # 根据pid合并
            df = pd.merge(goodsDF, brandDF, left_on='pid', right_on='pid', how='left')
            df = df.drop_duplicates()  # 删除重复值
            # df = df.dropna()
            df = df.fillna('default_value')  # value为要替换的值
            # 根据insertGoods(self, keyId, pid, brand1, brand2, brand3, brand4, brand5, title, price, commit, shop, detail_url)
            # 循环保存数据

            try:
                gcDF = self.goods_commit_process()
                cDF = self.commit_process()

                # 遍历df
                for index, row in df.iterrows():
                    # print(index)
                    # 获取gcDF中pid等于row['pid']的所有id列
                    gc_id = gcDF[gcDF['ProductId'] == row['pid']]['ID'].tolist()

                    # cDF中sentimentScore列为nan时设为0
                    cDF['sentimentScore'] = cDF['sentimentScore'].fillna(0)

                    #  获取cDF中id在gc_id中包含的sentimentScore列的平均值和score列的平均值
                    sentimentScore = cDF[cDF['ID'].isin(gc_id)].sentimentScore.mean()
                    if math.isnan(sentimentScore):
                        sentimentScore = 0

                    sentiment5 = cDF[(cDF['ID'].isin(gc_id)) & (cDF['score'] == 5)].sentimentScore.mean()
                    if math.isnan(sentiment5):
                        sentiment5 = 0
                    sentiment4 = cDF[(cDF['ID'].isin(gc_id)) & (cDF['score'] == 4)].sentimentScore.mean()
                    if math.isnan(sentiment4):
                        sentiment4 = 0
                    sentiment3 = cDF[(cDF['ID'].isin(gc_id)) & (cDF['score'] == 3)].sentimentScore.mean()
                    if math.isnan(sentiment3):
                        sentiment3 = 0
                    sentiment2 = cDF[(cDF['ID'].isin(gc_id)) & (cDF['score'] == 2)].sentimentScore.mean()
                    if math.isnan(sentiment2):
                        sentiment2 = 0
                    sentiment1 = cDF[(cDF['ID'].isin(gc_id)) & (cDF['score'] == 1)].sentimentScore.mean()
                    if math.isnan(sentiment1):
                        sentiment1 = 0


                    #  获取cDF中id在gc_id中包含的score列的总数
                    commit_count = cDF[cDF['ID'].isin(gc_id)].score.count()

                    #  获取cDF中id在gc_id中包含的score列等于5的总数
                    count5 = cDF[(cDF['ID'].isin(gc_id)) & (cDF['score'] == 5)].score.count()
                    count4 = cDF[(cDF['ID'].isin(gc_id)) & (cDF['score'] == 4)].score.count()
                    count3 = cDF[(cDF['ID'].isin(gc_id)) & (cDF['score'] == 3)].score.count()
                    count2 = cDF[(cDF['ID'].isin(gc_id)) & (cDF['score'] == 2)].score.count()
                    count1 = cDF[(cDF['ID'].isin(gc_id)) & (cDF['score'] == 1)].score.count()


                    # 输出sentimentScore的类型
                    if math.isnan(sentimentScore):
                        continue
                    self.di.insertGoods(kid, row['pid'], row['p_brand1'], row['p_brand2'], row['p_brand3'], row['p_brand4'], row['p_brand5'], row['p_name'], row['p_price'], row['p_commit'], row['p_shop'], row['p_img'], row['p_url'],sentimentScore,sentiment1,sentiment2,sentiment3,sentiment4,sentiment5,commit_count,count1,count2,count3,count4,count5)

            except Exception as e:
                print('--g--b--i--1')
                print(e)

        except Exception as e:
            print('--g--b--i--2')
            print(e)

    def goods_commit_process(self):
        print('处理goods_commit数据---------')
        df = pd.read_csv('static/data/csv/data-goods-commit.csv',encoding_errors='ignore', on_bad_lines='skip')
        df = df.dropna()
        df = df.drop_duplicates()  # 删除重复值
        df = df.fillna('default_value')  # value为要替换的值
        return df

    def goods_commit_insert(self, kid):
        try:
            print('保存goods_commit数据---------')
            df = self.goods_commit_process()

            for index, row in df.iterrows():
                self.di.insertGoodsCommit(kid, row['ProductId'], row['ID'])
        except Exception as e:
            print('--g--c--i--1')
            print(e)

    def commit_process(self):
        try:
            print('处理commit数据---------')
            df = pd.read_csv('static/data/csv/data-commit.csv',encoding_errors='ignore', on_bad_lines='skip')
            # 去重
            df = df.drop_duplicates()
            # df = df.dropna()
            df['score'] = pd.to_numeric(df['score'], errors='coerce')
            # df = df[df['score'].apply(lambda x: isinstance(x, float))]
            # 去重
            df = df.drop_duplicates()
            # 去除score列为空的
            df = df[df['score'].notnull()]
            df = df[df['content'].notnull()]
            df['score'] = df['score'].astype(int)

            # sentimentScore=‘nan’ 设为0
            df['sentimentScore'] = df['sentimentScore'].replace('nan', 0.0)
            # sentimentScore空值设为0
            df['sentimentScore'] = df['sentimentScore'].fillna(0.0)
            df['sentimentScore'] = df['sentimentScore'].astype(float)


            # 排除sentimentScore列不为float类型的
            df = df[df['sentimentScore'].apply(lambda x: isinstance(x, float))]

            df = df.fillna('default_value')  # value为要替换的值
            df = df.drop_duplicates()  # 删除重复值


            return df

        except Exception as e:
            print('--c--i--')
            print(e)
    def commit_insert(self, kid):
        try:
            print('保存commit数据---------')
            df = self.commit_process()

            for index, row in df.iterrows():
                # 输出sentimentScore的类型
                if math.isnan(row['sentimentScore']):
                    continue
                self.di.insertCommit(kid, row['ProductColor'], row['ProductSize'], row['ID'], row['score'], row['content'], row['sentimentScore'])
        except Exception as e:
            print('--c--i--')
            print(e)

    def commit_img_process(self):
        print('处理commit-img数据---------')
        df = pd.read_csv('static/data/csv/data-commit-img.csv',encoding_errors='ignore', on_bad_lines='skip')
        df = df.dropna()
        df = df.drop_duplicates()  # 删除重复值
        df = df.fillna('default_value')  # value为要替换的值
        return df

    def commit_img_insert(self, kid):
        try:
            print('保存commit-img数据---------')
            df = self.commit_img_process()

            for index, row in df.iterrows():
                self.di.insertCommitImg(kid, row['ID'], row['img'])
        except Exception as e:
            print('--c--ii--')
            print(e)

    def introduce_process(self):
        print('处理introduce数据---------')
        df = pd.read_csv('static/data/csv/data-introduce.csv',encoding_errors='ignore', on_bad_lines='skip')
        # df = df.dropna()
        df = df.fillna('default_value')  # value为要替换的值
        df = df.drop_duplicates()  # 删除重复值
        return df

    def introduce_insert(self, kid):
        try:
            print('保存introduce数据---------')
            df = self.introduce_process()

            for index, row in df.iterrows():
                self.di.insertIntroduce(kid, row['pid'], row['param1'], row['param2'], row['param3'])
        except Exception as e:
            print('--ii--')
            print(e)

    def spec_process(self):
        print('处理spec数据---------')
        df = pd.read_csv('static/data/csv/data-spec.csv',encoding_errors='ignore', on_bad_lines='skip')
        # df = df.dropna()
        df = df.fillna('default_value')  # value为要替换的值
        df = df.drop_duplicates()  # 删除重复值
        df = df.dropna()
        return df

    def spec_insert(self, kid):
        try:
            print('保存spec数据---------')
            df = self.spec_process()

            for index, row in df.iterrows():
                self.di.insertSpec(kid, row['pid'], row['param1'], row['param2'], row['param3'], row['param4'])
        except Exception as e:
            print('si')
            print(e)

    def spec_img_process(self):
        print('处理spec-img数据---------')
        df = pd.read_csv('static/data/csv/data-spec-img.csv',encoding_errors='ignore', on_bad_lines='skip')
        df = df.dropna()
        df = df.fillna('default_value')  # value为要替换的值
        df = df.drop_duplicates()  # 删除重复值
        df = df.dropna()
        return df

    def spec_img_insert(self, kid):
            print('保存spec-img数据---------')
            df = self.spec_img_process()

            for index, row in df.iterrows():
                self.di.insertSpecImg(kid, row['pid'], row['p_img'])

    def qa_process(self):
        print('处理qa数据---------')
        # 读取'static/data/csv/data-answer.csv'文件，再用utf-8保存回源文件

        df = pd.read_csv('static/data/csv/data-answer.csv',encoding_errors='ignore', on_bad_lines='skip')
        df = df.dropna()
        df = df.drop_duplicates()  # 删除重复值
        df = df.dropna()
        return df

    def qa_insert(self, kid):
            print('保存qa数据---------')
            df = self.qa_process()
            for index, row in df.iterrows():
                self.di.insertQa(kid, row['pid'], row['num'], row['question'], row['answer'])

    def keyword_updata(self, kid, goodsPage, commitPage):
        try:
            # 获取当前时间
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ds = Data_select()
            goodsCount = ds.selectGoodsCount(kid)
            commitCount =  ds.selectCommitCount(kid)
            commitImgCount =  ds.selectCommitImgCount(kid)
            pricedf = ds.selectGoods(kid, '', '', '', '', '', '', '')
            #取pricedf中的price列的平均值
            price = pricedf['price'].mean()
            du = Data_update()
            du.updataKeyword(kid, now_time, goodsPage, commitPage, goodsCount, commitCount, commitImgCount, price)
            du.commit()
        except Exception as e:
            print(e)


    def put_all(self,kid,goodsPage,commitPage):
        try:
            self.goods_brand_merge_insert(kid)
            print('goods-brand----完成--------')
            self.goods_commit_insert(kid)
            print('goods_commit----完成--------')
            self.commit_insert(kid)
            print('commit----完成--------')
            self.commit_img_insert(kid)
            print('commit-img----完成--------')
            self.spec_insert(kid)
            print('spec----完成--------')
            self.spec_img_insert(kid)
            print('spec-img----完成--------')
            self.introduce_insert(kid)
            print('introduce----完成--------')
            # self.qa_insert(kid)
            # print('qa----完成--------')
            self.di.commit()
            print('--------更新keyword数据--------')
            self.keyword_updata(kid, goodsPage,commitPage)
            print('--------更新keyword数据完成--------')
            print('关闭数据库连接---------')
        except:
            self.di.rollback()

if __name__ == '__main__':
    dc = Data_clean()
    dc.keyword_updata(1,50,20)