import json
import threading
import webbrowser

import numpy as np

from data_process.Data_chart import Data_chart
from flask import Flask, request, send_file, send_from_directory
from flask_cors import CORS

from data_process.Data_get import Data_get
from data_storage.Data_select import Data_select
from spider.SpiderGet import Spider_get

app = Flask(__name__, static_url_path='/',
            static_folder='static', template_folder='templates')
app.static_folder = 'static/dist'
CORS(app)  # 允许所有域名进行跨域请求

@app.route('/')
def indenx():  # put application's code here
    # 打开网页 http://localhost:5173/
    # 跳转
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/insertKeyword', methods=['POST'])
def insertKeyword():
    goods_keyword = request.get_json().get('goods_keyword')
    goods_page = request.get_json().get('goods_page')
    commit_page = request.get_json().get('commit_page')
    qa_page = request.get_json().get('qa_page')
    print(goods_keyword, goods_page, commit_page, qa_page)

    goods_keyword = str(goods_keyword)
    goods_page = int(goods_page)
    commit_page = int(commit_page)
    qa_page = int(qa_page)

    print(goods_keyword, goods_page, commit_page, qa_page)

    sg = Spider_get(goods_keyword, goods_page, commit_page, qa_page)

    def get_data_thread():
        sg.getAll()

    # 开启线程
    data_thread = threading.Thread(target=get_data_thread)
    data_thread.start()


    # data_thread.join()
    return {"code":'200', "mes":'新增成功'}

@app.route('/getKeywordList')
def getKeywordList():
    ds = Data_select()
    keywordList = ds.selectKeyword('none', 0, '')
    # print(keywordList)
    # 返回json数据
    return {"code": '200', "data": keywordList}

@app.route('/getKeywordOne', methods=['GET'])
def getKeywordOne():
    goods_keyword = request.args.get('keyword')
    print('------------'+str(goods_keyword))
    if goods_keyword == 'none' or goods_keyword == None:
        # print('goods_keyword')
        print('true1')
        return {"code": '200', "data": True}
    ds = Data_select()
    keywordList = ds.selectKeyword(goods_keyword, 0, '')
    # print('keywordList')
    if keywordList:
        print('true2')
        return {"code": '200', "data": True}
    print('false')
    return {"code": '200', "data": False}

@app.route('/getBrandPriceRangesChart')
def getBrandPriceRangesChart():
    # 接收参数
    keyId = request.args.get('keyId')
    brand1 = request.args.get('brand1')
    brand2 = request.args.get('brand2')
    brand3 = request.args.get('brand3')

    dc = Data_chart()
    data = dc.get_brand_price_ranges_chart(keyId, brand1, brand2, brand3)
    # print(data)
    # 返回json数据
    return {"code": '200', "data": data}

@app.route('/getBrandPriceRangesTable')
def getBrandPriceRangesTable():
    # 接收参数 keyId
    keyId = request.args.get('keyId')
    # print(keyId)

    dc = Data_chart()
    data = dc.get_brand_price_ranges_chart(keyId)
    # print(data)
    # 返回json数据
    return {"code": '200', "data": data}

@app.route('/getPriceRangesModelChart')
def getPriceRangesModelChart():
    # 接收参数 keyId
    keyId = request.args.get('keyId')
    # 接收参数 brand3
    brand4 = request.args.get('brand4')
    # 接收参数 priceRanges
    priceRanges = request.args.get('priceRanges')
    # print(keyId+'---'+brand3+'---'+priceRanges)

    dc = Data_chart()
    data = dc.get_price_ranges_model_chart(keyId, brand4, priceRanges)
    print(data)
    # 返回json数据
    return {"code": '200', "data": data}

@app.route('/getBrand')
def getBrand():
    # 接收参数
    keyId = request.args.get('keyId')
    brand1 = request.args.get('brand1')
    brand2 = request.args.get('brand2')

    print(keyId, brand1, brand2)
    ds = Data_select()

    if keyId:
        if brand2:
            data = ds.selectBrand3(keyId, brand1, brand2)
        elif brand1:
            data = ds.selectBrand2(keyId, brand1)
        else:
            data = ds.selectBrand1(keyId)

        # print(data)
        return {"code": '200', "data": data}
    else:
        # print(data)
        return {"code": '200', "data": None}

