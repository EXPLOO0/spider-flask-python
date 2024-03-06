import pandas as pd

from data_storage.Data_insert import Data_insert

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
        print('合并商品和品牌数据，并insert数据库---------')
        goodsDF = self.goods_process()
        brandDF = self.brand_process()
        # 根据pid合并
        df = pd.merge(goodsDF, brandDF, left_on='pid', right_on='pid', how='left')
        df = df.drop_duplicates()  # 删除重复值
        # df = df.dropna()
        df = df.fillna('default_value')  # value为要替换的值
        # 根据insertGoods(self, keyId, pid, brand1, brand2, brand3, brand4, brand5, title, price, commit, shop, detail_url)
        # 循环保存数据

        for index, row in df.iterrows():
            self.di.insertGoods(kid, row['pid'], row['p_brand1'], row['p_brand2'], row['p_brand3'], row['p_brand4'], row['p_brand5'], row['p_name'], row['p_price'], row['p_commit'], row['p_shop'], row['p_img'], row['p_url'])
        self.di.commit()

    def commit_process(self):
        print('处理commit数据---------')
        df = pd.read_csv('static/data/csv/data-commit.csv',encoding_errors='ignore', on_bad_lines='skip')
        # df = df.dropna()
        df['score'] = pd.to_numeric(df['score'], errors='coerce')
        # df = df[df['score'].apply(lambda x: isinstance(x, float))]
        # 去除score列为空的
        df = df[df['score'].notnull()]
        df['score'] = df['score'].astype(int)
        df = df.fillna('default_value')  # value为要替换的值
        df = df.drop_duplicates()  # 删除重复值
        return df

    def commit_insert(self, kid):
        print('保存commit数据---------')
        df = self.commit_process()

        for index, row in df.iterrows():
            self.di.insertCommit(kid, row['ProductId'], row['ProductColor'], row['ProductSize'], row['ID'], row['score'], row['content'])
        self.di.commit()

    def commit_img_process(self):
        print('处理commit-img数据---------')
        df = pd.read_csv('static/data/csv/data-commit-img.csv',encoding_errors='ignore', on_bad_lines='skip')
        df = df.dropna()
        df = df.drop_duplicates()  # 删除重复值
        return df

    def commit_img_insert(self, kid):
        print('保存commit-img数据---------')
        df = self.commit_img_process()

        for index, row in df.iterrows():
            self.di.insertCommitImg(kid, row['ProductId'], row['ID'], row['img'])
        self.di.commit()

    def introduce_process(self):
        print('处理introduce数据---------')
        df = pd.read_csv('static/data/csv/data-introduce.csv',encoding_errors='ignore', on_bad_lines='skip')
        # df = df.dropna()
        df = df.fillna('default_value')  # value为要替换的值
        df = df.drop_duplicates()  # 删除重复值
        return df

    def introduce_insert(self, kid):
        print('保存introduce数据---------')
        df = self.introduce_process()

        for index, row in df.iterrows():
            self.di.insertIntroduce(kid, row['pid'], row['param1'], row['param2'], row['param3'])
        self.di.commit()

    def spec_process(self):
        print('处理spec数据---------')
        df = pd.read_csv('static/data/csv/data-spec.csv',encoding_errors='ignore', on_bad_lines='skip')
        # df = df.dropna()
        df = df.fillna('default_value')  # value为要替换的值
        df = df.drop_duplicates()  # 删除重复值
        return df

    def spec_insert(self, kid):
        print('保存spec数据---------')
        df = self.spec_process()

        for index, row in df.iterrows():
            self.di.insertSpec(kid, row['pid'], row['param1'], row['param2'], row['param3'], row['param4'])
        self.di.commit()

    def spec_img_process(self):
        print('处理spec-img数据---------')
        df = pd.read_csv('static/data/csv/data-spec-img.csv',encoding_errors='ignore', on_bad_lines='skip')
        df = df.dropna()
        df = df.fillna('default_value')  # value为要替换的值
        df = df.drop_duplicates()  # 删除重复值
        return df

    def spec_img_insert(self, kid):
        print('保存spec-img数据---------')
        df = self.spec_img_process()

        for index, row in df.iterrows():
            self.di.insertSpecImg(kid, row['pid'], row['p_img'])
        self.di.commit()

    def qa_process(self):
        print('处理qa数据---------')
        # 读取'static/data/csv/data-answer.csv'文件，再用utf-8保存回源文件

        df = pd.read_csv('static/data/csv/data-answer.csv',encoding_errors='ignore', on_bad_lines='skip')
        df = df.dropna()
        df = df.drop_duplicates()  # 删除重复值
        return df

    def qa_insert(self, kid):
        print('保存qa数据---------')
        df = self.qa_process()
        for index, row in df.iterrows():
            self.di.insertQa(kid, row['pid'], row['num'], row['question'], row['answer'])
        self.di.commit()

    def put_all(self,kid):
        self.goods_brand_merge_insert(kid)
        print('goods-brand----完成--------')
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
        self.qa_insert(kid)
        print('qa----完成--------')
        self.di.close()
        print('关闭数据库连接---------')
