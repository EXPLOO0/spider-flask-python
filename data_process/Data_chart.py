import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from data_process.Data_clean import Data_clean
from data_storage.Data_select import Data_select


class Data_chart:
    # 不同品牌的评论量占比
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['figure.figsize'] = (20.0, 20.0)


    # 不同品牌销量分析
    def get_brand_proportion_chart(self):
        df = pd.read_csv('static/data/csv/data-goods.csv')
        df.fillna('none')  # value为要替换的值
        df.drop_duplicates()  # 删除重复值
        df["commit"] = df["commit"].apply(Data_clean().trans)
        df["commit"] = df["commit"].apply(pd.to_numeric)
        df['commit'] = df['commit'].astype(int)
        df['price'] = df['price'].astype(int)
        gb1 = df.groupby(
            by=['brand3'],
            as_index=False
        )['commit'].agg({
            'commit': np.sum
        })
        # print(gb1['commit'] > 50)
        # 筛选出评论量前8的品牌
        x = gb1['commit'].argsort()[::-1]
        z = x.values[0:10]
        g1 = gb1.iloc[z, :]
        # 将g1['commit'], g1['brand3']返回
        # print(g1['commit'], g1['brand3'])
        # value: 1048, name: 'Search Engine'
        # 将g1['commit']为value, g1['brand3']为name，组成字典
        data = dict(zip(g1['brand3'], g1['commit']))
        return data

    # 不同店铺销量分析
    def get_shop_proportion_chart(self, df):
        gb1 = df.groupby(
            by=['shop'],
            as_index=False
        )['commit'].agg({
            'commit': np.sum
        })
        print(gb1['commit'] > 50)
        x = gb1['commit'].argsort()[::-1]
        z = x.values[0:10]
        g1 = gb1.iloc[z, :]
        plt.pie(g1['commit'], labels=g1['shop'], textprops={}, autopct="""%0.1f%%""")
        plt.title('不同店铺销量分析', fontsize=40)
        plt.legend(loc='lower right', fontsize=40)
        plt.savefig('店铺销量分析.jpg')
        plt.show()
        plt.close()

    # 不同品牌平均售价分析
    def get_brand_ave_price(self, df):
        gb1 = df.groupby(
            by=['brand3'],
            as_index=False
        )['price'].agg({
            'price': np.average
        })
        # g1 = gb1[(gb1['price'] > 5000)]
        g1 = gb1
        index = np.arange(g1['brand3'].size)
        plt.barh(index, g1['price'], height=0.5, color='maroon')
        plt.yticks(index, g1['brand3'])
        plt.xlabel('品牌平均售价分析', fontsize=20)
        plt.ylabel('商品售价', loc='top', fontsize=20)
        plt.savefig('品牌平均售价分析.jpg')
        plt.show()
        plt.close()

    # 不同店铺平均售价分析
    def get_shop_ave_price(self, df):
        gb1 = df.groupby(
            by=['shop'],
            as_index=False
        )['price'].agg({
            'price': np.average
        })
        # g1 = gb1[(gb1['price'] > 5000)]
        g1 = gb1
        index = np.arange(g1['shop'].size)
        plt.barh(index, g1['price'], height=0.5, color='maroon')
        plt.yticks(index, g1['shop'])
        plt.xlabel('店铺平均售价分析', fontsize=20)
        plt.ylabel('商品售价', loc='top', fontsize=20)
        plt.savefig('店铺平均售价分析.jpg')
        plt.show()
        plt.close()

    # 不同价格区间购买人数
    def get_price_ranges_chart(self, df):
        df['price'] = df['price'].astype(int)
        bins = [0, 50, 100, 300, 500, 1000, 3000, 5000, 20000]
        labels = ['50及以下', '50到100', '100到300', '300到500', '500到1000', '1000到3000', '3000到5000', '5000以上']
        df['price'] = pd.cut(df['price'], bins, labels=labels)
        gb1 = df.groupby(
            by=['price'],
            as_index=False
        )['commit'].agg({
            'commit': np.sum
        })
        plt.pie(gb1['commit'], labels=gb1['price'], autopct='%.2f%%')
        plt.title('不同价格区间购买人数百分比')
        plt.savefig('不同价格区间购买人数百分比.jpg')
        plt.show()

    # 总销量前10的品牌不同价格区间的销量
    def get_brand_price_ranges_chart(self, keyId, brand1, brand2, brand3):
        ds = Data_select()

        df = ds.selectGoods(keyId, brand1, brand2, brand3, '', '','','')

        # 排除brand4列为default_value的
        df = df[df['brand1'] != 'default_value']
        df = df[df['brand2'] != 'default_value']
        df = df[df['brand3'] != 'default_value']
        df = df[df['brand4'] != 'default_value']

        # 获取销量前10的品牌
        gb1 = df.groupby(
            by=['brand4'],
            as_index=False
        )['commit'].agg({
            'commit': np.sum
        })
        gb1 = gb1.sort_values(by='commit', ascending=False)
        gb1 = gb1[:10]

        # 获取销量前10的品牌不同价格区间的销量
        gb2 = df[df['brand4'].isin(gb1['brand4'])]
        gb2.loc[:, 'price'] = gb2['price'].astype(int)
        bins = [0, 50, 100, 300, 500, 1000, 2000, 3000, 4000, 5000, 10000, 20000, 99999999]
        labels = ['50及以下', '50到100', '100到300', '300到500', '500到1000', '1000到2000', '2000到3000', '3000到4000', '4000到5000', '5000到10000', '10000到20000',
                  '20000以上']
        gb2.loc[:, 'price'] = pd.cut(gb2['price'], bins, labels=labels)

        # gb2['price'] = gb2['price'].astype(int)
        # bins = [0, 50, 100, 300, 500, 1000, 3000, 5000, 10000, 99999999]
        # labels = ['50及以下', '50到100', '100到300', '300到500', '500到1000', '1000到3000', '3000到5000', '5000到10000', '10000以上']
        # gb2['price'] = pd.cut(gb2['price'], bins, labels=labels)
        gb3 = gb2.groupby(
            by=['brand4', 'price'],
            as_index=False
        )['commit'].agg({
            'commit': np.sum
        })

        # 将品牌输出
        brand_list = gb1['brand4'].tolist()
        # 将brand_list 倒序
        brand_list.reverse()
        # 将数据按照price价格区间，将同区间不同品牌的销量放在一个数组中，
        gb3 = gb3.pivot_table(values='commit', index='price', columns='brand4', aggfunc=np.sum)
        # 根据brand_list中的品牌顺序将数据转成列表
        gb3 = gb3.reindex(brand_list, axis=1)
        gb3 = gb3.values.tolist()

        # 将品牌列表插入到gb3的第一列
        gb3.insert(0, brand_list)
        # print(gb3)
        return gb3

    # 对应品牌的对应价格区间的型号排行
    def get_price_ranges_model_chart(self, keyId, brand4, priceRanges):
        ds = Data_select()

        df = ds.selectGoods(keyId, '', '', '', '', '','','')
        
        df = df[df['brand5'] != 'default_value']

        # 取出df 的brand3列、brand4列、price列、commit列
        df = df[['brand4', 'brand5', 'price', 'commit']]
        df['brand5'] = df['brand5'].str.replace(brand4, '').str.replace(' ', '').str.replace('（.*）', '', regex=True).str.lower()
        df = df[df['brand5'].str.len() <= 30]

        gb = df[df['brand4']==brand4]
        gb.loc[:, 'price'] = gb['price'].astype(int)
        bins = [0, 50, 100, 300, 500, 1000, 2000, 3000, 4000, 5000, 10000, 20000, 99999999]
        labels = ['50及以下', '50到100', '100到300', '300到500', '500到1000', '1000到2000', '2000到3000', '3000到4000',
                  '4000到5000', '5000到10000', '10000到20000',
                  '20000以上']
        gb.loc[:, 'price'] = pd.cut(gb['price'], bins, labels=labels)

        gb2 = gb[gb['price']==priceRanges]

        gb3 = gb2.groupby(
            by=['brand5'],
            as_index=False
        )['commit'].agg({
            'commit': np.sum
        })

        # 取commit前20的
        gb3 = gb3.nlargest(20, 'commit')

        data = dict(zip(gb3['brand5'], gb3['commit']))
        return data

    # 不同店铺销量分析
    def get_brand5_shop_proportion_chart(self, keyId, brand5):
        ds = Data_select()

        df = ds.selectGoods(keyId, '', '', '', '', brand5,'','')

        gb1 = df.groupby(
            by=['shop'],
            as_index=False
        )['commit'].agg({
            'commit': np.sum
        })
        x = gb1['commit'].argsort()[::-1]
        z = x.values[0:10]
        g1 = gb1.iloc[z, :]
        # 按commit降序
        g1 = g1.sort_values(by='commit', ascending=True)
        g1 = g1.reset_index(drop=True)

        # 分别取出shop列和commit,组成列表
        shop = g1['shop'].tolist()
        commit = g1['commit'].tolist()

        data = [shop, commit]

        return data

if __name__ == '__main__':
    dc = Data_chart()
    a = dc.get_brand5_shop_proportion_chart(1, '荣耀X50')

    print(a)


