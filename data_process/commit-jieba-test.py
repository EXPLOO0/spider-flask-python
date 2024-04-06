

from data_storage.Data_select import Data_select

import jieba
from collections import Counter


def extract_keywords_from_comments(comments):
    # 定义停用词列表
    stopwords = ['的', '了', '也', '是', '在', '和', '有', '就', '中', '这', '不', '我', '你', '他', '她', '我们',
                 '你们', '他们', '很', '太', '非常', '简直', '真的', '还行', '不算', '太']

    # 定义表示程度的词语
    degree_words = ['很', '太', '非常', '简直', '真的', '还行', '不算', '太']

    # 将所有评论拼接成一个长字符串
    text = ''.join(comments)

    # 使用jieba分词进行中文分词，并过滤停用词、表示程度的词语和标点符号
    words = [word for word in jieba.cut(text) if word not in stopwords and word not in degree_words and word.isalnum()]

    # 使用Counter统计词频
    word_counter = Counter(words)

    # 获取出现频率最高的前N个词作为关键信息
    top_keywords = word_counter.most_common(30)  # 可以根据需求调整提取的关键词数量
    return top_keywords


ds = Data_select()
a = ds.selectCommit(17,100061054752)

keywords = extract_keywords_from_comments(a[3])
print("Top Keywords:")
for keyword, count in keywords:
    print(f"{keyword}: {count}")
