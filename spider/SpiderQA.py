import pandas as pd

from spider.SpiderQAServer import Spider_answer
import threading

def getQa(qap):
    qa_page = qap

    # 商品问答
    sa = Spider_answer(qa_page)
    #  清除商品问答CSV文件
    sa.clear_csv()

    df = pd.read_csv('static/data/csv/data-goods.csv')


    def test_xc(s, e):
        for i in range(s, e):
            print('--------第' + str(i) + '个--'+str(e)+'--' + str(df.at[i, 'pid']) + '----')
            # 根据商品ID爬取问答信息
            sa.get_product_quest(pid=int(df.at[i, 'pid']))



    p = len(df) // 4
    t1 = threading.Thread(target=test_xc, args=(0, p))
    t1.start()

    t2 = threading.Thread(target=test_xc, args=(p, 2 * p))
    t2.start()

    t3 = threading.Thread(target=test_xc, args=(2 * p, 3 * p))
    t3.start()

    t4 = threading.Thread(target=test_xc, args=(3 * p, len(df)))
    t4.start()

    # 线程全部执行完毕
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    return 0
