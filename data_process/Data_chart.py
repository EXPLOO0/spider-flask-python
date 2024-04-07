import math

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
        # print(gb1['commit'] > 50)
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

        df = ds.selectGoods(keyId, brand1, brand2, brand3, '', '', '', '')

        # 排除brand4列为default_value的
        df = df[df['brand1'] != 'default_value']
        df = df[df['brand2'] != 'default_value']
        df = df[df['brand3'] != 'default_value']
        df = df[df['brand4'] != 'default_value']
        df = df[df['brand5'] != 'default_value']

        # 取brand4,brand5,shop,commit列
        df = df[['brand4', 'brand5', 'shop', 'commit', 'price']]
        # 去重
        df = df.drop_duplicates()

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
        labels = ['50及以下', '50到100', '100到300', '300到500', '500到1000', '1000到2000', '2000到3000', '3000到4000',
                  '4000到5000', '5000到10000', '10000到20000',
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

        df = ds.selectGoods(keyId, '', '', '', '', '', '', '')

        df = df[df['brand5'] != 'default_value']

        # 取出df 的brand3列、brand4列、price列、commit列
        df = df[['brand4', 'brand5', 'price', 'commit']]
        df['brand5'] = df['brand5'].str.replace('（.*）', '', regex=True).str.lower()
        df = df[df['brand5'].str.len() <= 30]

        gb = df[df['brand4'] == brand4]
        gb.loc[:, 'price'] = gb['price'].astype(int)
        bins = [0, 50, 100, 300, 500, 1000, 2000, 3000, 4000, 5000, 10000, 20000, 99999999]
        labels = ['50及以下', '50到100', '100到300', '300到500', '500到1000', '1000到2000', '2000到3000', '3000到4000',
                  '4000到5000', '5000到10000', '10000到20000',
                  '20000以上']
        gb.loc[:, 'price'] = pd.cut(gb['price'], bins, labels=labels)

        gb2 = gb[gb['price'] == priceRanges]

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

        df = ds.selectGoods(keyId, '', '', '', '', brand5, '', '')

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

    # 销量排序
    def get_commit_sort_chart(self, keyId, brand1, brand2, brand3):
        ds = Data_select()

        df = ds.selectGoods(keyId, brand1, brand2, brand3, '', '', '', '')

        # brand5列 相同的commit列累加合并
        gb1 = df.groupby(
            by=['brand5'],
            as_index=False
        )['commit'].agg({
            'commit': np.sum
        })
        # 去除 brand5列为default_value的
        gb1 = gb1[gb1['brand5'] != 'default_value']

        # 按commit升序
        gb1 = gb1.sort_values(by='commit', ascending=False)
        gb1 = gb1.reset_index(drop=True)
        # 前20个
        gb1 = gb1.nlargest(20, 'commit')

        # 分别取出brand5列和commit列,组成列表
        brand5 = gb1['brand5'].tolist()
        commit = gb1['commit'].tolist()

        # 倒序
        brand5 = brand5[::-1]
        commit = commit[::-1]

        data = [brand5, commit]

        return data

    # 首页，图表左边两个，所有商品的大分类brand1占比，和所有商品的品牌brand4占比  （前十名）
    def get_all_brand1_left_chart(self):
        ds = Data_select()

        df = ds.selectGoods('', '', '', '', '', '', '', '')

        # 分别获取 brand1列 和 brand4列
        brand1 = df['brand1']
        brand4 = df['brand4']

        # 排除 等于 default_value 的数据
        brand1 = brand1[brand1 != 'default_value']
        brand4 = brand4[brand4 != 'default_value']

        # 排除 等于 ' ' 的数据
        brand1 = brand1[brand1 != ' ']
        brand4 = brand4[brand4 != ' ']

        # brand1
        # 分组统计brand1，并返回计数,只要计数前十的   前六
        gb1 = brand1.value_counts().nlargest(6)

        # 分别取出brand1列和commit列,组成列表
        brand1 = gb1.index.tolist()
        commit1 = gb1.tolist()

        # 倒序
        brand1 = brand1[::-1]
        commit1 = commit1[::-1]

        # brand1ChartData 转换成value:commit,name:brand1
        brand1ChartData = []
        for i in range(len(brand1)):
            brand1ChartData.append({'name': brand1[i], 'value': commit1[i]})

        # brand4
        # 分组统计brand4，并返回计数,只要计数前十的
        gb2 = brand4.value_counts().nlargest(6)

        # 分别取出brand1列和commit列,组成列表
        brand4 = gb2.index.tolist()
        commit4 = gb2.tolist()

        # 倒序
        brand4 = brand4[::-1]
        commit4 = commit4[::-1]

        # brand4ChartData 转换成数据字典
        brand4ChartData = []
        for i in range(len(brand4)):
            brand4ChartData.append({'name': brand4[i], 'value': commit4[i]})

        data = [brand1ChartData, brand4ChartData]

        return data

    # 首页，图表中间  关键词的商品数量、平均价格
    def get_all_center_chart(self):
        ds = Data_select()

        dataDF = ds.selectKeyword('none', 0, '')

        # 循环 dataDF 的元组，将每个元组的第一个存入keyIdList，第二个存入keywordList，第四个存入goodsCountList，第四个存入priceList
        keyIdList = []
        keywordList = []
        goodsCountList = []
        priceList = []
        for i in range(len(dataDF)):
            keyIdList.append(dataDF[i][0])
            # 为空时 默认设为0
            keywordList.append(dataDF[i][1])
            if dataDF[i][2] is None:
                goodsCountList.append(0)
            else:
                goodsCountList.append(dataDF[i][2])
            if dataDF[i][3] is None:
                priceList.append(0)
            else:
                priceList.append(dataDF[i][3])

        data = [keyIdList, keywordList, goodsCountList, priceList]

        return data

    # 首页，图表右边  散点图 （价格，销量）
    def get_all_right_chart(self, kid, brand1, brand2, brand3):
        ds = Data_select()

        dataDF = ds.selectGoods(kid, brand1, brand2, brand3, '', '', '', '')

        # 排除brand5列为default_value的
        dataDF = dataDF[dataDF['brand5'] != 'default_value']
        # 按price排序
        dataDF = dataDF.sort_values(by='price', ascending=False)

        priceRange = [0, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 999999999999]
        commitRange = [0, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 999999999999]

        data = []
        for n in range(len(priceRange)):
            for m in range(len(commitRange)):
                data.append([m, n, 0])

        for i in range(len(dataDF)):
            price = dataDF['price'][i]
            commit = dataDF['commit'][i]

            for j in range(len(priceRange)):
                if j == 0:
                    if price <= priceRange[j]:
                        price_index = j
                        break
                else:
                    if priceRange[j] >= price > priceRange[j - 1]:
                        price_index = j
                        break

            for k in range(len(commitRange)):
                if k == 0:
                    if commit <= priceRange[k]:
                        commit_index = k
                        break
                else:
                    if priceRange[k] >= commit > priceRange[k - 1]:
                        commit_index = k
                        break

            # 增加数据计数
            for l in range(len(data)):
                if data[l][0] == commit_index and data[l][1] == price_index:
                    data[l][2] += 1
                    break

        return data

    # 图表，第三个抽屉的图表，符合价格、销量区间的商品
    def get_chart_price_drawer3_chart(self, keyId, brand1, brand2, brand3, commitRangeIndex, priceRangeIndex):
        ds = Data_select()

        dataDF = ds.selectGoods(keyId, brand1, brand2, brand3, '', '', '', '')

        priceRange = [0, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 999999999999]
        commitRange = [0, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 999999999999]

        if priceRangeIndex == 0:
            priceMax = priceRange[priceRangeIndex]
            priceMin = 0
        else:
            priceMax = priceRange[priceRangeIndex]
            priceMin = priceRange[priceRangeIndex - 1]

        if commitRangeIndex == 0:
            commitMax = commitRange[commitRangeIndex]
            commitMin = 0
        else:
            commitMax = commitRange[commitRangeIndex]
            commitMin = commitRange[commitRangeIndex - 1]

        dataDF = dataDF[(dataDF['price'] > priceMin) & (dataDF['price'] <= priceMax) & (dataDF['commit'] > commitMin) & (dataDF['commit'] <= commitMax)]

        # 获取title, commit
        # allData = dataDF[['brand5', 'commit', 'price', 'sentimentScore']].values.tolist()

        # 根据 ‘brand’ 列 ，取commit、price和sentimentScore的平均值

        dataDF = dataDF.groupby('brand5').agg({'commit': 'mean', 'price': 'mean', 'sentimentScore': 'mean'}).reset_index()
        dataDF.columns = ['brand5', 'commit', 'price', 'sentimentScore']
        dataDF = dataDF.sort_values(by='commit', ascending=False).head(10)

        brand5 = dataDF['brand5'].tolist()
        commit = dataDF['commit'].tolist()
        price = dataDF['price'].tolist()
        sentimentScore = dataDF['sentimentScore'].tolist()

        data = [brand5, commit, price, sentimentScore]

        return data

    # 商品雷达图
    def get_goods_radar_chart(self, keyId, pid):
        # 获取关键词平均价格
        ds = Data_select()
        keywordDF = ds.selectKeyword(keyword='none', value=0, keyId=keyId)

        # 计算平均价格
        average_price = keywordDF[0][3]
        average_price = float(average_price)

        # 根据平均价格确定档位价格范围
        low_price_range = average_price / 2
        high_price_range = average_price * 1.5  # 自定义高档位的范围，这里假设是平均价格的1.5倍

        allGoodsDF = ds.selectGoods(keyId, '', '', '', '', '', '', '')

        goodsDF = ds.selectGoods(keyId, '', '', '', '', '', '',pid)

        goodsPrice = goodsDF['price'].tolist()[0]
        goodsCommit = goodsDF['commit'].tolist()[0]
        goodsSentimentScore = goodsDF['sentimentScore'].tolist()[0] * 100
        try:
            goodsCommitGood = ( goodsDF['count5'].tolist()[0] /  goodsDF['commit_count'].tolist()[0] ) * 100
        except:
            goodsCommitGood = 0

        # 判断档位
        if goodsPrice <= low_price_range:
            level = 1
            levelValue = '低'
            # allGoodsDF 中 price <= low_price_range 的商品的平均值
            avgerage_price = allGoodsDF[allGoodsDF['price'] <= low_price_range]['price'].mean()
        elif goodsPrice <= high_price_range:
            level = 2
            levelValue = '中'
            # allGoodsDF 中 price > low_price_range price <= low_price_range 的商品的平均值
            avgerage_price = allGoodsDF[(allGoodsDF['price'] > low_price_range) & (allGoodsDF['price'] <= high_price_range)]['price'].mean()
        else:
            level = 3
            levelValue = '高'
            # allGoodsDF 中 price > low_price_range 的商品的平均值
            avgerage_price = allGoodsDF[allGoodsDF['price'] > high_price_range]['price'].mean()

        deviation = ((goodsPrice - avgerage_price) / avgerage_price) * 100

        # deviation 为负数时，去掉负号
        if deviation < 0:
            deviation = deviation * -1

        # 都保留两位小数
        deviation = round(deviation, 2)
        goodsSentimentScore = round(goodsSentimentScore, 2)
        goodsCommitGood = round(goodsCommitGood, 2)

        commitRange = [0, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 999999999999]

        # 判断goodsCommit属于哪一个区间，返回下标
        goodsIndex = -1
        if goodsCommit > 0:
            for i in range(len(commitRange)):
                if goodsCommit > commitRange[i] and goodsCommit <= commitRange[i + 1]:
                    goodsIndex = i + 1
                    break
        else:
            goodsIndex = 0

        # goodsIndex >13 或 goodsIndex = -1 时 设为13
        if goodsIndex > 13 or goodsIndex == -1:
            goodsIndex  = 13

        data = [
            [deviation, goodsIndex, goodsCommitGood, goodsSentimentScore, level],
            [goodsCommit, goodsPrice, avgerage_price, levelValue]
        ]

        return data


if __name__ == '__main__':
    dc = Data_chart()
    a = dc.get_goods_radar_chart(16, '100082369233')

    print(a)
