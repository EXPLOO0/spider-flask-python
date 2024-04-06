import time
from collections import Counter

from data_process import Data_util
from data_storage.Data_select import Data_select


class Data_get:

    def merge_titles(self, titles):
        # 将所有标题拆分为单词
        words = [word for title in titles for word in title.split()]

        # 计算单词频率
        word_freq = Counter(words)

        # 选取频率较高的单词
        common_words = [word for word, freq in word_freq.items() if freq >= len(titles) / 2]

        # 将频率较高的单词拼接为新的标题
        merged_title = ' '.join(common_words)

        return merged_title

    def get_product_introduction(self, keyId, brand1, brand2, brand3, brand4, brand5):
        ds = Data_select()

        # 获取goods表信息，为dataFrame格式
        goods_data = ds.selectGoods(keyId, brand1, brand2, brand3, brand4, brand5, '','')

        # 获取商品名称列表
        title_data = goods_data['title']

        # 合并标题为一个新的标题
        merged_title = self.merge_titles(title_data)

        # 获取goods_data中price列的最大、最小、平均值
        price_max = goods_data['price'].max()
        price_min = goods_data['price'].min()
        price_avg = goods_data['price'].mean()

        # price_max，price_min，price_avg 装置到列表中
        price_list = [price_max, price_min, price_avg]

        # 获取goods_data中commit累计值
        commit_sum = goods_data['commit'].sum()
        commit_sum = str(commit_sum)

        # 获取goods_data中pid列
        pid_df = goods_data['pid']
        # 去除重复
        pid_df = pid_df.drop_duplicates()

        # 获取图片，遍历pid
        pimg_list = []
        for pid in pid_df:
            pimg_list_tmp = ds.selectSpecImg(keyId, pid)
            # 将列表pimg_list_tmp中的每个元素添加到列表pimg_list中
            pimg_list.extend(pimg_list_tmp)
            if len(pimg_list) >= 20:
                break

        # 获取好评率
        # commitCount = ds.selectCommitCount(keyId, pid_df[0], '')
        # commit5Count = ds.selectCommitCount(keyId, pid_df[0], 5)
        # if commitCount == 0:
        #     goodCommit = 0
        # else:
        #     goodCommit = str(commit5Count/commitCount*100)

        data = [brand5, merged_title, price_list, commit_sum, pimg_list, 95]
        return data

    def get_brand5_shop_pid(self, keyId, brand5, shop):
        ds = Data_select()

        # 获取goods表信息，为dataFrame格式
        goods_data = ds.selectGoods(keyId, '', '', '', '', brand5, shop,'')

        # 获取商品名称列表
        pid_data = goods_data['pid']
        # 去重
        pid_data = pid_data.drop_duplicates().tolist()

        return pid_data

    def get_goods_page_sess(self,keyId, pid):
        ds = Data_select()

        # 获取goods表信息，为dataFrame格式
        goods_data = ds.selectGoods(keyId, '', '', '', '', '', '',pid)

        # 去重
        goods_data = goods_data.drop_duplicates()

        title = goods_data['title'].tolist()[0]
        brand3 = goods_data['brand3'].tolist()[0]
        brand4 = goods_data['brand4'].tolist()[0]
        brand5 = goods_data['brand5'].tolist()[0]
        price = goods_data['price'].tolist()[0]
        shop = goods_data['shop'].tolist()[0]
        commit = goods_data['commit'].tolist()[0]
        detail_url = goods_data['detail_url'].tolist()[0]
        sentimentScore = goods_data['sentimentScore'].tolist()[0]
        commit_count = goods_data['commit_count'].tolist()[0]
        count5 = goods_data['count5'].tolist()[0]

        pimg_list = ds.selectSpecImg(keyId, pid)

        # spec_list = ds.selectSpec(keyId, pid)

        data_list = [title, brand3, brand4, brand5, price, shop, commit, detail_url, pimg_list,  sentimentScore, commit_count, count5]
        return data_list

    def get_goods_page_spec(self,keyId, pid):
        ds = Data_select()
        spec_list = ds.selectSpec(keyId, pid)
        return spec_list

    def get_goods_page_chart(self,keyId, pid):
        wcimg = Data_util.generateWordCloud(keyId, pid)

        ds = Data_select()
        # 获取goods表信息，为dataFrame格式
        goods_data = ds.selectGoods(keyId, '', '', '', '', '', '',pid)

        # 去重
        goods_data = goods_data.drop_duplicates()
        # 控制默认设为0
        goods_data = goods_data.fillna(0)

        if goods_data['commit_count'].tolist()[0] != 0:
            count1 = round((goods_data['count1'].tolist()[0] / goods_data['commit_count'].tolist()[0] * 100), 2)
            count2 = round((goods_data['count2'].tolist()[0] / goods_data['commit_count'].tolist()[0] * 100), 2)
            count3 = round((goods_data['count3'].tolist()[0] / goods_data['commit_count'].tolist()[0] * 100), 2)
            count4 = round((goods_data['count4'].tolist()[0] / goods_data['commit_count'].tolist()[0] * 100), 2)
            count5 = round((goods_data['count5'].tolist()[0] / goods_data['commit_count'].tolist()[0] * 100), 2)
        else:
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            count5 = 0
        sentiment1 = round((goods_data['sentiment1'].tolist()[0] * 100), 2)
        sentiment2 = round((goods_data['sentiment2'].tolist()[0] * 100), 2)
        sentiment3 = round((goods_data['sentiment3'].tolist()[0] * 100), 2)
        sentiment4 = round((goods_data['sentiment4'].tolist()[0] * 100), 2)
        sentiment5 = round((goods_data['sentiment5'].tolist()[0] * 100), 2)

        countList = [count1, count2, count3, count4, count5]
        sentimentList = [sentiment1, sentiment2, sentiment3, sentiment4, sentiment5]
        data_list = [wcimg, countList, sentimentList]

        return data_list

    def get_goods_page_commit(self, keyId, pid, score, page):

        ds = Data_select()

        commitList = ds.selectCommit(keyId, pid, score, page)

        dataList = []
        for commit in commitList:
            cid = commit[5]
            commitImgList = ds.selectCommitImgByCid(keyId, cid)
            commit[4] = round((commit[4] * 100), 2)
            data = [commit, commitImgList]
            dataList.append(data)

        return dataList

    def get_home_data(self):
        ds = Data_select()

        keywordCount = ds.selectKeywordCount()
        goodsCount = ds.selectGoodsCount('')
        commitCount = ds.selectCommitCount('')
        commitImg = ds.selectCommitImgCount('')

        data = [keywordCount, goodsCount, commitCount, commitImg]

        return data



if __name__ == '__main__':
    dg = Data_get()

    # a = dg.get_goods_page_commit(1, "10074859458710", '', 1)

    a = dg.get_home_data()

    print(a)
