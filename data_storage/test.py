from spider.SpiderQAServer import Spider_answer
from spider.SpiderCommitServer import Spider_commit
from spider.Spider_goods import Spider_goods
from spider.Spider_spec import Spider_spec


class Data_get:
    goods_keyword = ''
    goods_page = 20
    commit_page = 20
    qa_page = 20

    def __init__(self, goods_keyword, goods_page, commit_page, qa_page):
        self.goods_keyword = goods_keyword
        self.goods_page = goods_page
        self.commit_page = commit_page
        self.qa_page = qa_page


    def getData(self):

        # 商品列表
        sg = Spider_goods(self.goods_keyword, self.goods_page)
        # 获取商品ID
        idList = sg.get_product_id()

        # 商品评论
        sc = Spider_commit('', '', '')
        # 清除商品评论CSV文件
        sc.clear_csv()

        # 商品问答
        sa = Spider_answer(self.qa_page)
        #  清除商品问答CSV文件
        sa.clear_csv()

        for id in idList:
            # 根据商品ID爬取评论
            sc = Spider_commit(productId=int(idList[id]), page=self.commit_page, score=0)
            sc.csv_write()
            # 根据商品ID爬取问答信息
            sa.get_product_quest(pid=int(idList[id]))

if __name__ == '__main__':
    dg = Data_get('', 20, 20, 20)
    dg.getData()