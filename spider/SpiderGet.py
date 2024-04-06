from data_storage.Data_delete import Data_delete
from data_storage.Data_insert import Data_insert
from data_storage.Data_select import Data_select
from data_storage.Data_update import Data_update
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
        ds = Data_select()
        du = Data_update()

        print('-----'+self.goods_keyword)
        a = ds.selectKeyword(self.goods_keyword, 2)

        ds.close()
        # 判断a的结果是否存在
        if a != None:
            print('关键词数据已存在')
            kid = a[0]
            print('----'+str(kid))
            if du.updataKeywordStus(kid, 1):
                du.commit()
                SpiderGoodsBrand.getGoodsList(self.goods_keyword, self.goods_page)
                SpiderBSI.getBSI()
                SpiderCommit.getCommit(self.commit_page)
                SpiderQA.getQa(self.qa_page)
                dd = Data_delete()
                dd.deleteAll(kid)
        else:
            print('关键词数据不存在')
            di = Data_insert()
            di.insertKeyword(self.goods_keyword)
            di.commit()
            ds = Data_select()
            a = ds.selectKeyword(self.goods_keyword, 2)
            kid = a[0]
            SpiderGoodsBrand.getGoodsList(self.goods_keyword, self.goods_page)
            SpiderBSI.getBSI()
            SpiderCommit.getCommit(self.commit_page)
            SpiderQA.getQa(self.qa_page)

        dc = Data_clean()
        dc.put_all(kid, self.goods_page, self.commit_page)
        du.updataKeywordStus(kid, 0)
        du.commit()
