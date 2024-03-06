from data_storage.Data_insert import Data_insert
from data_storage.Data_select import Data_select
from spider import SpiderGoodsBrand, SpiderBSI, SpiderCommit, SpiderQA
from data_process.Data_clean import Data_clean

class Spider_get:
    goods_keyword = '笔记本电脑'
    goods_page = 30
    commit_page = 15
    qa_page = 5

    def __init__(self, goods_keyword, goods_page, commit_page, qa_page):
        self.goods_keyword = goods_keyword
        self.goods_page = goods_page
        self.commit_page = commit_page
        self.qa_page = qa_page


    def getAll(self):
        SpiderGoodsBrand.getGoodsList(self.goods_keyword, self.goods_page)

        SpiderBSI.getBSI()

        SpiderCommit.getCommit(self.commit_page)

        SpiderQA.getQa(self.qa_page)

        ds = Data_select()
        di = Data_insert()

        a = ds.selectKeyword(self.goods_keyword)
        ds.close()

        if a:
            print('关键词数据已存在')
            print(a[0])
            dc = Data_clean()
            dc.put_all(a[0])
        else:
            print('关键词数据不存在')
            di.insertKeyword(self.goods_keyword)
            di.commit()
            ds = Data_select()
            kd = ds.selectKeyword(self.goods_keyword)

            print(kd[0])
            dc = Data_clean()
            dc.put_all(kd[0])