@app.route('/getProductIntroduction')
def getProductIntroduction():
    # 接收参数
    keyId = request.args.get('keyId')
    brand1 = request.args.get('brand1')
    brand2 = request.args.get('brand2')
    brand3 = request.args.get('brand3')
    brand4 = request.args.get('brand4')
    brand5 = request.args.get('brand5')

    print(keyId, brand1, brand2, brand3, brand4, brand5)

    dg = Data_get()
    data = dg.get_product_introduction(keyId, brand1, brand2, brand3, brand4, brand5)
    print(data)
    # 返回json数据
    res = {"code": '200', "data": data}
    return json.dumps(res)

@app.route('/getBrand5ShopProportionChart')
def getBrand5ShopProportionChart():
    # 接收参数
    keyId = request.args.get('keyId')
    brand5 = request.args.get('brand5')
    print('123456----', str(keyId), str(brand5))

    dc = Data_chart()
    data = dc.get_brand5_shop_proportion_chart(keyId, brand5)
    print('111',str(data))
    # 返回json数据
    res = {"code": '200', "data": data}
    return json.dumps(res)

@app.route('/getBrand5ShopPid')
def getBrand5ShopPid():
    # 接收参数
    keyId = request.args.get('keyId')
    brand5 = request.args.get('brand5')
    shop = request.args.get('shop')
    print(keyId, brand5, shop)

    dg = Data_get()
    data = dg.get_brand5_shop_pid(keyId, brand5, shop)
    print(data)
    # 返回json数据
    res = {"code": '200', "data": data}
    return json.dumps(res)

@app.route('/getShopPageSess')
def getShopPageSess():
    # 接收参数
    keyId = request.args.get('keyId')
    pid = request.args.get('pid')
    print(keyId, pid)

    dg = Data_get()
    data = dg.get_goods_page_sess(keyId, pid)
    print(data)
    # 返回json数据
    res = {"code": '200', "data": data}
    return json.dumps(res)

@app.route('/getGoodsPageSpec')
def getGoodsPageSpec():
    # 接收参数
    keyId = request.args.get('keyId')
    pid = request.args.get('pid')
    print(keyId, pid)

    dg = Data_get()
    data = dg.get_goods_page_spec(keyId, pid)
    print(data)
    # 返回json数据
    res = {"code": '200', "data": data}
    return json.dumps(res)

@app.route('/getGoodsPageChart')
def getGoodsPageChart():
    # 接收参数
    keyId = request.args.get('keyId')
    pid = request.args.get('pid')
    print(keyId, pid)

    dg = Data_get()
    data = dg.get_goods_page_chart(keyId, pid)
    print(data)
    # 返回json数据
    res = {"code": '200', "data": data}
    return json.dumps(res)

@app.route('/getGoodsPageCommit')
def getGoodsPageCommit():
    # 接收参数
    keyId = request.args.get('keyId')
    pid = request.args.get('pid')
    score = request.args.get('score')
    page = request.args.get('page')
    print(keyId, pid, score, page)

    dg = Data_get()
    data = dg.get_goods_page_commit(keyId, pid, score, page)
    print(data)
    # 返回json数据
    res = {"code": '200', "data": data}
    return json.dumps(res)

@app.route('/getCommitSortChart')
def getCommitSortChart():
    # 接收参数
    keyId = request.args.get('keyId')
    brand1 = request.args.get('brand1')
    brand2 = request.args.get('brand2')
    brand3 = request.args.get('brand3')

    dc = Data_chart()
    data = dc.get_commit_sort_chart(keyId, brand1, brand2, brand3)
    # print(data)
    # 返回json数据
    return {"code": '200', "data": data}

@app.route('/getHomePageData')
def getHomePageData():
    dg = Data_get()
    data = dg.get_home_data()

    print(data)
    # 返回json数据
    return {"code": '200', "data": data}

