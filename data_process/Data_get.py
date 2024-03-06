from collections import Counter

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

        pimg_list = ds.selectSpecImg(keyId, pid)

        # spec_list = ds.selectSpec(keyId, pid)

        data_list = [title, brand3, brand4, brand5, price, shop, commit, detail_url, pimg_list]
        return data_list

    def get_goods_page_spec(self,keyId, pid):
        ds = Data_select()
        spec_list = ds.selectSpec(keyId, pid)
        return spec_list

if __name__ == '__main__':
    dg = Data_get()

    a = dg.get_goods_page_spec(23, "100068991305")

    print(a)
