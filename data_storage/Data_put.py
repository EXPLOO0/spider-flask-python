from data_process import Data_clean
from data_storage.Data_insert import Data_insert
from data_storage.Data_select import Data_select


def putGoods(keyword):
    ds = Data_select()
    keyId = ds.selectKeyword(keyword=keyword, value=0)

    df = Data_clean.goods_process()
    # df为处理后的csv文件数据
    di = Data_insert()
    # insertGoods(self, keyId, pid, brand1, brand2, brand3, brand4, title, price, commit, shop, detail_url):方法写入数据库
    # 循环使用insertGoods将df的数据写入数据库
    # 遍历每一行
    for index, row in df.iterrows():
        # 写入数据
        di.insertGoods(keyId, row['pid'], row['brand1'], row['brand2'], row['brand3'],
                       row['brand4'], row['title'], row['price'], row['commit'], row['shop'], row['detail_url'])