import json
import threading
import webbrowser

from data_process.Data_chart import Data_chart
from flask import Flask, request
from flask_cors import CORS

from data_process.Data_get import Data_get
from data_storage.Data_select import Data_select
from spider.SpiderGet import Spider_get

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})  # 允许所有域名进行跨域请求

@app.route('/')
def indenx():  # put application's code here
    # 打开网页 http://localhost:5173/
    # 跳转
    webbrowser.open('http://localhost:5173/')
    return 0

@app.route('/insertKeyword', methods=['POST'])
def insertKeyword():
    goods_keyword = request.form.get('goods_keyword')
    goods_page = request.form.get('goods_page')
    commit_page = request.form.get('commit_page')
    qa_page = request.form.get('qa_page')

    print('---'+goods_keyword+'---'+goods_page+'---'+commit_page+'---'+qa_page+'---')

    goods_keyword = str(goods_keyword)
    goods_page = int(goods_page)
    commit_page = int(commit_page)
    qa_page = int(qa_page)


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
    keywordList = ds.selectKeyword('none')
    # print(keywordList)
    # 返回json数据
    return {"code": '200', "data": keywordList}

@app.route('/getKeywordOne')
def getKeywordOne():
    goods_keyword = request.args.get('keyword')
    if goods_keyword == 'none' or goods_keyword == None:
        # print('goods_keyword')
        return {"code": '200', "data": True}
    ds = Data_select()
    keywordList = ds.selectKeyword(goods_keyword)
    # print('keywordList')
    if keywordList:
        return {"code": '200', "data": True}
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
    brand3 = request.args.get('brand3')
    # 接收参数 priceRanges
    priceRanges = request.args.get('priceRanges')
    # print(keyId+'---'+brand3+'---'+priceRanges)

    dc = Data_chart()
    data = dc.get_price_ranges_model_chart(keyId, brand3, priceRanges)
    # print(data)
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

    if brand2:
        data = ds.selectBrand3(keyId, brand1, brand2)
    elif brand1:
        data = ds.selectBrand2(keyId, brand1)
    else:
        data = ds.selectBrand1(keyId)

    # print(data)
    return {"code": '200', "data": data}

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
    print(keyId, brand5)

    dc = Data_chart()
    data = dc.get_brand5_shop_proportion_chart(keyId, brand5)
    print(data)
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



if __name__ == '__main__':
    app.run()
