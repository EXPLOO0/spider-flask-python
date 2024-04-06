import base64

import jieba
from wordcloud import WordCloud
from PIL import Image # 和词云库一起装的
import numpy as np # 科学计算库，和词云库一起装的，导入numpy并且取别名
from snownlp import SnowNLP

from data_storage.Data_select import Data_select

def generateWordCloud(kid, pid):
    ds = Data_select()
    dataList = ds.selectCommit(kid, pid, '', '')

    # 调用读取评论的方法
    commenrList = []

    # 循环a list
    for i in dataList:
        commenrList.append(i[3])

    if len(commenrList) == 0:
        return "该商品评论为空"
    finalComments = ""
    # 将所有评论拼接成一个完整的字符串
    for comment in commenrList:
        finalComments += comment
    # 再做分词切割
    finalComments = " ".join(jieba.cut(finalComments))
    # 使用Image将图片读取到程序中，并且使用numpy处理成ndarray格式
    image = np.array(Image.open("static/data/wordcloud/img/云2.jpeg"))

    # 定义停用词列表
    stopwords = ['的', '了', '也', '是', '在', '和', '有', '就', '中', '这', '不', '我', '你', '他', '她', '我们',
                 '你们', '他们', '很', '太', '非常', '简直', '真的', '还行', '不算', '太']

    # 实例化词云对象
    # font_path:本机字体路径（相对或绝对都行）
    # background_color:背景颜色
    # mask:词云的轮廓，白色不会赋值
    wordCloud = WordCloud(
        # font_path="C:/Windows/Fonts/simsun.ttc",
        font_path="../static/data/wordcloud/simsun.ttc",
        width=800,
        height=400,
        background_color="white",
        mask=image,
        stopwords=stopwords
    ).generate(finalComments)
    # 生成词云文件
    wordCloud.to_file("static/data/wordcloud/wc_tmp.png")

    # 返回前端能直接用的图片在服务器的地址
    return "http://127.0.0.1:5000/static/data/wordcloud/wc_tmp.png"

def analyze_sentiment_detailed(comment):
    s = SnowNLP(comment)
    sentiment_score = s.sentiments
    # 根据情感得分划分为积极、中性和消极三个维度
    # if sentiment_score > 0.6:
    #     sentiment = '积极'
    # elif sentiment_score < 0.4:
    #     sentiment = '消极'
    # else:
    #     sentiment = '中性'
    # return {
    #     'Sentiment': sentiment,
    #     'Positive': sentiment_score,
    #     'Negative': 1 - sentiment_score
    # }
    return sentiment_score