@app.route('/getHomePageChartLeft')
def getHomePageChartLeft():
    dc = Data_chart()
    data = dc.get_all_brand1_left_chart()

    print(data)
    # 返回json数据
    return {"code": '200', "data": data}

@app.route('/getHomePageChartCenter')
def getHomePageChartCenter():
    dc = Data_chart()
    data = dc.get_all_center_chart()

    print(data)
    # 返回json数据
    return {"code": '200', "data": data}

@app.route('/getHomePageChartRight')
def getHomePageChartRight():
    # 接收参数
    keyId = request.args.get('keyId')
    brand1 = request.args.get('brand1')
    brand2 = request.args.get('brand2')
    brand3 = request.args.get('brand3')

    dc = Data_chart()
    data = dc.get_all_right_chart(keyId, brand1, brand2, brand3)


    # 返回json数据
    res = {"code": '200', "data": data}

    def default_dump(obj):
        """Convert numpy classes to JSON serializable objects."""
        if isinstance(obj, (np.integer, np.floating, np.bool_)):
            return obj.item()
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return obj

    print(res)

    return json.dumps(res, ensure_ascii=False, default=default_dump)

@app.route('/getChartPagePriceDrawer3')
def getChartPagePriceDrawer3():
    # 接收参数
    keyId = request.args.get('keyId')
    brand1 = request.args.get('brand1')
    brand2 = request.args.get('brand2')
    brand3 = request.args.get('brand3')
    commitRangeIndex = request.args.get('commitRangeIndex')
    priceRangeIndex = request.args.get('priceRangeIndex')

    priceRangeIndex = int(priceRangeIndex)
    commitRangeIndex = int(commitRangeIndex)

    print(keyId, brand1, brand2, brand3, commitRangeIndex, priceRangeIndex)

    dc = Data_chart()
    data = dc.get_chart_price_drawer3_chart(keyId, brand1, brand2, brand3, commitRangeIndex, priceRangeIndex)

    # 返回json数据
    res = {"code": '200', "data": data}

    def default_dump(obj):
        """Convert numpy classes to JSON serializable objects."""
        if isinstance(obj, (np.integer, np.floating, np.bool_)):
            return obj.item()
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return obj

    print(res)

    return json.dumps(res, ensure_ascii=False, default=default_dump)

@app.route('/getPidByBrand5AndIndex')
def getPidByBrand5AndIndex():
    # 接收参数
    keyId = request.args.get('keyId')
    brand1 = request.args.get('brand1')
    brand2 = request.args.get('brand2')
    brand3 = request.args.get('brand3')
    commitRangeIndex = request.args.get('commitRangeIndex')
    priceRangeIndex = request.args.get('priceRangeIndex')
    brand5 = request.args.get('brand5')

    priceRangeIndex = int(priceRangeIndex)
    commitRangeIndex = int(commitRangeIndex)

    dg = Data_get()
    data = dg.getPidByBrand5CommitRangeIndexPriceRangeIndex(keyId, brand1, brand2, brand3, commitRangeIndex, priceRangeIndex, brand5)

    # 返回json数据
    res = {"code": '200', "data": data}

    def default_dump(obj):
        """Convert numpy classes to JSON serializable objects."""
        if isinstance(obj, (np.integer, np.floating, np.bool_)):
            return obj.item()
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return obj

    print(res)

    return json.dumps(res, ensure_ascii=False, default=default_dump)

@app.route('/getGoodsRadarChart')
def getGoodsRadarChart():
    # 接收参数
    keyId = request.args.get('keyId')
    pid = request.args.get('pid')

    dc = Data_chart()
    data = dc.get_goods_radar_chart(keyId, pid)

    # 返回json数据
    res = {"code": '200', "data": data}

    def default_dump(obj):
        """Convert numpy classes to JSON serializable objects."""
        if isinstance(obj, (np.integer, np.floating, np.bool_)):
            return obj.item()
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return obj

    print(res)

    return json.dumps(res, ensure_ascii=False, default=default_dump)

if __name__ == '__main__':
    app.run()
